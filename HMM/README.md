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

* <img src="/HMM/tex/bb17b0e6d694fc6d731ee88afe1bae60.svg?invert_in_darkmode&sanitize=true" align=middle width=12.99542474999999pt height=22.465723500000017pt/>为<img src="/HMM/tex/5e9c7a7d16b15ab5b947bedf5f56bd79.svg?invert_in_darkmode&sanitize=true" align=middle width=14.99998994999999pt height=22.465723500000017pt/>个节点的集合.
* <img src="/HMM/tex/4ddffcd42610c451b271272b7ec53505.svg?invert_in_darkmode&sanitize=true" align=middle width=12.32879834999999pt height=22.465723500000017pt/>为转移概率矩阵, <img src="/HMM/tex/bb3c0a1697c75fdb8038ecf006251dd4.svg?invert_in_darkmode&sanitize=true" align=middle width=19.44456194999999pt height=14.15524440000002pt/>表示节点<img src="/HMM/tex/8fceb32bd3f6803b77bbe1b1758a60b6.svg?invert_in_darkmode&sanitize=true" align=middle width=5.663225699999989pt height=21.68300969999999pt/>到节点<img src="/HMM/tex/e62c4c55196ed02fd2fa7c51b8c03611.svg?invert_in_darkmode&sanitize=true" align=middle width=7.710416999999989pt height=21.68300969999999pt/>的转移概率,
且满足<img src="/HMM/tex/416ddc33e9190caf9cfefbd8552a4a4a.svg?invert_in_darkmode&sanitize=true" align=middle width=116.1664581pt height=32.256008400000006pt/>.
* <img src="/HMM/tex/d049e9034b43e5d5bfc25f7e2a30a0e7.svg?invert_in_darkmode&sanitize=true" align=middle width=14.021211599999992pt height=14.15524440000002pt/>为节点<img src="/HMM/tex/8fceb32bd3f6803b77bbe1b1758a60b6.svg?invert_in_darkmode&sanitize=true" align=middle width=5.663225699999989pt height=21.68300969999999pt/>的初始概率分布, 满足<img src="/HMM/tex/c01ea360f7f9da268b266ff4e6551cfe.svg?invert_in_darkmode&sanitize=true" align=middle width=87.18796679999998pt height=32.256008400000006pt/>,
<img src="/HMM/tex/448621753905e93f28aeb01dfbfac7fb.svg?invert_in_darkmode&sanitize=true" align=middle width=44.97994874999999pt height=21.18721440000001pt/>表示不可能为初始状态节点.

例如上图a中, 假设初始概率分布为<img src="/HMM/tex/046186685c17916adfacfab007a9f168.svg?invert_in_darkmode&sanitize=true" align=middle width=241.48054259999995pt height=24.65753399999998pt/>,
那么:

<p align="center"><img src="/HMM/tex/f296616e8cb9c2fc61ba6f646d51c50d.svg?invert_in_darkmode&sanitize=true" align=middle width=372.1137123pt height=16.438356pt/></p>

## Hidden Markov Models

很多情况下, 我们关心的状态是隐藏起来的.
例如, 我们通过文本无法直接观测到词性标注(POS), 我们只可以观测到词.
POS只能通过词序列来推测, 因此是被隐藏起来的.

HMM是一个同时包含了观测状态和隐藏状态的概率模型, 由五个部分组成:

<p align="center"><img src="/HMM/tex/d1c5c17bc5edcebecbb683a7a8dfda78.svg?invert_in_darkmode&sanitize=true" align=middle width=158.4250932pt height=113.0593497pt/></p>

