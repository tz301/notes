#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by tz301 on 2020/7/10
"""Pitch特征."""
import logging
from math import ceil, cos, floor, gcd, pi, sin

import numpy as np

from base.utils import LOGGER_FORMAT


def _lcm(num1, num2):
  """计算最小公倍数.

  Args:
    num1: 数字1.
    num2: 数字2.

  Returns:
    最小公倍数.
  """
  return abs(num1 * num2) // gcd(num1, num2)


class LinearResampler:
  """线性重采样类, 要求时间间隔线性.

  Attributes:
    __in_sample_rate: 输入信号的采样频率.
    __out_sample_rate: 输出信号的采样频率.
    __cutoff_freq: 滤波的截止频率.
    __in_samples_in_unit: 输入采样点数的最小单位.
    __out_samples_in_unit: 输出采样点数的最小单位.
    __window_width: 采样窗宽.
    __first_index: 输出样本点对应的第一个输入样本点索引.
    __weights: 窗函数权重.
    __input_offset: 输入信号的偏置.
    __output_offset: 输出信号的偏置.
    __input_buffer: 输入信号的缓存.
  """

  def __init__(self, in_sample_rate, out_sample_rate, cutoff_freq):
    """初始化.

    Args:
      in_sample_rate: 输入信号的采样频率.
      out_sample_rate: 输出信号的采样频率.
      cutoff_freq: 滤波的截止频率.
    """
    self.__in_sample_rate = in_sample_rate
    self.__out_sample_rate = out_sample_rate
    self.__cutoff_freq = cutoff_freq
    self.__check()

    base_freq = gcd(in_sample_rate, out_sample_rate)
    self.__in_samples_in_unit = int(in_sample_rate / base_freq)
    self.__out_samples_in_unit = int(out_sample_rate / base_freq)
    self.__window_width = 1 / (2 * self.__cutoff_freq)
    self.__first_index = [0] * self.__out_samples_in_unit
    self.__weights = [np.array([0]) for _ in range(self.__out_samples_in_unit)]
    self.__set_indexes_and_weights()

    self.__input_offset = 0
    self.__output_offset = 0
    self.__input_buffer = np.array([])

  def __check(self):
    """参数检查."""
    assert self.__in_sample_rate > 0
    assert self.__out_sample_rate > 0
    assert self.__cutoff_freq > 0
    assert self.__cutoff_freq * 2 < self.__in_sample_rate
    assert self.__cutoff_freq * 2 < self.__out_sample_rate

  def __filter(self, t_index):
    """滤波, Hanning窗 + sinc函数.

    Args:
      t_index: 以窗中心为基准的时间索引.

    Returns:
      窗函数滤波值.
    """
    if abs(t_index) < self.__window_width:
      coeff = 2 * pi * self.__cutoff_freq
      window = 0.5 * (1 + cos(coeff * t_index))
    else:
      window = 0

    if t_index != 0:
      filter_value = sin(2 * pi * self.__cutoff_freq * t_index) / (pi * t_index)
    else:
      filter_value = 2 * self.__cutoff_freq
    return filter_value * window

  def __set_indexes_and_weights(self):
    """设置索引和权重."""
    for i in range(self.__out_samples_in_unit):
      output_t = i / self.__out_sample_rate
      min_t = output_t - self.__window_width
      max_t = output_t + self.__window_width
      min_input_index = int(ceil(min_t * self.__in_sample_rate))
      max_input_index = int(floor(max_t * self.__in_sample_rate))
      num_indices = max_input_index - min_input_index + 1

      self.__first_index[i] = min_input_index
      self.__weights[i] = np.zeros(num_indices)
      for j in range(num_indices):
        input_index = min_input_index + j
        input_t = input_index / self.__in_sample_rate
        delta_t = input_t - output_t
        self.__weights[i][j] = self.__filter(delta_t) / self.__in_sample_rate

  def __num_output_samples(self, num_input_samples, is_end):
    """获取输出样本数量.

    Args:
      num_input_samples: 输入样本数量.
      is_end: 是否结束.

    Returns:
      输出样本数量.
    """
    tick_freq = _lcm(self.__in_sample_rate, self.__out_sample_rate)
    ticks_per_input_period = int(tick_freq / self.__in_sample_rate)
    interval_length_in_ticks = num_input_samples * ticks_per_input_period

    if not is_end:
      interval_length_in_ticks -= int(floor(self.__window_width * tick_freq))

    ticks_per_output_period = int(tick_freq / self.__out_sample_rate)
    last_output_samp = int(interval_length_in_ticks / ticks_per_output_period)
    if last_output_samp * ticks_per_output_period == interval_length_in_ticks:
      last_output_samp -= 1
    return last_output_samp + 1

  def __get_indexes(self, output_index):
    """获取索引.

    Args:
      output_index: 输出采样点索引.

    Returns:
      第一个输入采样点索引和求余后的输出采样点索引.
    """
    unit_index = int(output_index / self.__out_samples_in_unit)
    samp_out_wrapped = output_index - unit_index * self.__out_samples_in_unit
    first_input_index = (self.__first_index[samp_out_wrapped] +
                         unit_index * self.__in_samples_in_unit)
    return first_input_index, samp_out_wrapped

  def __update_buffer(self, signal):
    """更新buffer.

    Args:
      signal: 信号.
    """
    old_buffer = self.__input_buffer.copy()
    max_needed = int(ceil(self.__in_sample_rate / self.__cutoff_freq))
    self.__input_buffer = np.zeros(max_needed)

    for i in range(-max_needed, 0):
      input_index = i + len(signal)
      if input_index > 0:
        self.__input_buffer[i + max_needed] = signal[input_index]
      elif input_index + len(old_buffer) >= 0:
        self.__input_buffer[i + max_needed] = old_buffer[i + len(old_buffer)]

  def __reset(self):
    """重置."""
    self.__input_offset = 0
    self.__output_offset = 0
    self.__input_buffer = np.array([])

  def resample(self, signal, is_end):
    """对信号进行重采样.

    Args:
      signal: 信号.
      is_end: 是否结束.

    Returns:
      重采样后的信号.
    """
    sig_dim = len(signal)
    num_input_samples = self.__input_offset + sig_dim
    num_output_samples = self.__num_output_samples(num_input_samples, is_end)

    outputs = np.zeros(num_output_samples - self.__output_offset)
    for samp_out in range(self.__output_offset, num_output_samples):
      first_input_index, samp_out_wrapped = self.__get_indexes(samp_out)
      weights = self.__weights[samp_out_wrapped]
      weights_dim = len(weights)
      first_input_index -= self.__input_offset
      output_index = samp_out - self.__output_offset

      if first_input_index >= 0 and first_input_index + weights_dim <= sig_dim:
        cur_sig = signal[first_input_index:first_input_index + weights_dim]
        outputs[output_index] = np.dot(cur_sig, weights)
      else:  # 边界处理.
        for i in range(weights_dim):
          weight = weights[i]
          input_index = first_input_index + i
          buffer_index = len(self.__input_buffer) + input_index
          if input_index < 0 <= buffer_index:
            outputs[output_index] += weight * self.__input_buffer[buffer_index]
          elif 0 <= input_index < sig_dim:
            outputs[output_index] += weight * signal[input_index]
          elif input_index >= sig_dim:
            assert is_end

    if is_end:
      self.__reset()
    else:
      self.__input_offset = num_input_samples
      self.__output_offset = num_output_samples
      self.__update_buffer(signal)
    return outputs


