#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by tz301 on 2020/2/16
"""共用模块."""
import numpy as np


def sigmoid(input_vec):
  """sigmoid函数.

  Args:
    input_vec: 输入向量.

  Returns:
    输出向量.
  """
  return 1 / (1 + np.exp(-input_vec))


def predict(theta, feat):
  """预测结果.

  Args:
    theta: 参数, 维度(特征数).
    feat: 特征, 维度(特征数)或者(样本数, 特征数).

  Returns:
    标签, 0或者1, 维度(样本数).
  """
  if len(feat.shape) == 1:
    feat = np.expand_dims(feat, 1)
  return (np.dot(feat, theta) >= 0.5).astype(np.int)
