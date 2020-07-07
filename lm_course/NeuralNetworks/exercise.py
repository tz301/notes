#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by tz301 on 2020/3/29
import logging
import math

import matplotlib.pyplot as plt
import numpy as np
from scipy.io import loadmat
from base.utils import LOGGER_FORMAT


def __plot(inputs):
  """绘图. 随机选取100个数字,

  Args:
    inputs: 输入图像, 维度(num_samples, input_layer_size)
  """
  rows = 10
  cols = 10
  indexes = np.random.choice(inputs.shape[0], rows * cols, replace=False)
  samples = inputs[indexes, :]
  num_samples, input_layer_size = samples.shape
  height = width = int(math.sqrt(input_layer_size))

  image_index = 0
  pad = 1
  display_array = np.ones((pad + rows * (height + pad),
                           pad + cols * (width + pad)))
  for i in range(rows):
    for j in range(cols):
      cur_sample = np.reshape(samples[image_index, :], (width, height)).T
      row_start = pad + i * (width + pad)
      row_end = row_start + width
      col_start = pad + j * (height + pad)
      col_end = col_start + height
      display_array[row_start: row_end, col_start: col_end] = cur_sample
      image_index += 1

  plt.imshow(display_array)
  plt.show()


def __cmd():
  """命令行函数.

  """
  data = loadmat("data.mat")
  inputs = data["X"]
  labels = data["y"]
  __plot(inputs)

  num_samples, input_layer_size = inputs.shape
  num_labels = 10


if __name__ == '__main__':
  logging.basicConfig(format=LOGGER_FORMAT, level=logging.INFO)
  __cmd()
