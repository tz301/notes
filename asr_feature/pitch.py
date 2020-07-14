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


def _filter(t_index, cutoff_freq, num_zeros):
  """滤波, Hanning窗 + sinc函数.

  Args:
    t_index: 以窗中心为基准的时间索引.

  Returns:
    窗函数滤波值.
  """
  window_width = num_zeros / (2 * cutoff_freq)
  if abs(t_index) < window_width:
    coeff = 2 * pi * cutoff_freq / num_zeros
    window = 0.5 * (1 + cos(coeff * t_index))
  else:
    window = 0

  if t_index != 0:
    filter_value = sin(2 * pi * cutoff_freq * t_index) / (pi * t_index)
  else:
    filter_value = 2 * cutoff_freq
  return filter_value * window


class LinearResampler:
  """线性重采样类, 要求时间间隔线性.

  Attributes:
    __in_sample_rate: 输入信号的采样频率.
    __out_sample_rate: 输出信号的采样频率.
    __cutoff_freq: 滤波的截止频率.
    __num_zeros: 滤波的零的数量.
    __in_samples_in_unit: 输入采样点数的最小单位.
    __out_samples_in_unit: 输出采样点数的最小单位.
    __window_width: 采样窗宽.
    __first_index: 输出样本点对应的第一个输入样本点索引.
    __weights: 窗函数权重.
    __input_offset: 输入信号的偏置.
    __output_offset: 输出信号的偏置.
    __input_buffer: 输入信号的缓存.
  """

  def __init__(self, in_sample_rate, out_sample_rate, cutoff_freq, num_zeros=1):
    """初始化.

    Args:
      in_sample_rate: 输入信号的采样频率.
      out_sample_rate: 输出信号的采样频率.
      cutoff_freq: 滤波的截止频率.
      num_zeros: 滤波的零的数量, 默认1.
    """
    self.__in_sample_rate = in_sample_rate
    self.__out_sample_rate = out_sample_rate
    self.__cutoff_freq = cutoff_freq
    self.__num_zeros = num_zeros
    self.__check()

    base_freq = gcd(in_sample_rate, out_sample_rate)
    self.__in_samples_in_unit = int(in_sample_rate / base_freq)
    self.__out_samples_in_unit = int(out_sample_rate / base_freq)
    self.__window_width = num_zeros / (2 * self.__cutoff_freq)
    self.__first_index = np.zeros(self.__out_samples_in_unit, dtype=np.int)
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
    assert self.__num_zeros > 0

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
        filter_value = _filter(delta_t, self.__cutoff_freq, self.__num_zeros)
        self.__weights[i][j] = filter_value / self.__in_sample_rate

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


class ArbitraryResample:
  """重采样类, 允许非线性时间间隔的重采样.

  Attributes:
    __num_in_samples: 输入样本点数.
    __in_sample_rate: 采样频率.
    __cutoff_freq: 滤波的截止频率.
    __num_zeros: 滤波的零的数量.
    __num_out_samples: 输出样本数量.
    __window_width: 采样窗宽.
    __first_index: 输出样本点对应的第一个输入样本点索引.
    __weights: 窗函数权重.
  """

  def __init__(self, num_in_samples, in_sample_rate, cutoff_freq,
               sample_points, num_zeros):
    """初始化.

    Args:
      num_in_samples: 输入样本点数.
      in_sample_rate: 采样频率.
      cutoff_freq: 滤波的截止频率.
      sample_points: 采样点对应的时间列表, 单位s.
      num_zeros: 滤波的零的数量.
    """
    self.__num_in_samples = num_in_samples
    self.__in_sample_rate = in_sample_rate
    self.__cutoff_freq = cutoff_freq
    self.__num_zeros = num_zeros
    self.__check()

    self.__num_out_samples = len(sample_points)
    self.__window_width = num_zeros / (2 * self.__cutoff_freq)
    self.__first_index = np.zeros(len(sample_points), dtype=np.int)
    self.__weights = [np.array([0]) for _ in sample_points]
    self.__set_indexes_and_weights(sample_points)

  def __check(self):
    """参数检查."""
    assert self.__num_in_samples > 0
    assert self.__in_sample_rate > 0
    assert self.__cutoff_freq > 0
    assert self.__cutoff_freq * 2 <= self.__in_sample_rate
    assert self.__num_zeros > 0

  def __set_indexes_and_weights(self, sample_points):
    """设置索引和权重.

    Args:
      sample_points: 采样点对应的时间列表, 单位s.
    """
    for i in range(len(sample_points)):
      t = sample_points[i]
      t_min = t - self.__window_width
      t_max = t + self.__window_width
      index_min = int(ceil(t_min * self.__in_sample_rate))
      index_max = int(ceil(t_max * self.__in_sample_rate))
      index_min = max(index_min, 0)
      index_max = min(index_max, self.__num_in_samples - 1)
      self.__first_index[i] = index_min

      num_indices = index_max - index_min + 1
      self.__weights[i] = np.zeros(num_indices)
      for j in range(num_indices):
        delta_t = sample_points[i] - (index_min + j) / self.__in_sample_rate
        filter_value = _filter(delta_t, self.__cutoff_freq, self.__num_zeros)
        self.__weights[i][j] = filter_value / self.__in_sample_rate

  def resample(self, signal):
    """对信号进行重采样.

    Args:
      signal: 信号.

    Returns:
      重采样后的信号.
    """
    output = np.zeros((len(signal), self.__num_out_samples))
    for i in range(self.__num_out_samples):
      first_index = self.__first_index[i]
      weight = self.__weights[i]
      sub_input = signal[:, first_index: first_index + len(weight)]
      output[:, i] = np.dot(sub_input, weight)
    return output


class PitchConfig:
  """Pitch配置.

  Attributes:
    sample_rate: 采样频率.
    frame_shift: 帧移.
    frame_length: 帧长.
    min_f0: 最小f0.
    max_f0: 最大f0.
    soft_min_f0: 最小soft f0.
    penalty_factor:
    lowpass_cutoff: 低通截止频率.
    resample_freq: 重采样频率.
    delta_pitch: pitch间隔.
    nccf_ballast: nccf_ballast.
    upsample_filter_width: 上采样滤波宽度.
    max_frames_latency: 最大帧延迟.
    frames_per_chunk:
    recompute_frame:
    nccf_shift: nccf帧移.
    nccf_length: nccf帧长.
  """

  def __init__(self, sample_rate):
    """初始化.

    Args:
      sample_rate: 采样频率.
    """
    self.sample_rate = sample_rate
    self.frame_shift = 0.01
    self.frame_length = 0.025
    self.min_f0 = 50
    self.max_f0 = 400
    self.soft_min_f0 = 10
    self.penalty_factor = 0.1
    self.lowpass_cutoff = 1000
    self.resample_freq = 4000
    self.delta_pitch = 0.005
    self.nccf_ballast = 7000
    self.upsample_filter_width = 5
    self.max_frames_latency = 0
    self.frames_per_chunk = 0
    self.recompute_frame = 500
    self.nccf_shift = int(self.resample_freq * self.frame_shift)
    self.nccf_length = int(self.resample_freq * self.frame_length)


class StateInfo:
  """状态信息类, 用于Viterbi计算, 储存一帧计算所需的偏移.

  Attributes:
    __back_pointer: 当前状态最优的上一状态帧的状态索引.
    __pov_nccf: pov计算的nccf.
  """

  def __init__(self):
    """初始化."""
    self.__back_pointer = 0
    self.__pov_nccf = 0


class PitchFrameInfo:
  """Pitch帧信息类, 储存用于计算一帧pitch的信息.

  Attributes:
    __state_info: 状态信息.
    __state_offset: 状态偏移.
    __cur_best_state: 当前最好的状态.
    __prev_info: 前一个状态信息.
  """

  def __init__(self, num_states):
    """初始化.

    Args:
      num_states: 状态数.
    """
    self.__state_info = [StateInfo] * num_states
    self.__state_offset = 0
    self.__cur_best_state = -1
    self.__prev_info = None


class NccfInfo:
  """Nccf信息类.

  Attributes:
    avg_norm_prod: 平均范数内积.
    mean_square_energy: 均方能量.
  """

  def __init__(self, avg_norm_prod, mean_square_energy):
    """初始化.

    Args:
      avg_norm_prod: 平均范数内积.
      mean_square_energy: 均方能量.
    """
    self.avg_norm_prod = avg_norm_prod
    self.mean_square_energy = mean_square_energy