* <img src="/HMM/tex/bb17b0e6d694fc6d731ee88afe1bae60.svg?invert_in_darkmode&sanitize=true" align=middle width=12.99542474999999pt height=22.465723500000017pt/>为<img src="/HMM/tex/5e9c7a7d16b15ab5b947bedf5f56bd79.svg?invert_in_darkmode&sanitize=true" align=middle width=14.99998994999999pt height=22.465723500000017pt/>个节点的集合.
* <img src="/HMM/tex/4ddffcd42610c451b271272b7ec53505.svg?invert_in_darkmode&sanitize=true" align=middle width=12.32879834999999pt height=22.465723500000017pt/>为转移概率矩阵, <img src="/HMM/tex/bb3c0a1697c75fdb8038ecf006251dd4.svg?invert_in_darkmode&sanitize=true" align=middle width=19.44456194999999pt height=14.15524440000002pt/>表示节点<img src="/HMM/tex/8fceb32bd3f6803b77bbe1b1758a60b6.svg?invert_in_darkmode&sanitize=true" align=middle width=5.663225699999989pt height=21.68300969999999pt/>到节点<img src="/HMM/tex/e62c4c55196ed02fd2fa7c51b8c03611.svg?invert_in_darkmode&sanitize=true" align=middle width=7.710416999999989pt height=21.68300969999999pt/>的转移概率,
且满足<img src="/HMM/tex/416ddc33e9190caf9cfefbd8552a4a4a.svg?invert_in_darkmode&sanitize=true" align=middle width=116.1664581pt height=32.256008400000006pt/>.
* <img src="/HMM/tex/8e54b634c62877959e17337133a188a2.svg?invert_in_darkmode&sanitize=true" align=middle width=12.99542474999999pt height=22.465723500000017pt/>为观测序列, 每个观测值来源于词典<img src="/HMM/tex/947d5a3fa201d3d11357deaeb27708ce.svg?invert_in_darkmode&sanitize=true" align=middle width=130.98141539999997pt height=22.465723500000017pt/>.
* <img src="/HMM/tex/1eb95ebf2173f6c5b3788ff373fd443e.svg?invert_in_darkmode&sanitize=true" align=middle width=13.29340979999999pt height=22.465723500000017pt/>为发射概率, 表示节点<img src="/HMM/tex/8fceb32bd3f6803b77bbe1b1758a60b6.svg?invert_in_darkmode&sanitize=true" align=middle width=5.663225699999989pt height=21.68300969999999pt/>产生观测<img src="/HMM/tex/3278587601fbd6585373782719047b74.svg?invert_in_darkmode&sanitize=true" align=middle width=12.933843449999989pt height=14.15524440000002pt/>的概率.
* <img src="/HMM/tex/d049e9034b43e5d5bfc25f7e2a30a0e7.svg?invert_in_darkmode&sanitize=true" align=middle width=14.021211599999992pt height=14.15524440000002pt/>为节点<img src="/HMM/tex/8fceb32bd3f6803b77bbe1b1758a60b6.svg?invert_in_darkmode&sanitize=true" align=middle width=5.663225699999989pt height=21.68300969999999pt/>的初始概率分布, 满足<img src="/HMM/tex/c01ea360f7f9da268b266ff4e6551cfe.svg?invert_in_darkmode&sanitize=true" align=middle width=87.18796679999998pt height=32.256008400000006pt/>,
<img src="/HMM/tex/448621753905e93f28aeb01dfbfac7fb.svg?invert_in_darkmode&sanitize=true" align=middle width=44.97994874999999pt height=21.18721440000001pt/>表示不可能为初始状态节点.

一阶马尔可夫模型遵循两个假设:

1. 某个状态节点的概率仅与前一个状态节点有关:

<p align="center"><img src="/HMM/tex/ceee94c7c67f44415a5d264fd97b7173.svg?invert_in_darkmode&sanitize=true" align=middle width=267.77565375pt height=16.438356pt/></p>

2. 观测值<img src="/HMM/tex/bfc42b48cfe1471b0406c7d9cecaeb1b.svg?invert_in_darkmode&sanitize=true" align=middle width=12.618950849999989pt height=14.15524440000002pt/>仅与产生该观测值的节点<img src="/HMM/tex/7cc9f7d4df7214f10be34880352d9612.svg?invert_in_darkmode&sanitize=true" align=middle width=11.989211849999991pt height=14.15524440000002pt/>有关, 与其他状态节点或者观测值无关,
即输出独立性:

<p align="center"><img src="/HMM/tex/3b84dcce7e1bd461ec0bed0cb5bccb0f.svg?invert_in_darkmode&sanitize=true" align=middle width=311.11138904999996pt height=16.438356pt/></p>

下面用一个例子简述HMM模型. 假设有两种天气COLD(C)和HOT(H), 但是没有天气的信息,
只有每天吃掉的冰淇淋数量. 那么问题变成: 已知观测序列<img src="/HMM/tex/8e54b634c62877959e17337133a188a2.svg?invert_in_darkmode&sanitize=true" align=middle width=12.99542474999999pt height=22.465723500000017pt/>(每天吃掉的冰淇淋数量),
寻找天气(C或者H)对应的隐序列<img src="/HMM/tex/bb17b0e6d694fc6d731ee88afe1bae60.svg?invert_in_darkmode&sanitize=true" align=middle width=12.99542474999999pt height=22.465723500000017pt/>, 如下图.
观测序列<img src="/HMM/tex/a738e7a9fab34d3131e991dc5ba4d18b.svg?invert_in_darkmode&sanitize=true" align=middle width=90.62086934999999pt height=24.65753399999998pt/>对应每天吃掉的冰淇淋数量.

<div align=center><img width="450" src="figure/2.png" alt=" "/></div>

HMM的三个问题:

