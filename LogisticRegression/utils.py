#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by TZ on 2020/2/16
import numpy as np


def sigmoid(input_vec):
  """sigmoid函数.

  Args:
    input_vec: 输入向量.

  Returns:
    输出向量.
  """
  return 1 / (1 + np.exp(-input_vec))