class PitchExtractor:
  """Pitch特征提取器.

  Attributes:
    __is_end: 是否结束.
    __conf: pitch配置类.
    __resampler: 重采样类.
    __num_processed: 已处理的样本数.
    __buffer: 缓存.
    __signal_sum: 重采样后信号和.
    __signal_sum_sq: 重采样后信号平方和.
    __nccf_first_lag: 第一个nccf偏移值.
    __nccf_last_lag: 最后一个nccf偏移值.
    __lags: nccf偏移列表.
    __num_lags: nccf偏移数.
    __nccf_resampler: nccf重采样类.
    __frames_latency:
    __frame_info:
    __forward_cost:
    __nccf_info:
  """

  def __init__(self, sample_rate):
    """初始化.

    Args:
      sample_rate: 采样频率.
    """
    self.__is_end = False
    self.__conf = PitchConfig(sample_rate)
    self.__resampler = LinearResampler(sample_rate, self.__conf.resample_freq,
                                       self.__conf.lowpass_cutoff)

    self.__num_processed = 0
    self.__buffer = list()

    self.__signal_sum = 0
    self.__signal_sum_sq = 0

    win = self.__conf.upsample_filter_width / (2.0 * self.__conf.resample_freq)
    outer_min_lag = 1 / self.__conf.max_f0 - win
    outer_max_lag = 1 / self.__conf.min_f0 + win
    self.__nccf_first_lag = int(ceil(self.__conf.resample_freq * outer_min_lag))
    self.__nccf_last_lag = int(floor(self.__conf.resample_freq * outer_max_lag))
    self.__lags = self.__select_lags()
    self.__num_lags = self.__nccf_last_lag - self.__nccf_first_lag + 1

    upsample_cutoff = self.__conf.resample_freq * 0.5
    lags_offset = (self.__lags - self.__nccf_first_lag /
                   self.__conf.resample_freq)
    self.__nccf_resampler = ArbitraryResample(
        self.__num_lags, self.__conf.resample_freq, upsample_cutoff,
        lags_offset, self.__conf.upsample_filter_width)

    self.__frames_latency = 0
    self.__frame_info = [PitchFrameInfo(len(self.__lags))]
    self.__forward_cost = np.zeros(len(self.__lags))
    self.__nccf_info = list()

  def __select_lags(self):
    """选取NCCF lag, 范围为[1/max_f0, 1/min_f0].

    Returns:
      NCCF lag.
    """
    min_lag = 1 / self.__conf.max_f0
    max_lag = 1 / self.__conf.min_f0
    lag = min_lag
    lags = list()
    while lag <= max_lag:
      lags.append(lag)
      lag *= 1 + self.__conf.delta_pitch
    return np.array(lags)

  def __num_frames_available(self, num_sample):
    """获取可处理的帧数.

    Args:
      num_sample: 样本数.

    Returns:
      帧数.
    """
    frame_length = self.__conf.nccf_length
    if not self.__is_end:
      frame_length += self.__nccf_last_lag
    if num_sample < frame_length:
      return 0
    else:
      return int((num_sample - frame_length) / self.__conf.nccf_shift + 1)

  def __update_buffer(self, signal):
    """更新缓存.

    Args:
      signal: 信号.
    """
    num_frames = len(self.__frame_info) - 1
    next_frame = num_frames
    frame_shift = self.__conf.nccf_shift
    next_frame_sample = frame_shift * next_frame

    self.__signal_sum += np.sum(signal)
    self.__signal_sum_sq += np.dot(signal, signal)

    next_num_processed = self.__num_processed + len(signal)
    if next_frame_sample > next_num_processed:
      full_frame_length = self.__conf.nccf_length + self.__nccf_last_lag
      assert full_frame_length < frame_shift
    else:
      new_buffer = np.zeros(next_num_processed - next_frame_sample)
      for i in range(next_frame_sample, next_num_processed):
        if i >= self.__num_processed:
          new_buffer[i - next_frame_sample] = signal[i - self.__num_processed]
        else:
          buffer_index = i - self.__num_processed + len(self.__buffer)
          new_buffer[i - next_frame_sample] = self.__buffer[buffer_index]
      self.__buffer = new_buffer
    self.__num_processed = next_num_processed

  def __extract_window(self, signal, start_frame, length):
    """提取窗内的信号.

    Args:
      signal: 信号.
      start_frame: 起始帧索引.
      length: 窗长.

    Returns:
      窗信号.
    """
    offset = start_frame - self.__num_processed
    assert offset >= 0

    if offset + length > len(signal):
      raise NotImplementedError("sub extract")

    return signal[offset: offset + length]

  def __cal_correlation(self, window, length):
    """计算相关所需的系数.

    Args:
      window: 窗信号.
      length: 用于计算相关系数的长度.

    Returns:
      内积和范数内积.
    """
    mean_value = np.sum(window[:length]) / length
    zero_mean_wave = window - mean_value

    sub_array1 = zero_mean_wave[:length]
    e1 = np.dot(sub_array1, sub_array1)
    inner_prod = np.zeros(self.__num_lags)
    norm_prod = np.zeros(self.__num_lags)
    for lag in range(self.__nccf_first_lag, self.__nccf_last_lag + 1):
      sub_array2 = zero_mean_wave[lag: lag + length]
      e2 = np.dot(sub_array2, sub_array2)
      inner_prod[lag - self.__nccf_first_lag] = np.dot(sub_array1, sub_array2)
      norm_prod[lag - self.__nccf_first_lag] = e1 * e2
    return inner_prod, norm_prod

  def __cal_nccf(self, inner_prod, norm_prod, nccf_ballast):
    """计算nccf.

    Args:
      inner_prod: 内积.
      norm_prod: 范数内积.
      nccf_ballast: ballast.

    Returns:
      nccf.
    """
    nccf = np.zeros(self.__num_lags)
    for lag in range(self.__num_lags):
      numerator = inner_prod[lag]
      denominator = pow(norm_prod[lag] + nccf_ballast, 0.5)
      if denominator != 0:
        nccf[lag] = numerator / denominator
      else:
        assert numerator == 0
        nccf[lag] = 0
      assert -1.01 < nccf[lag] < 1.01
    return nccf

  def __accept_wave_form(self, signal):
    """接收音频数据.

    Args:
      signal: 信号.
    """
    signal = self.__resampler.resample(signal, self.__is_end)

    cur_sum = self.__signal_sum + sum(signal)
    cur_sum_sq = self.__signal_sum_sq + np.dot(signal, signal)
    cur_num_samp = self.__num_processed + len(signal)
    mean_square = cur_sum_sq / cur_num_samp - pow(cur_sum / cur_num_samp, 2.0)

    end_frame = self.__num_frames_available(cur_num_samp)
    start_frame = len(self.__frame_info) - 1
    num_new_frames = end_frame - start_frame

    if num_new_frames == 0:
      self.__update_buffer(signal)
      return

    num_resample_lags = len(self.__lags)
    basic_frame_length = self.__conf.nccf_length
    full_frame_length = basic_frame_length + self.__nccf_last_lag
    nccf_ballast = self.__conf.nccf_ballast
    nccf_ballast *= pow(mean_square * basic_frame_length, 2)

    nccf_pitch = np.zeros((num_new_frames, self.__num_lags))
    nccf_pov = np.zeros((num_new_frames, self.__num_lags))
    for frame in range(start_frame, end_frame):
      start_sample = frame * self.__conf.nccf_shift
      window = self.__extract_window(signal, start_sample, full_frame_length)
      inner_prod, norm_prod = self.__cal_correlation(window, basic_frame_length)

      index = frame - start_frame
      nccf_pitch[index] = self.__cal_nccf(inner_prod, norm_prod, nccf_ballast)
      nccf_pov[index] = self.__cal_nccf(inner_prod, norm_prod, 0)

      if frame < self.__conf.recompute_frame:
        self.__nccf_info.append(NccfInfo(np.average(norm_prod), mean_square))

    nccf_pitch = self.__nccf_resampler.resample(nccf_pitch)
    nccf_pov = self.__nccf_resampler.resample(nccf_pov)
    self.__update_buffer(signal)

    prev_frame_end_sample = 0
    cur_forward_cost = np.zeros(num_resample_lags)

    exit(0)

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