1. Likelihood: 已知HMM模型 <img src="/HMM/tex/5c8f0ae74f8564dcc17feaf6c68ac190.svg?invert_in_darkmode&sanitize=true" align=middle width=77.22023264999999pt height=24.65753399999998pt/>, 给定观测序列<img src="/HMM/tex/8e54b634c62877959e17337133a188a2.svg?invert_in_darkmode&sanitize=true" align=middle width=12.99542474999999pt height=22.465723500000017pt/>,
计算似然<img src="/HMM/tex/a28e3689e9f711f6b2d3c396dac9388a.svg?invert_in_darkmode&sanitize=true" align=middle width=52.77293669999999pt height=24.65753399999998pt/>.
2. Decoding: 已知HMM模型 <img src="/HMM/tex/5c8f0ae74f8564dcc17feaf6c68ac190.svg?invert_in_darkmode&sanitize=true" align=middle width=77.22023264999999pt height=24.65753399999998pt/>, 给定观测序列<img src="/HMM/tex/8e54b634c62877959e17337133a188a2.svg?invert_in_darkmode&sanitize=true" align=middle width=12.99542474999999pt height=22.465723500000017pt/>,
获取最可能的隐状态序列<img src="/HMM/tex/bb17b0e6d694fc6d731ee88afe1bae60.svg?invert_in_darkmode&sanitize=true" align=middle width=12.99542474999999pt height=22.465723500000017pt/>.
3. Learning: 给定观测序列<img src="/HMM/tex/8e54b634c62877959e17337133a188a2.svg?invert_in_darkmode&sanitize=true" align=middle width=12.99542474999999pt height=22.465723500000017pt/>和一系列状态, 学习HMM的参数<img src="/HMM/tex/4ddffcd42610c451b271272b7ec53505.svg?invert_in_darkmode&sanitize=true" align=middle width=12.32879834999999pt height=22.465723500000017pt/>和<img src="/HMM/tex/1eb95ebf2173f6c5b3788ff373fd443e.svg?invert_in_darkmode&sanitize=true" align=middle width=13.29340979999999pt height=22.465723500000017pt/>.

下面以冰淇淋-天气案例, 分别对这三个问题进行分析和求解, 代码见[exercise.py](exercise.py).

## Likelihood - The Forward Algorithm

假设HMM已知, 计算观测序列(冰淇淋数量)为3 1 3的概率.

由于每个隐状态仅仅产生一个观测值, 隐状态序列长度与观测值序列长度相等.
那么, 给定隐状态序列<img src="/HMM/tex/3a0af56ff3dcf7acc2f1bc48489995a2.svg?invert_in_darkmode&sanitize=true" align=middle width=117.70761749999998pt height=22.465723500000017pt/>和观测序列
<img src="/HMM/tex/60d5e945b9cd7ade28baf8c27ff980a1.svg?invert_in_darkmode&sanitize=true" align=middle width=129.92596319999998pt height=22.465723500000017pt/>, 观测序列的似然可以表示为:

<p align="center"><img src="/HMM/tex/1e059ace2b5d3733b9f49ef7bcb9f8f1.svg?invert_in_darkmode&sanitize=true" align=middle width=158.57174355pt height=47.806078649999996pt/></p>

那么一条可能的隐状态hot hot cold对应的似然为:

<p align="center"><img src="/HMM/tex/1eb656c6d04f5037490d07a65bff22bd.svg?invert_in_darkmode&sanitize=true" align=middle width=377.37865275pt height=16.438356pt/></p>

每一条隐状态序列的产生都拥有一定的概率, 容易求出其概率, 得到加权后观测序列的似然为:

<p align="center"><img src="/HMM/tex/c83fceb297b788b4dbf652ca1ffb7ea4.svg?invert_in_darkmode&sanitize=true" align=middle width=412.14030164999997pt height=47.806078649999996pt/></p>

那么:

<p align="center"><img src="/HMM/tex/b1983e738dbfde708d302c27d579291d.svg?invert_in_darkmode&sanitize=true" align=middle width=680.3317966499999pt height=16.438356pt/></p>

最后, 将所有可能的隐状态序列对应的似然进行加权求和:

<p align="center"><img src="/HMM/tex/a9616b6e9b2cc90c04b10703392aedea.svg?invert_in_darkmode&sanitize=true" align=middle width=390.81042659999997pt height=50.2924224pt/></p>

那么:

<p align="center"><img src="/HMM/tex/a959d88aa378fef4613ea4a8ac56e58b.svg?invert_in_darkmode&sanitize=true" align=middle width=458.25956714999995pt height=16.438356pt/></p>

## Decoding - The Viterbi Algorithm


## HMM Training - The Forward-Backward Algorithm
