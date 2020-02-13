#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by TZ on 2020/2/12
import logging
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d


def __plot(feature, label):
  """绘图.

  Args:
    feature: 特征, 维度为(样本数, 1).
    label: 标签, 维度为(样本数, 1).
  """
  plt.figure()
  plt.plot(feature, label, "rx", label="Training Data")
  plt.xlabel("Population of City in 10,000s")
  plt.ylabel("Profit in $10,000s")


def __compute_cost(feature, label, theta):
  """计算代价函数.

  Args:
    feature: 特征, 维度为(样本数, 特征数).
    label: 维度为(样本数, 1).
    theta: 参数, 维度为(特征数, 1).

  Returns:
    代价函数.
  """
  err = np.dot(feature, theta) - label
  return np.dot(err.T, err) / (2 * len(label))


def __gradient_descent(feature, label, theta, lr, iteration):
  """梯度下降.

  Args:
    feature: 特征, 维度为(样本数, 特征数).
    label: 维度为(样本数, 1).
    theta: 参数, 维度为(特征数, 1).
    lr: 学习率.
    iteration: 迭代次数.

  Returns:
    更新后的参数和每次迭代得到的代价函数构成的矩阵.
  """
  num_samples = len(label)
  num_feats = len(theta)
  costs = np.zeros(iteration)
  for i in range(iteration):
    err = np.dot(feature, theta) - label
    grad = np.sum(np.multiply(np.tile(err, num_feats), feature), axis=0)
    theta = (theta.T - lr / num_samples * grad).T
    costs[i] = __compute_cost(feature, label, theta)
  return theta, costs


def __cost_visualizing(feature, label, best_theta):
  """代价函数可视化.

  Args:
    feature: 特征, 维度为(样本数, 特征数).
    label: 维度为(样本数, 1).
    best_theta: 最优参数, 维度为(n, 1).
  """
  num = 100
  theta0_vals = np.linspace(-10, 10, num)
  theta1_vals = np.linspace(-1, 4, num)
  grid1 = np.outer(theta0_vals, np.ones(num))
  grid2 = np.outer(theta1_vals, np.ones(num)).T

  costs = np.zeros((num, num))
  for i in range(num):
    for j in range(num):
      theta = [[grid1[i, j]], [grid2[i, j]]]
      costs[i, j] = __compute_cost(feature, label, theta)

  plt.figure()
  ax = plt.axes(projection='3d')
  ax.plot_surface(grid1, grid2, costs, cmap="viridis")
  ax.set_xlabel(r"$\theta_0$")
  ax.set_ylabel(r"$\theta_1$")
  ax.set_zlabel("cost")

  plt.figure()
  ax = plt.axes()
  log_costs = np.log10(costs)
  space = np.logspace((log_costs.min()), (log_costs.max()), 15)
  ax.contour(grid1, grid2, costs, space)
  plt.plot(best_theta[0], best_theta[1], "rx")
  ax.set_xlabel(r"$\theta_0$")
  ax.set_ylabel(r"$\theta_1$")


def __cmd():
  """命令行函数.

  """
  data = np.loadtxt(Path(__file__).parent / "data1.txt",  delimiter=",")
  feature = np.expand_dims(data[:, 0], 1)
  label = np.expand_dims(data[:, 1], 1)
  num = len(feature)  # 样本数

  # 绘图显示数据.
  __plot(feature, label)

  # 梯度下降.
  lr = 0.01
  iteration = 1500
  init_theta = np.zeros((2, 1))
  feature = np.concatenate([np.ones((num, 1)), feature], axis=-1)  # 增加x0列.
  best_theta, _ = __gradient_descent(feature, label, init_theta, lr, iteration)
  logging.info(f"梯度下降得到的参数为: [{best_theta[0, 0]:.5f} "
               f"{best_theta[1, 0]:.5f}]")

  plt.plot(feature[:, 1], np.dot(feature, best_theta), "-",
           label="Linear Regression")
  plt.legend()

  # 预测.
  pred = np.squeeze(np.dot(np.array([[1, 35000]]), best_theta))
  logging.info(f"人口为35000时, 预测得到的利润为: {pred:.2f}")

  # 代价函数可视化.
  __cost_visualizing(feature, label, best_theta)
  plt.show()


if __name__ == '__main__':
  logging.basicConfig(format="%(asctime)s %(name)s %(levelname)s %(message)s",
                      level=logging.INFO)
  __cmd()
