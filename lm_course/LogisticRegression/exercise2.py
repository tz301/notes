#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by tz301 on 2020/2/16
import logging
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize

from base.utils import load_txt, LOGGER_FORMAT
from lm_course.LogisticRegression.utils import sigmoid


def __plot(feat, label):
  """作图.

  Args:
    feat: 特征, 维度(样本数, 特征维度).
    label: 标签, 0或者1, 维度(样本数).
  """
  pos = np.where(label == 1)[0]
  neg = np.where(label == 0)[0]

  plt.figure()
  plt.plot(feat[pos, 0], feat[pos, 1], "k+", label="y = 1")
  plt.scatter(feat[neg, 0], feat[neg, 1], facecolors="y", edgecolors="k",
              label="y = 0")
  plt.xlabel("Microchip Test 1")
  plt.ylabel("Microchip Test 2")
  plt.legend()


def __feat_mapping(feat):
  """特征映射, 增加特征维度.

  Args:
    feat: 特征, 维度(样本数, 特征数), 此处特征数为2.

  Returns:
    特征映射后的特征, 维度(样本数, 特征数), 此处特征数为28.
  """
  feat1 = feat[:, 0]
  feat2 = feat[:, 1]

  degree = 6
  new_feat = np.ones((len(feat), 1))
  for i in range(1, degree + 1):
    for j in range(i + 1):
      new_col = np.expand_dims(np.multiply(feat1 ** (i - j), feat2 ** j), 1)
      new_feat = np.append(new_feat, new_col, 1)
  return new_feat


def __compute_cost(theta, feat, label, lambda_factor):
  """计算代价函数.

  Args:
    theta: 参数, 维度(特征数).
    feat: 特征, 维度(样本数, 特征数).
    label: 标签, 维度(样本数).
    lambda_factor: 正则化因子.

  Returns:
    代价函数数值.
  """
  num = len(feat)
  hypothesis = sigmoid(np.dot(feat, theta))
  cost = np.sum(-np.multiply(label, np.log(hypothesis)) -
                np.multiply(1 - label, np.log(1 - hypothesis))) / num
  penalty = lambda_factor / (2 * num) * np.sum(theta[1:])
  return cost + penalty


def __compute_grad(theta, feat, label, lambda_factor):
  """计算梯度.

  Args:
    theta: 参数, 维度(特征数).
    feat: 特征, 维度(样本数, 特征数).
    label: 标签, 维度(样本数).
    lambda_factor: 正则化因子.

  Returns:
    梯度数值.
  """
  num = len(feat)
  hypothesis = sigmoid(np.dot(feat, theta))
  grad = np.sum(np.multiply(np.tile(hypothesis - label, (feat.shape[1], 1)).T,
                            feat), axis=0) / num
  penalty = np.zeros(len(theta))
  penalty[1:] = lambda_factor / num * theta[1:]
  return grad + penalty


def __predict(theta, feat):
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


def __cmd():
  """命令行函数.

  """
  feat, label = load_txt(Path(__file__).parent / "data2.txt")
  num = len(feat)  # 样本数

  # 样本作图.
  __plot(feat, label)

  # 梯度下降.
  new_feat = __feat_mapping(feat)
  init_theta = np.zeros(new_feat.shape[1])
  grid_num = 50
  grid_x = np.linspace(-1, 1.5, grid_num)
  grid_y = np.linspace(-1, 1.5, grid_num)
  for lambda_factor in [0, 0.01, 1, 100]:
    args = (new_feat, label, lambda_factor)
    optimal = minimize(__compute_cost, init_theta, args=args,
                       method="TNC", jac=__compute_grad)
    best_theta = optimal["x"]

    acc = np.sum(__predict(best_theta, new_feat) == label) / num
    logging.info(f"正则化因子为{lambda_factor}时, 训练集准确率为: {acc * 100:.2f}%.")

    value_z = np.zeros((grid_num, grid_num))
    for i in range(grid_num):
      for j in range(grid_num):
        feat_tmp = np.array([[grid_x[i], grid_y[j]]])
        value_z[i, j] = np.dot(__feat_mapping(feat_tmp), best_theta)

    __plot(feat, label)
    plt.title(r"$\lambda=$" + f"{lambda_factor}")
    plt.contour(grid_x, grid_y, value_z, [0])

  plt.show()


if __name__ == '__main__':
  logging.basicConfig(format=LOGGER_FORMAT, level=logging.INFO)
  __cmd()
