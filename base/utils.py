#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by TZ on 2020/2/15
import numpy as np


def load_txt(file_path):
  """从txt文件中读取特征和标签.

  文件每一行为一个样本, 每行以","为分隔符, 最后一列为标签, 其余列为特征.

  Args:
    file_path: txt文件路径.

  Returns:
    特征和标签, 特征维度(样本数, 特征数), 标签维度(样本数).
  """
  data = np.loadtxt(file_path, delimiter=",")
  feat = data[:, :-1]
  label = data[:, -1]
  if len(feat.shape) == 1:
    feat = np.expand_dims(feat, 1)
  return feat, label
