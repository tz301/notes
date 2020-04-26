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

* $ Q $为$ N $个节点的集合.
* $ A $为转移概率矩阵, $ a_{ij} $表示节点$ i $到节点$ j $的转移概率,
且满足$ \sum_{j=1}^N a_{ij} = 1, \forall i $.
* $ \pi_i $为节点$ i $的初始概率分布, 满足$ \sum_{i=1}^N \pi_i = 1 $,
$ \pi_i = 0 $表示不可能为初始状态节点.

例如上图a中, 假设初始概率分布为$ \pi(hot, cold, warm) = [0.1, 0.7, 0.2] $,
那么:

$$ P(cold, hot, cold, hot) = 0.7 * 0.1 * 0.1 * 0.1 = 0.0007 $$

## Hidden Markov Models

很多情况下, 我们关心的状态是隐藏起来的.
例如, 我们通过文本无法直接观测到词性标注(POS), 我们只可以观测到词.
POS只能通过词序列来推测, 因此是被隐藏起来的.

HMM是一个同时包含了观测状态和隐藏状态的概率模型, 由五个部分组成:

$$
\begin{aligned}
& Q = q_1 q_2 \cdots q_N \\
& A = a_{11} \cdots a_{ij} \cdots a_{NN} \\
& O = o_1 o_2 \cdots o_T \\
& B = b_i(o_t) \\
& \pi = \pi_1, \pi_2 \cdots, \pi_N
\end{aligned}
$$

* $ Q $为$ N $个节点的集合.
* $ A $为转移概率矩阵, $ a_{ij} $表示节点$ i $到节点$ j $的转移概率,
且满足$ \sum_{j=1}^N a_{ij} = 1, \forall i $.
* $ O $为观测序列, 每个观测值来源于词典$ V = v_1, v_2, \cdots, v_V $.
* $ B $为发射概率, 表示节点$ i $产生观测$ o_t $的概率.
* $ \pi_i $为节点$ i $的初始概率分布, 满足$ \sum_{i=1}^N \pi_i = 1 $,
$ \pi_i = 0 $表示不可能为初始状态节点.

一阶马尔可夫模型遵循两个假设:

1. 某个状态节点的概率仅与前一个状态节点有关:

$$ P(q_i = a|q_1 \cdots q_{i-1}) = P(q_i = a|q_{i-1}) $$

2. 观测值$ o_i $仅与产生该观测值的节点$ q_i $有关, 与其他状态节点或者观测值无关,
即输出独立性:

$$ P(o_i|q_1 \cdots q_i \cdots q_t, o_1 \cdots o_i \cdots o_t) =
 P(o_i|q_i}) $$

下面用一个例子简述HMM模型. 假设有两种天气COLD(C)和HOT(H), 但是没有天气的信息,
只有每天吃掉的冰淇淋数量. 那么问题变成: 已知观测序列$ O $(每天吃掉的冰淇淋数量),
寻找天气(C或者H)对应的隐序列$ Q $, 如下图.
观测序列$ O = \{1, 2, 3\} $对应每天吃掉的冰淇淋数量.

<div align=center><img width="450" src="figure/2.png" alt=" "/></div>

HMM的三个问题:

1. Likelihood: 已知HMM模型 $ \lambda = (A, B) $, 给定观测序列$ O $,
计算似然$ P(O|\lambda) $.
2. Decoding: 已知HMM模型 $ \lambda = (A, B) $, 给定观测序列$ O $,
获取最可能的隐状态序列$ Q $.
3. Learning: 给定观测序列$ O $和一系列状态, 学习HMM的参数$ A $和$ B $.

## Likelihood - The Forward Algorithm


## Decoding - The Viterbi Algorithm


## HMM Training - The Forward-Backward Algorithm
