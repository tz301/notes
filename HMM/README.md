# [目录](../README.md)

# Hidden Markov Models

## Markov Chains

马尔科夫链, 是状态空间中从一个状态到另一个状态转换的随机过程.
对于马尔科夫链, 如果要从一个序列进行预测, 当前状态起到决定的作用,
历史状态对于预测没有影响.

假设一个序列内的状态变量为<img src="/HMM/tex/e637b86bbdb2aacea366b27626449b0a.svg?invert_in_darkmode&sanitize=true" align=middle width=87.98971334999999pt height=14.611911599999981pt/>. 可以将马尔可夫假设表示为:

<p align="center"><img src="/HMM/tex/ceee94c7c67f44415a5d264fd97b7173.svg?invert_in_darkmode&sanitize=true" align=middle width=267.77565375pt height=16.438356pt/></p>

下图a给出了天气变化的马尔科夫链, 可能的天气为HOT, COLD和WARM.
图中, 状态以节点表示, 每条边上标明转移概率, 每个节点所有边的转移概率之和为1.
图b给出了一个二元语言模型的马尔科夫链.

<div align=center><img width="450" src="figure/1.png" alt=" "/></div>

综上, 马尔科夫链主要由三个部分组成:

<p align="center"><img src="/HMM/tex/bb93915952237707c08a9f722b98b3c5.svg?invert_in_darkmode&sanitize=true" align=middle width=188.4845622pt height=63.744281699999995pt/></p>

<img src="/HMM/tex/bb17b0e6d694fc6d731ee88afe1bae60.svg?invert_in_darkmode&sanitize=true" align=middle width=12.99542474999999pt height=22.465723500000017pt/>为<img src="/HMM/tex/5e9c7a7d16b15ab5b947bedf5f56bd79.svg?invert_in_darkmode&sanitize=true" align=middle width=14.99998994999999pt height=22.465723500000017pt/>个节点的集合.

<img src="/HMM/tex/4ddffcd42610c451b271272b7ec53505.svg?invert_in_darkmode&sanitize=true" align=middle width=12.32879834999999pt height=22.465723500000017pt/>为转移概率矩阵, <img src="/HMM/tex/bb3c0a1697c75fdb8038ecf006251dd4.svg?invert_in_darkmode&sanitize=true" align=middle width=19.44456194999999pt height=14.15524440000002pt/>表示节点i到节点j的转移概率,
且满足<img src="/HMM/tex/416ddc33e9190caf9cfefbd8552a4a4a.svg?invert_in_darkmode&sanitize=true" align=middle width=116.1664581pt height=32.256008400000006pt/>.

<img src="/HMM/tex/d049e9034b43e5d5bfc25f7e2a30a0e7.svg?invert_in_darkmode&sanitize=true" align=middle width=14.021211599999992pt height=14.15524440000002pt/>为节点<img src="/HMM/tex/8fceb32bd3f6803b77bbe1b1758a60b6.svg?invert_in_darkmode&sanitize=true" align=middle width=5.663225699999989pt height=21.68300969999999pt/>的初始概率分布, 满足<img src="/HMM/tex/c01ea360f7f9da268b266ff4e6551cfe.svg?invert_in_darkmode&sanitize=true" align=middle width=87.18796679999998pt height=32.256008400000006pt/>,
<img src="/HMM/tex/448621753905e93f28aeb01dfbfac7fb.svg?invert_in_darkmode&sanitize=true" align=middle width=44.97994874999999pt height=21.18721440000001pt/>表示不可能为初始状态节点.

例如上图a中, 假设初始概率分布为<img src="/HMM/tex/046186685c17916adfacfab007a9f168.svg?invert_in_darkmode&sanitize=true" align=middle width=241.48054259999995pt height=24.65753399999998pt/>,
那么:

<p align="center"><img src="/HMM/tex/f296616e8cb9c2fc61ba6f646d51c50d.svg?invert_in_darkmode&sanitize=true" align=middle width=372.1137123pt height=16.438356pt/></p>

## Hidden Markov Models

很多情况下, 我们关心的状态是隐藏起来的.
例如, 我们通过文本无法直接观测到词性标注(POS), 我们只可以观测到词.
POS只能通过词序列来推测, 因此是被隐藏起来的.

HMM是一个同时包含了观测状态和隐藏状态的概率模型, 由五个部分组成:
