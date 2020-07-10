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

  def __get_num_output_samples(self, num_input_samples):
    """获取输出样本数量.

    Args:
      num_input_samples: 输入样本数量.

    Returns:
      输出样本数量.
    """
    tick_freq = _lcm(self.__in_sample_rate, self.__out_sample_rate)
    ticks_per_input_period = int(tick_freq / self.__in_sample_rate)
    interval_length_in_ticks = num_input_samples * ticks_per_input_period

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

  def resample(self, signal):
    """对信号进行重采样.

    Args:
      signal: 信号.

    Returns:
      重采样后的信号.
    """
    sig_dim = len(signal)
    num_output_samples = self.__get_num_output_samples(sig_dim)

    outputs = np.zeros(num_output_samples)
    for out_index in range(num_output_samples):
      first_input_index, samp_out_wrapped = self.__get_indexes(out_index)
      weights = self.__weights[samp_out_wrapped]
      weights_dim = len(weights)

      if first_input_index >= 0 and first_input_index + weights_dim <= sig_dim:
        cur_sig = signal[first_input_index:first_input_index + weights_dim]
        outputs[out_index] = np.dot(cur_sig, weights)
      else:  # 边界处理.
        for i in range(weights_dim):
          input_index = first_input_index + i
          if 0 <= input_index < sig_dim:
            outputs[out_index] += weights[i] * signal[input_index]
    return outputs


def pitch(signal, sample_rate):
  """提取pitch特征.

  Args:
    signal: 信号.
    sample_rate: 采样频率.

  Returns:
    pitch特征.
  """
  resampler = LinearResampler(sample_rate, 3000, 1000)
  signal = resampler.resample(signal)
  return np.zeros((1, 1))


def __cmd():
  """命令行函数."""
  num = 1000
  sample_rate = 16000
  signal = np.zeros(num, dtype=np.int)
  for i in range(num):
    signal[i] = (abs(i * 433024) % 65535) - (65535 // 2)

  feature = pitch(signal, sample_rate)
  logging.info(f'pitch特征维度: {feature.shape}.')


if __name__ == '__main__':
  logging.basicConfig(format=LOGGER_FORMAT, level=logging.INFO)
  __cmd()
