#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by tz301 on 2020/4/26
import logging

import numpy as np

from base.utils import LOGGER_FORMAT


class HMM:
  """HMM类.

  Attributes:
    states: 所有可能的隐状态.
    init_prob: 初始概率, {stage: prob}.
    transition_prob: 转移概率, {(state_i, state_j): prob}表示状态i -> 状态j的转移概率.
    emission_prob: 发射概率, {(state_i, o_t): prob}表示状态i -> 观测j的发射概率.
    vocabularies: 所有可能的观测值.
  """

  def __init__(self):
    """初始化."""
    self.states = list()
    self.vocabularies = set()
    self.init_prob = dict()
    self.transition_prob = dict()
    self.emission_prob = dict()

  def compute_likelihood(self, observations):
    """采用前向算法计算某个观测序列的似然.

    Args:
      observations: 观测值序列.

    Returns:
      某个观测序列的似然.
    """
    alpha = np.zeros((len(observations), len(self.states)))

    # 初始化.
    init_observation = observations[0]
    for j, state in enumerate(self.states):
      emission_prob = self.emission_prob[(state, init_observation)]
      alpha[0, j] = self.init_prob[state] * emission_prob

    # 递归.
    for t, observation in enumerate(observations[1:], 1):
      for j, cur_state in enumerate(self.states):
        cur_alpha = 0
        for i, last_state in enumerate(self.states):
          transition_prob = self.transition_prob[(last_state, cur_state)]
          emission_prob = self.emission_prob[(cur_state, observation)]
          cur_alpha += alpha[t - 1, i] * transition_prob * emission_prob
        alpha[t, j] = cur_alpha

    return np.sum(alpha[-1, :])

  def decode(self, observations):
    """采用Viterbi算法进行解码.

    Args:
      observations: 观测值序列.

    Returns:
      最后路径以及对应的概率.
    """
    num_states = len(self.states)
    num_observations = len(observations)
    viterbi_prob = np.zeros((num_observations, num_states))
    back_trace = np.zeros(viterbi_prob.shape, dtype=np.int)

    # 初始化.
    init_observation = observations[0]
    for j, state in enumerate(self.states):
      emission_prob = self.emission_prob[(state, init_observation)]
      viterbi_prob[0, j] = self.init_prob[state] * emission_prob

    # 递归.
    tmp_prob = np.zeros(num_states)  # 计算每个网格节点时, 临时保存每条路径的概率.
    for t, observation in enumerate(observations[1:], 1):
      for j, cur_state in enumerate(self.states):
        for i, last_state in enumerate(self.states):
          transition_prob = self.transition_prob[(last_state, cur_state)]
          emission_prob = self.emission_prob[(cur_state, observation)]
          tmp_prob[i] = viterbi_prob[t - 1, i] * transition_prob * emission_prob
        viterbi_prob[t, j] = np.max(tmp_prob)
        back_trace[t, j] = np.argmax(tmp_prob)

    # 终止
    final_prob = np.max(viterbi_prob[-1])

    best_state_ids = np.zeros(num_observations, dtype=np.int)
    best_state_ids[-1] = np.argmax(viterbi_prob[-1])
    cur_state = best_state_ids[-1]
    for i in range(num_observations - 1):
      cur_state = back_trace[num_observations - 1 - i, cur_state]
      best_state_ids[num_observations - 2 - i] = cur_state

    best_path = [self.states[state_id] for state_id in best_state_ids]
    return best_path, final_prob


def __cmd():
  """命令行函数."""
  hmm = HMM()
  hmm.states = ["hot", "cold"]
  hmm.vocabularies = {1, 2, 3}
  hmm.init_prob = {"hot": 0.8, "cold": 0.2}
  hmm.transition_prob = {("hot", "hot"): 0.6, ("hot", "cold"): 0.4,
                         ("cold", "hot"): 0.5, ("cold", "cold"): 0.5}
  hmm.emission_prob = {("hot", 1): 0.2, ("hot", 2): 0.4, ("hot", 3): 0.4,
                       ("cold", 1): 0.5, ("cold", 2): 0.4, ("cold", 3): 0.1}

  likelihood = hmm.compute_likelihood([3, 1, 3])
  logging.info(f"似然: {likelihood:.5f}")

  best_path, best_path_prob = hmm.decode([3, 1, 3])
  logging.info(f"概率最大的隐序列: {best_path}, 对应的概率为{best_path_prob:.5f}.")


if __name__ == '__main__':
  logging.basicConfig(format=LOGGER_FORMAT, level=logging.INFO)
  __cmd()
