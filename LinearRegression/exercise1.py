#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by TZ on 2020/2/12
import logging
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

from base.utils import load_txt
from LinearRegression.utils import compute_cost, gradient_descent


def __plot(feat, label):
  """绘图.

  Args:
    feat: 特征, 维度为(样本数, 1).
    label: 标签, 维度为(样本数).
  """
  plt.figure()
  plt.plot(feat, label, "rx", label="Training Data")
  plt.xlabel("Population of City in 10,000s")
  plt.ylabel("Profit in $10,000s")


def __cost_visualizing(best_theta, feat, label):
  """代价函数可视化.

  Args:
    best_theta: 最优参数, 维度为(特征数).
    feat: 特征, 维度为(样本数, 特征数).
    label: 维度为(样本数).
  """
  num = 100
  theta0_vals = np.linspace(-10, 10, num)
  theta1_vals = np.linspace(-1, 4, num)
  grid1 = np.outer(theta0_vals, np.ones(num))
  grid2 = np.outer(theta1_vals, np.ones(num)).T

  costs = np.zeros((num, num))
  for i in range(num):
    for j in range(num):
      theta = [grid1[i, j], grid2[i, j]]
      costs[i, j] = compute_cost(theta, feat, label)

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
  feat, label = load_txt(Path(__file__).parent / "data1.txt")
  num = len(feat)  # 样本数

  # 绘图显示数据.
  __plot(feat, label)

  # 梯度下降.
  lr = 0.01
  iteration = 1500
  init_theta = np.zeros(2)
  feat = np.concatenate([np.ones((num, 1)), feat], axis=-1)  # 增加全为1的第0列.
  best_theta, _ = gradient_descent(init_theta, feat, label, lr, iteration)
  logging.info(f"梯度下降得到的最优参数: [{best_theta[0]:.5f} "
               f"{best_theta[1]:.5f}]")

  plt.plot(feat[:, 1], np.dot(feat, best_theta), "-",
           label="Linear Regression")
  plt.legend()

  # 预测.
  pred = np.squeeze(np.dot(np.array([[1, 35000]]), best_theta))
  logging.info(f"人口为35000时, 预测得到的利润为: {pred:.2f}")

  # 代价函数可视化.
  __cost_visualizing(best_theta, feat, label)
  plt.show()


if __name__ == '__main__':
  logging.basicConfig(format="%(asctime)s %(name)s %(levelname)s %(message)s",
                      level=logging.INFO)
  __cmd()
