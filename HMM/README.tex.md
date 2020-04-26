# [目录](../README.md)

# Hidden Markov Models

## Markov Chains

马尔科夫链, 是状态空间中从一个状态到另一个状态转换的随机过程.
对于马尔科夫链, 如果要从一个序列进行预测, 当前状态起到决定的作用,
历史状态对于预测没有影响.

假设一个序列内的状态变量为$ q_1, q_2, \cdots, q_i $. 可以将马尔可夫假设表示为:

$$ P(q_i = a|q_1 \cdots q_{i-1}) = P(q_i = a|q_{i-1}) $$

下图a给出了天气变化的马尔科夫链, 可能的天气为HOT, COLD和WARM.
图中, 状态以节点表示, 每条边上标明转移概率, 每个节点所有边的转移概率之和为1.
图b给出了一个二元语言模型的马尔科夫链.

<div align=center><img width="450" src="figure/1.png" alt=" "/></div>

综上, 马尔科夫链主要由三个部分组成:

$$
\begin{aligned}
& Q = q_1 q_2 \cdots q_N \\
& A = a_{11} a_{12} \cdots a_{1N} \cdots a_{NN} \\
& \pi = \pi_1, \pi_2 \cdots, \pi_N
\end{aligned}
$$

$ Q $为$ N $个节点的集合.

$ A $为转移概率矩阵, $ a_{ij} $表示节点i到节点j的转移概率,
且满足$ \sum_{j=1}^N a_{ij} = 1, \forall i $.

$ \pi_i $为节点$ i $的初始概率分布, 满足$ \sum_{i=1}^N \pi_i = 1 $,
$ \pi_i = 0 $表示不可能为初始状态节点.

例如上图a中, 假设初始概率分布为$ \pi(hot, cold, warm) = [0.1, 0.7, 0.2] $,
那么:

$$ P(cold, hot, cold, hot) = 0.7 * 0.1 * 0.1 * 0.1 = 0.0007 $$

## Hidden Markov Models

很多情况下, 我们关心的状态是隐藏起来的.
例如, 我们通过文本无法直接观测到词性标注(POS), 我们只可以观测到词.
POS只能通过词序列来推测, 因此是被隐藏起来的.

HMM是一个同时包含了观测状态和隐藏状态的概率模型, 由五个部分组成:
