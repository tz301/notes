#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by tz301 on 2020/7/9
"""MFCC特征."""
import logging

import numpy as np
from scipy.fftpack import dct
from scipy.io import wavfile

from asr_feature.fbank import fbank
from base.utils import LOGGER_FORMAT


def __lifter(cepstrum, order=22):
  """倒谱加权.

  Args:
    cepstrum: 倒谱.
    order: 阶数, 默认22.

  Returns:
    加权后的倒谱.
  """
  if order > 0:
    _, num_coeff = np.shape(cepstrum)
    coeff = np.arange(num_coeff)
    lift = 1 + (order / 2.0) * np.sin(np.pi * coeff / order)
    return lift * cepstrum
  else:
    return cepstrum


def mfcc(signal, sample_rate, num_cep=13):
  """获取mfcc特征.

  Args:
    signal: 信号.
    sample_rate: 采样频率.
    num_cep: mfcc阶数, 默认13.

  Returns:
    fbank特征, 维度(帧数, 滤波器数量).
  """
  fbank_feature = fbank(signal, sample_rate)
  fbank_log_feature = np.log(fbank_feature)
  mfcc_feature = dct(fbank_log_feature, axis=1, norm='ortho')[:, :num_cep]
  mfcc_feature = __lifter(mfcc_feature)
  return mfcc_feature


def __cmd():
  """命令行函数."""
  sample_rate, signal = wavfile.read('asr_feature/test.wav')
  feature = mfcc(signal, sample_rate)
  logging.info(f'mfcc特征维度: {feature.shape}.')
  assert feature.shape == (419, 13), 'mfcc特征维度错误.'
  assert abs(feature[0][0] - 10.70478) < 1e-5, 'fbank特征错误.'


if __name__ == '__main__':
  logging.basicConfig(format=LOGGER_FORMAT, level=logging.INFO)
  __cmd()