class PitchExtractor:
  """Pitch特征提取器.

  Attributes:
    __is_end: 是否结束.
    __resampler: 重采样类.
  """

  def __init__(self, sample_rate):
    """初始化.

    Args:
      sample_rate: 采样频率.
    """
    self.__is_end = False

    resample_sample_rate = 3000
    cutoff_freq = 1000
    self.__resampler = LinearResampler(sample_rate, resample_sample_rate,
                                       cutoff_freq)

  def __accept_wave_form(self, signal):
    """接收音频数据.

    Args:
      signal: 信号.
    """
    signal = self.__resampler.resample(signal, self.__is_end)

  def __input_finished(self):
    """完成所有输入."""
    self.__is_end = True
    self.__accept_wave_form([])

  def __reset(self):
    """重置."""
    self.__is_end = False

  def extract(self, signal):
    """提取pitch特征.

    Args:
      signal: 信号.

    Returns:
      pitch特征.
    """
    self.__accept_wave_form(signal)
    self.__input_finished()
    self.__reset()
    return np.zeros((1, 1))


def __cmd():
  """命令行函数."""
  num = 1000
  sample_rate = 16000
  signal = np.zeros(num, dtype=np.int)
  for i in range(num):
    signal[i] = (abs(i * 433024) % 65535) - (65535 // 2)

  feature = PitchExtractor(sample_rate).extract(signal)
  logging.info(f'pitch特征维度: {feature.shape}.')


if __name__ == '__main__':
  logging.basicConfig(format=LOGGER_FORMAT, level=logging.INFO)
  __cmd()
