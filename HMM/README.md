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

<div align=center><img width="350" src="figure/1.png" alt=" "/></div>

综上, 马尔科夫链主要由三个部分组成:

<p align="center"><img src="/HMM/tex/08332bea384129a7f32e73afaa4f3b03.svg?invert_in_darkmode&sanitize=true" align=middle width=330.552981pt height=133.08250395pt/></p>

例如上图a中, 假设初始概率分布为<img src="/HMM/tex/3426d2c754d1c21af73b8cc320213921.svg?invert_in_darkmode&sanitize=true" align=middle width=296.66329769999993pt height=24.65753399999998pt/>,
那么:

<p align="center"><img src="/HMM/tex/0ba84b096a9da55599542d9b99e33aac.svg?invert_in_darkmode&sanitize=true" align=middle width=427.82968965000003pt height=16.438356pt/></p>
