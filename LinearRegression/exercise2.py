#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by TZ on 2020/2/12
import logging
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from LinearRegression.utils import gradient_descent


def __normalize_feature(feature):
  """对特征进行归一化.

  Args:
    feature: 特征, 维度(样本数, 特征维度).

  Returns:
    归一化后的特征, 维度(样本数, 特征维度).
  """
  mu = np.mean(feature, axis=0)
  sigma = np.std(feature, axis=0)
  return (feature - mu) / np.tile(sigma, (len(feature), 1)), mu, sigma


def __gradient_descent_multi_lr(feature, label, init_theta, lr_list, iteration):
  """多个学习率分别进行梯度下降, 汇出曲线, 选择一组合适的参数.

  Args:
    feature: 特征, 维度为(样本数, 特征数).
    label: 维度为(样本数).
    init_theta: 初始参数, 维度为(特征数).
    lr_list: 学习率列表.
    iteration: 迭代次数.

  Returns:
    更新后的参数.
  """
  res = list()
  for lr in lr_list:
    theta, costs = gradient_descent(feature, label, init_theta, lr, iteration)
    res.append((lr, theta, costs))

  plt.figure()
  iterations = range(iteration)
  colors = ["b", "k", "g", "r", "m", "c"]
  for (lr, _, costs), color in zip(res, colors):
    plt.plot(iterations, costs, color, label=f"lr={lr}")
  plt.xlabel("iteration")
  plt.ylabel("cost")
  plt.legend()
  plt.show()

  return res[2][1]


def __cmd():
  """命令行函数.

  """
  data = np.loadtxt(Path(__file__).parent / "data2.txt",  delimiter=",")
  feature = data[:, :-1]
  label = data[:, -1]
  num = len(label)  # 样本数

  feature_norm, mu, sigma = __normalize_feature(feature)
  # 增加全为1的第0列.
  feature_norm = np.concatenate([np.ones((num, 1)), feature_norm], axis=-1)

  # 梯度下降, 不同学习率.
  lr_list = [0.3, 0.1, 0.03, 0.01, 0.003, 0.001]
  iteration = 400
  init_theta = np.zeros(3)
  best_theta = __gradient_descent_multi_lr(feature_norm, label, init_theta,
                                           lr_list, iteration)
  logging.info(f"梯度下降得到的最优参数: [{best_theta[0]:.5f} "
               f"{best_theta[1]:.5f} {best_theta[2]:.5f}]")

  # 梯度下降预测
  feat1 = np.array([1650, 3])
  pred1 = np.squeeze(np.dot(np.insert((feat1 - mu) / sigma, 0, 1), best_theta))
  logging.info(f"房屋尺寸为1650, 卧室数量为3时, 梯度下降预测得到的房价: {pred1:.2f}")

  # Normal Equation
  feature = np.concatenate([np.ones((num, 1)), feature], axis=-1)
  inv_item = np.linalg.pinv(np.dot(feature.T, feature))
  theta_equation = np.dot(np.dot(inv_item, feature.T), label)
  logging.info(f"Normal Equation得到的最优参数: [{theta_equation[0]:.5f} "
               f"{theta_equation[1]:.5f} {theta_equation[2]:.5f}]")

  feat2 = np.array([1, 1650, 3])
  pred2 = np.squeeze(np.dot(feat2, theta_equation))
  logging.info(f"房屋尺寸为1650, 卧室数量为3时, Normal Equation预测得到的房价: {pred2:.2f}")


if __name__ == '__main__':
  logging.basicConfig(format="%(asctime)s %(name)s %(levelname)s %(message)s",
                      level=logging.INFO)
  __cmd()
