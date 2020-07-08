#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by tz301 on 2020/7/7
import logging
from decimal import Decimal, ROUND_HALF_UP
from math import ceil, pi

import numpy as np
from scipy.io import wavfile

from base.utils import LOGGER_FORMAT


def __pre_emphasis(signal, alpha=0.97):
  """预加重.

  Args:
    signal: 输入信号.
    alpha: 预加重系数, 默认0.97.

  Returns:
    输出信号.
  """
  return np.append(signal[0], signal[1:] - alpha * signal[:-1])


def __round_half_up(number):
  """按照小数点后第一位取整, 不小于5的向上取整, 1.4 -> 1, 1.5 -> 2.

  Args:
    number: 数字.

  Returns:
    向上取整后的数字.
  """
  return int(Decimal(number).quantize(Decimal('1'), rounding=ROUND_HALF_UP))


def __framing(signal, sample_rate, win_len=0.025, win_step=0.01):
  """分帧.

  Args:
    signal: 输入信号.
    sample_rate: 采样频率.
    win_len: 帧长, 默认25ms.
    win_step: 帧移, 默认10ms.

  Returns:
    所有帧, 维度(帧数, 帧长).
  """
  frame_len = __round_half_up(win_len * sample_rate)
  frame_step = __round_half_up(win_step * sample_rate)

  length = len(signal)
  no_frame = length < frame_len
  num_frames = 1 if no_frame else 1 + ceil((length - frame_len) / frame_step)

  # 右侧进行padding.
  pad_len = (num_frames - 1) * frame_step + frame_len
  signal = np.concatenate((signal, np.zeros((pad_len - length))))

  frame_indices = np.tile(np.arange(0, frame_len), (num_frames, 1))
  step_indices = np.arange(0, num_frames * frame_step, frame_step)
  indices = frame_indices + np.tile(step_indices, (frame_len, 1)).T
  return signal[indices]


def __hamming_window(length):
  """Hamming窗函数.

  Args:
    length: 窗长.

  Returns:
    Hamming窗.
  """
  return 0.54 - 0.46 * np.cos(2.0 * pi * np.arange(0, length) / (length - 1))


def __window(frames, win='hamming'):
  """加窗.

  Args:
    frames: 所有帧, 维度(帧数, 帧长).
    win: 窗函数, 默认hamming窗.

  Returns:
    加窗后的所有帧, 维度(帧数, 帧长).
  """
  if not win:
    return frames

  num_frames, frame_len = frames.shape
  if win == 'hamming':
    window = np.tile(__hamming_window(frame_len), (num_frames, 1))
    return window * frames
  else:
    raise NotImplementedError(f'不支持的窗函数: {win}.')


def __power_spectral(frames, n_fft=512):
  """计算功率谱.

  Args:
    frames: 所有帧, 维度(帧数, 帧长).
    n_fft: fft点数, 默认512.

  Returns:
    功率谱, 维度(帧数, n_fft / 2 + 1).
  """
  magnitude_spectral = np.absolute(np.fft.rfft(frames, n_fft))
  return 1 / n_fft * np.square(magnitude_spectral)


def __freq2mel(freq):
  """频率转为梅尔频率.

  Args:
    freq: 频率.

  Returns:
    梅尔频率.
  """
  return 2595 * np.log10(1 + freq / 700)


def __mel2freq(mel):
  """梅尔频率转为频率.

  Args:
    mel: 梅尔频率.

  Returns:
    频率.
  """
  return 700 * (10 ** (mel / 2595) - 1)


def __mel_filter_banks(sample_rate, n_filter=26, n_fft=512, low_freq=200,
                       high_freq=7800):
  """获取梅尔滤波器组.

  Args:
    sample_rate: 采样频率.
    n_filter: 滤波器数量, 默认26.
    n_fft: fft点数, 默认512.
    low_freq: 低频截止频率, 默认200Hz.
    high_freq: 高频截止频率, 默认7800Hz.

  Returns:
    梅尔滤波器组, 维度(滤波器数量, n_fft / 2 + 1).
  """
  half_freq = sample_rate / 2
  high_freq = high_freq or half_freq
  if high_freq > half_freq:
    raise ValueError(f'高频截止频率不能超过1/2采样频率: {high_freq} > {half_freq}.')

  low_mel = __freq2mel(low_freq)
  high_mel = __freq2mel(high_freq)
  mel_points = np.linspace(low_mel, high_mel, n_filter + 2)
  freq_points = __mel2freq(mel_points)
  bins = np.floor((n_fft + 1) * freq_points / sample_rate).astype(np.int)

  filter_banks = np.zeros([n_filter, n_fft // 2 + 1])
  for i in range(0, n_filter):
    for j in range(bins[i], bins[i + 1]):
      filter_banks[i, j] = (j - bins[i]) / (bins[i + 1] - bins[i])
    for j in range(bins[i + 1], bins[i + 2]):
      filter_banks[i, j] = (bins[i + 2] - j) / (bins[i + 2] - bins[i + 1])
  return filter_banks


def fbank(signal, sample_rate):
  """获取fbank特征.

  Args:
    signal: 信号.
    sample_rate: 采样频率.

  Returns:
    fbank特征, 维度(帧数, 滤波器数量).
  """
  signal = __pre_emphasis(signal)
  frames = __framing(signal, sample_rate)
  frames = __window(frames)
  power_spectral = __power_spectral(frames)
  filter_banks = __mel_filter_banks(sample_rate)
  feature = np.dot(power_spectral, filter_banks.T)
  return feature


def __cmd():
  """命令行函数."""
  sample_rate, signal = wavfile.read('asr_feature/test.wav')
  feature = fbank(signal, sample_rate)
  logging.info(f'fbank特征维度: {feature.shape}.')
  assert feature.shape == (419, 26), 'fbank特征维度错误.'
  assert abs(feature[0][0] - 1.87086) < 1e-5, 'fbank特征错误.'


if __name__ == '__main__':
  logging.basicConfig(format=LOGGER_FORMAT, level=logging.INFO)
  __cmd()
