#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by TZ on 2020/2/15
import logging
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize

from base.utils import load_txt
from LogisticRegression.utils import sigmoid


def __plot(feat, label):
  """作图.

  Args:
    feat: 特征, 维度(样本数, 特征维度).
    label: 标签, 0或者1, 维度(样本数).

  Returns:
    ax.
  """
  pos = np.where(label == 1)[0]
  neg = np.where(label == 0)[0]

  fig = plt.figure()
  ax = fig.subplots()
  ax.plot(feat[pos, 0], feat[pos, 1], "k+", label="Admitted")
  ax.scatter(feat[neg, 0], feat[neg, 1], facecolors="y", edgecolors="k",
             label="Not Admitted")
  plt.xlabel("Exam 1 score")
  plt.ylabel("Exam 2 score")
  return ax


def __compute_cost(theta, feat, label):
  """计算代价函数.

  Args:
    theta: 参数, 维度(特征数).
    feat: 特征, 维度(样本数, 特征数).
    label: 标签, 维度(样本数).

  Returns:
    代价函数数值.
  """
  hypothesis = sigmoid(np.dot(feat, theta))
  cost = np.sum(-np.multiply(label, np.log(hypothesis)) -
                np.multiply(1 - label, np.log(1 - hypothesis))) / len(feat)
  return cost


def __compute_grad(theta, feat, label):
  """计算梯度.

  Args:
    theta: 参数, 维度(特征数).
    feat: 特征, 维度(样本数, 特征数).
    label: 标签, 维度(样本数).

  Returns:
    梯度数值.
  """
  hypothesis = sigmoid(np.dot(feat, theta))
  grad = np.sum(np.multiply(np.tile(hypothesis - label, (feat.shape[1], 1)).T,
                            feat), axis=0) / len(feat)
  return grad


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
  feat, label = load_txt(Path(__file__).parent / "data1.txt")
  num = len(feat)  # 样本数

  # 样本作图.
  ax = __plot(feat, label)

  # 梯度下降.
  init_theta = np.zeros(3)
  feat = np.concatenate([np.ones((num, 1)), feat], axis=-1)  # 增加全为1的第0列.
  optimal = minimize(__compute_cost, init_theta, args=(feat, label),
                     method="TNC", jac=__compute_grad)
  best_theta = optimal["x"]
  logging.info(f"梯度下降得到的最优参数: [{best_theta[0]:.5f} "
               f"{best_theta[1]:.5f} {best_theta[2]:.5f}]")

  # 绘出决策边界, sigmoid(theta * feature) = 0.5的直线, 即theta * feature = 0的直线.
  boundary_x = np.array([min(feat[:, 1]) - 2, max(feat[:, 2]) + 2])
  boundary_y = -1 / best_theta[2] * (boundary_x * best_theta[1] + best_theta[0])
  ax.plot(boundary_x, boundary_y, label="Decision Boundary")
  handles, labels = ax.get_legend_handles_labels()
  handles = [handles[0], handles[2], handles[1]]
  labels = [labels[0], labels[2], labels[1]]
  ax.legend(handles, labels)
  plt.show()

  # 预测.
  prob = sigmoid(np.dot(np.array([[1, 45, 85]]), best_theta))[0]
  logging.info(f"科目1分数为45, 科目2分数为85时, 入学概率为: {prob:.3f}.")

  # 训练集准确率.
  predict = __predict(best_theta, feat)
  acc = np.sum(predict == label) / num
  logging.info(f"训练集准确率为: {acc * 100:.0f}%.")


if __name__ == '__main__':
  logging.basicConfig(format="%(asctime)s %(name)s %(levelname)s %(message)s",
                      level=logging.INFO)
  __cmd()
