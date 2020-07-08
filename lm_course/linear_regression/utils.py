#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by TZ on 2020/2/12
import numpy as np


def compute_cost(theta, feat, label):
  """计算代价函数.

  Args:
    theta: 参数, 维度为(特征数).
    feat: 特征, 维度为(样本数, 特征数).
    label: 维度为(样本数).

  Returns:
    代价函数.
  """
  err = np.dot(feat, theta) - label
  return np.sum(err ** 2) / (2 * len(label))


def gradient_descent(theta, feat, label, lr, iteration):
  """梯度下降.

  Args:
    theta: 参数, 维度为(特征数).
    feat: 特征, 维度为(样本数, 特征数).
    label: 维度为(样本数).
    lr: 学习率.
    iteration: 迭代次数.

  Returns:
    更新后的参数和每次迭代得到的代价函数构成的矩阵.
  """
  num_samples = len(label)
  num_feats = len(theta)
  costs = np.zeros(iteration)
  for i in range(iteration):
    err = np.dot(feat, theta) - label
    grad = np.sum(np.multiply(np.tile(err, (num_feats, 1)).T, feat), axis=0)
    theta = theta - lr / num_samples * grad
    costs[i] = compute_cost(theta, feat, label)
  return theta, costs
