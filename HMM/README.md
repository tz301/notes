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
那么, 给定隐状态序列<img src="/HMM/tex/203dc0489d93d6423f18756db63fc1fc.svg?invert_in_darkmode&sanitize=true" align=middle width=127.78558814999998pt height=22.465723500000017pt/>和观测序列
<img src="/HMM/tex/505df8570f602e65f4a0dcba2b3a24ba.svg?invert_in_darkmode&sanitize=true" align=middle width=129.6748035pt height=22.465723500000017pt/>, 观测序列的似然可以表示为:

<p align="center"><img src="/HMM/tex/1e059ace2b5d3733b9f49ef7bcb9f8f1.svg?invert_in_darkmode&sanitize=true" align=middle width=158.57174355pt height=47.806078649999996pt/></p>

那么一条可能的隐状态hot hot cold对应的似然为:

<p align="center"><img src="/HMM/tex/978c1a0d95cea94ee47eda1f78e136f8.svg?invert_in_darkmode&sanitize=true" align=middle width=405.3201405pt height=16.438356pt/></p>

每一条隐状态序列的产生都拥有一定的概率, 容易求出其概率, 得到加权后观测序列的似然为:

<p align="center"><img src="/HMM/tex/c83fceb297b788b4dbf652ca1ffb7ea4.svg?invert_in_darkmode&sanitize=true" align=middle width=412.14030164999997pt height=47.806078649999996pt/></p>

即:

<p align="center"><img src="/HMM/tex/c3e603b4d68b2bd0dbc71f1fce77228e.svg?invert_in_darkmode&sanitize=true" align=middle width=700.2746371499999pt height=16.438356pt/></p>

最后, 将所有可能的隐状态序列对应的似然进行加权求和:

<p align="center"><img src="/HMM/tex/1c15bd48fe9c3be0329d8717940e43e2.svg?invert_in_darkmode&sanitize=true" align=middle width=408.01599465pt height=50.64874485pt/></p>

即:

<p align="center"><img src="/HMM/tex/a959d88aa378fef4613ea4a8ac56e58b.svg?invert_in_darkmode&sanitize=true" align=middle width=458.25956714999995pt height=16.438356pt/></p>

### The Forward Algorithm

对于拥有<img src="/HMM/tex/5e9c7a7d16b15ab5b947bedf5f56bd79.svg?invert_in_darkmode&sanitize=true" align=middle width=14.99998994999999pt height=22.465723500000017pt/>个隐状态的HMM, 如果观测序列长度为<img src="/HMM/tex/ee09a26cd2a8b21b5980249d554ff09f.svg?invert_in_darkmode&sanitize=true" align=middle width=11.889314249999991pt height=22.465723500000017pt/>, 那么总共可能有
<img src="/HMM/tex/cc9a9c5775604b97d905380fe1fb800d.svg?invert_in_darkmode&sanitize=true" align=middle width=24.53368664999999pt height=27.6567522pt/>个隐序列. 对于一般的任务, <img src="/HMM/tex/5e9c7a7d16b15ab5b947bedf5f56bd79.svg?invert_in_darkmode&sanitize=true" align=middle width=14.99998994999999pt height=22.465723500000017pt/>和<img src="/HMM/tex/ee09a26cd2a8b21b5980249d554ff09f.svg?invert_in_darkmode&sanitize=true" align=middle width=11.889314249999991pt height=22.465723500000017pt/>可能很大, 导致计算代价太大.

因此采用动态规划的前向算法, 对每一条可能的路径进行概率求和, 复杂度为<img src="/HMM/tex/5d79089817d0e5a7c958d20f3792bfdf.svg?invert_in_darkmode&sanitize=true" align=middle width=60.04459724999998pt height=26.76175259999998pt/>.

<div align=center><img width="450" src="figure/3.png" alt=" "/></div>

如上图, 网格的节点<img src="/HMM/tex/b77ed6e409322f6100f32c21bb6f1ff6.svg?invert_in_darkmode&sanitize=true" align=middle width=36.79918604999999pt height=24.65753399999998pt/>表示经历过前<img src="/HMM/tex/99d32c17b0344b01c18cce1e210642dc.svg?invert_in_darkmode&sanitize=true" align=middle width=5.936097749999991pt height=20.221802699999984pt/>个观测后状态<img src="/HMM/tex/e62c4c55196ed02fd2fa7c51b8c03611.svg?invert_in_darkmode&sanitize=true" align=middle width=7.710416999999989pt height=21.68300969999999pt/>的总概率:

<p align="center"><img src="/HMM/tex/99940942d27ef1bed984fa14666765cb.svg?invert_in_darkmode&sanitize=true" align=middle width=239.5699779pt height=16.438356pt/></p>

可以得到<img src="/HMM/tex/b77ed6e409322f6100f32c21bb6f1ff6.svg?invert_in_darkmode&sanitize=true" align=middle width=36.79918604999999pt height=24.65753399999998pt/>的递归表达:

<p align="center"><img src="/HMM/tex/182435c150a2555558c40ae55acda8fe.svg?invert_in_darkmode&sanitize=true" align=middle width=197.56815705pt height=47.806078649999996pt/></p>

这样可以将前向算法写作:

1. 初始化:

<p align="center"><img src="/HMM/tex/d3d5c36cdd22b1b3be74add440333900.svg?invert_in_darkmode&sanitize=true" align=middle width=200.7802104pt height=17.031940199999998pt/></p>

2. 递归:

<p align="center"><img src="/HMM/tex/0f94e732efdc27192a7b144d9734f675.svg?invert_in_darkmode&sanitize=true" align=middle width=355.91141849999997pt height=47.806078649999996pt/></p>

3. 终止:

<p align="center"><img src="/HMM/tex/59e8a22ca12bc7f2ab428cb411c91ee6.svg?invert_in_darkmode&sanitize=true" align=middle width=140.49446565pt height=47.806078649999996pt/></p>

## Decoding - The Viterbi Algorithm

解码, 就是给定观测序列, 获取概率最大的隐序列.

例如, 对于例子中的HMM, 给定观测序列(冰淇淋数量){3, 1, 3},
解码的目标是获取最可能的天气序列.

对于每一条隐序列, 我们可以通过前向算法计算其似然, 然后找到似然最大的隐序列,
但是这种算法复杂度太高. 因此采用动态规划的Viterbi算法来计算, 如下图.

<div align=center><img width="450" src="figure/4.png" alt=" "/></div>

Viterbi算法的思想是, 针对观测序列从左到右计算网格值<img src="/HMM/tex/c8d1ebc858a808b1232048d311047b9f.svg?invert_in_darkmode&sanitize=true" align=middle width=34.25160584999999pt height=24.65753399999998pt/>,
代表了状态<img src="/HMM/tex/e62c4c55196ed02fd2fa7c51b8c03611.svg?invert_in_darkmode&sanitize=true" align=middle width=7.710416999999989pt height=21.68300969999999pt/>对于前<img src="/HMM/tex/99d32c17b0344b01c18cce1e210642dc.svg?invert_in_darkmode&sanitize=true" align=middle width=5.936097749999991pt height=20.221802699999984pt/>个观测值最可能的隐状态序列
<img src="/HMM/tex/47daa418aa62420a78bfec3682390c1c.svg?invert_in_darkmode&sanitize=true" align=middle width=83.1125196pt height=14.611911599999981pt/>的概率:

<p align="center"><img src="/HMM/tex/0d9a1b35d92942685b2461e4ed69901c.svg?invert_in_darkmode&sanitize=true" align=middle width=353.92594875pt height=25.2055452pt/></p>

容易得到<img src="/HMM/tex/c8d1ebc858a808b1232048d311047b9f.svg?invert_in_darkmode&sanitize=true" align=middle width=34.25160584999999pt height=24.65753399999998pt/>的递归表达:

<p align="center"><img src="/HMM/tex/8ce2ee61169c905f49bd228a2ee6e8c1.svg?invert_in_darkmode&sanitize=true" align=middle width=201.24585689999998pt height=28.5821118pt/></p>

为了获取最大似然的隐状态序列, 在动态计算概率的过程中,
还需要一个状态量来保存每次取max的路径.

这样可以将Viterbi算法写作:

1. 初始化:

<p align="center"><img src="/HMM/tex/047970733eb3ac4147f52fc8fea9403a.svg?invert_in_darkmode&sanitize=true" align=middle width=222.43349535pt height=41.09589pt/></p>

2. 递归:

<p align="center"><img src="/HMM/tex/f0f4e161e3a06e2c7fb49c6a1e16ebde.svg?invert_in_darkmode&sanitize=true" align=middle width=412.60384275pt height=70.22358089999999pt/></p>

3. 终止:

<p align="center"><img src="/HMM/tex/03b9e99eecefa10ec4b0e76802d81262.svg?invert_in_darkmode&sanitize=true" align=middle width=332.60732835pt height=70.22358089999999pt/></p>

## HMM Training - The Forward-Backward Algorithm

HMM训练采用前向-后向算法, 或者Baum-Wehch算法, 一种EM算法来训练.
给定观测序列和可能的隐状态集合, 通过训练来学习HMM的转移概率和发射概率.
对于每一次迭代, 通过一个状态量来评估模型的优劣, 并不断朝着优化状态量的方向更新.

对于一个简单的例子, 假设存在三组观测序列和隐序列的对应关系:
hot hot cold -> 3 3 2; cold cold cold -> 1 1 2; cold hot hot -> 1 2 3.

那么很容易通过最大似然估计得到HMM的参数:
<p align="center"><img src="/HMM/tex/92c1873ac7212dd60c0b1812c31aad4a.svg?invert_in_darkmode&sanitize=true" align=middle width=270.80692485pt height=139.72602765pt/></p>

然而, 实际情况下, 我们无法知道一个观测序列对应的隐状态序列, 我们仅仅能获取其概率.

在前向算法中定义了前向概率, 还需要定义后向概率<img src="/HMM/tex/9480545cb12c693db1b6559e43971278.svg?invert_in_darkmode&sanitize=true" align=middle width=10.16555099999999pt height=22.831056599999986pt/>, 表示从<img src="/HMM/tex/2f54f1433f0c3a3d7c44740cf8a23287.svg?invert_in_darkmode&sanitize=true" align=middle width=34.24649744999999pt height=21.18721440000001pt/>
个观测值到最后的概率:

<p align="center"><img src="/HMM/tex/e5b65d571e2a7d7a7d59b5f815f72d69.svg?invert_in_darkmode&sanitize=true" align=middle width=247.02244545pt height=16.438356pt/></p>

后向概率的计算与前向概率相似:

1. 初始化:

<p align="center"><img src="/HMM/tex/cc7737fca41e1fcff0619d8534b4be04.svg?invert_in_darkmode&sanitize=true" align=middle width=148.2626277pt height=16.438356pt/></p>

2. 递归:

<p align="center"><img src="/HMM/tex/11c4a716da4274deea1c006d61b50aec.svg?invert_in_darkmode&sanitize=true" align=middle width=367.89014295pt height=50.04352485pt/></p>

3. 终止:

<p align="center"><img src="/HMM/tex/c693a5a5726b4185f4216a33b7d12acb.svg?invert_in_darkmode&sanitize=true" align=middle width=196.74870105pt height=50.04352485pt/></p>

通过前向概率和后向概率就可以估计转移概率和发射概率. 转移概率的最大似然估计为:

<p align="center"><img src="/HMM/tex/6b9e7e33e8a7fcf8c9ad04c19397582a.svg?invert_in_darkmode&sanitize=true" align=middle width=384.15455925pt height=37.0084374pt/></p>

对于上式的分母, 如果对于观测序列上<img src="/HMM/tex/99d32c17b0344b01c18cce1e210642dc.svg?invert_in_darkmode&sanitize=true" align=middle width=5.936097749999991pt height=20.221802699999984pt/>时刻的某个观测值,
能够估计出<img src="/HMM/tex/f28b1ce9dc327019f10e92a9cf6d187a.svg?invert_in_darkmode&sanitize=true" align=middle width=38.94424379999999pt height=21.68300969999999pt/>的转移概率,
那么可以通过对所有时刻的求和得到<img src="/HMM/tex/f28b1ce9dc327019f10e92a9cf6d187a.svg?invert_in_darkmode&sanitize=true" align=middle width=38.94424379999999pt height=21.68300969999999pt/>的转移概率.

定义<img src="/HMM/tex/99d32c17b0344b01c18cce1e210642dc.svg?invert_in_darkmode&sanitize=true" align=middle width=5.936097749999991pt height=20.221802699999984pt/>时刻状态为<img src="/HMM/tex/8fceb32bd3f6803b77bbe1b1758a60b6.svg?invert_in_darkmode&sanitize=true" align=middle width=5.663225699999989pt height=21.68300969999999pt/>, <img src="/HMM/tex/2f54f1433f0c3a3d7c44740cf8a23287.svg?invert_in_darkmode&sanitize=true" align=middle width=34.24649744999999pt height=21.18721440000001pt/>时刻状态为<img src="/HMM/tex/e62c4c55196ed02fd2fa7c51b8c03611.svg?invert_in_darkmode&sanitize=true" align=middle width=7.710416999999989pt height=21.68300969999999pt/>的概率为<img src="/HMM/tex/324efe480281e20ccaa6e9f265fd0f99.svg?invert_in_darkmode&sanitize=true" align=middle width=12.15760424999999pt height=22.831056599999986pt/>:

<p align="center"><img src="/HMM/tex/fcff57eec45e63f74d8eabe3b0bf1833.svg?invert_in_darkmode&sanitize=true" align=middle width=235.8516105pt height=16.438356pt/></p>

为了计算上式, 先计算包含观测序列概率的<img src="/HMM/tex/324efe480281e20ccaa6e9f265fd0f99.svg?invert_in_darkmode&sanitize=true" align=middle width=12.15760424999999pt height=22.831056599999986pt/>:

<p align="center"><img src="/HMM/tex/b92a016a76ebc11fc02f3fc68072db5e.svg?invert_in_darkmode&sanitize=true" align=middle width=335.48359515pt height=16.438356pt/></p>

<div align=center><img width="450" src="figure/4.png" alt=" "/></div>

从上图可以看出<img src="/HMM/tex/c689f4a0f610674011ed94b2d2f28c2e.svg?invert_in_darkmode&sanitize=true" align=middle width=112.70283254999998pt height=22.831056599999986pt/>的计算为:

<p align="center"><img src="/HMM/tex/8471e163a750ec997ae7cb397b547379.svg?invert_in_darkmode&sanitize=true" align=middle width=333.3174471pt height=17.031940199999998pt/></p>

根据贝叶斯定理:

<p align="center"><img src="/HMM/tex/ebe45cd9060a7cf6c71aaf8b38993101.svg?invert_in_darkmode&sanitize=true" align=middle width=176.23050389999997pt height=38.83491479999999pt/></p>

可得:

<p align="center"><img src="/HMM/tex/2f4f2f3bb39cb9ab2d2a33f4a1f19542.svg?invert_in_darkmode&sanitize=true" align=middle width=236.91092865pt height=115.1703762pt/></p>

那么将上式对所有<img src="/HMM/tex/99d32c17b0344b01c18cce1e210642dc.svg?invert_in_darkmode&sanitize=true" align=middle width=5.936097749999991pt height=20.221802699999984pt/>求和就可以得到从状态<img src="/HMM/tex/8fceb32bd3f6803b77bbe1b1758a60b6.svg?invert_in_darkmode&sanitize=true" align=middle width=5.663225699999989pt height=21.68300969999999pt/>到状态<img src="/HMM/tex/e62c4c55196ed02fd2fa7c51b8c03611.svg?invert_in_darkmode&sanitize=true" align=middle width=7.710416999999989pt height=21.68300969999999pt/>的所有转移数量.
还需要计算状态<img src="/HMM/tex/8fceb32bd3f6803b77bbe1b1758a60b6.svg?invert_in_darkmode&sanitize=true" align=middle width=5.663225699999989pt height=21.68300969999999pt/>的所有转移数量, 可以对所有以状态<img src="/HMM/tex/8fceb32bd3f6803b77bbe1b1758a60b6.svg?invert_in_darkmode&sanitize=true" align=middle width=5.663225699999989pt height=21.68300969999999pt/>为起始的转移进行求和得到.
这样, 就得到了转移概率的计算公式:

<p align="center"><img src="/HMM/tex/e0d46e4cb4e47fb9517bb3b7da5cb5ee.svg?invert_in_darkmode&sanitize=true" align=middle width=184.06265624999997pt height=46.72166729999999pt/></p>

同样, 还需要计算发射概率:

<p align="center"><img src="/HMM/tex/34d868ea47ff672a579d70c01998e2b7.svg?invert_in_darkmode&sanitize=true" align=middle width=455.6393721pt height=37.0084374pt/></p>

为了计算上式, 需要知道时刻<img src="/HMM/tex/99d32c17b0344b01c18cce1e210642dc.svg?invert_in_darkmode&sanitize=true" align=middle width=5.936097749999991pt height=20.221802699999984pt/>在状态<img src="/HMM/tex/e62c4c55196ed02fd2fa7c51b8c03611.svg?invert_in_darkmode&sanitize=true" align=middle width=7.710416999999989pt height=21.68300969999999pt/>的概率:

<p align="center"><img src="/HMM/tex/59a5543ce8f1820800a995b70fb914af.svg?invert_in_darkmode&sanitize=true" align=middle width=159.54467925pt height=16.438356pt/></p>

根据贝叶斯定理, 可以将上式写作:

<p align="center"><img src="/HMM/tex/453cd0c1f1205c5991a1a3b2877316cf.svg?invert_in_darkmode&sanitize=true" align=middle width=160.60403204999997pt height=38.83491479999999pt/></p>

<div align=center><img width="450" src="figure/5.png" alt=" "/></div>

通过上图可以看出, 分子项就是前向概率和后向概率的乘积, 那么可得:

<p align="center"><img src="/HMM/tex/b7055fb75ce8b7eee19ccd71b272df48.svg?invert_in_darkmode&sanitize=true" align=middle width=131.06509845pt height=38.83491479999999pt/></p>

那么就得到了发射概率的计算如下:

<p align="center"><img src="/HMM/tex/69e96c5c300ad48fbc8e06128e8d9f8f.svg?invert_in_darkmode&sanitize=true" align=middle width=209.76344565pt height=48.4659615pt/></p>

这样, 就可以通过E-M算法不断迭代估计HMM的参数, 直到收敛. 前向后向算法如下:

1. 初始化转移概率矩阵<img src="/HMM/tex/4ddffcd42610c451b271272b7ec53505.svg?invert_in_darkmode&sanitize=true" align=middle width=12.32879834999999pt height=22.465723500000017pt/>和发射概率矩阵<img src="/HMM/tex/1eb95ebf2173f6c5b3788ff373fd443e.svg?invert_in_darkmode&sanitize=true" align=middle width=13.29340979999999pt height=22.465723500000017pt/>.

2. E-step:

<p align="center"><img src="/HMM/tex/5b37cce3fca4a0c73b1479d78fa7c72d.svg?invert_in_darkmode&sanitize=true" align=middle width=321.49511789999997pt height=84.24519509999999pt/></p>

3. M-step

<p align="center"><img src="/HMM/tex/a327a856614f0a41b787c8dbb00efbe0.svg?invert_in_darkmode&sanitize=true" align=middle width=210.34560195pt height=101.76299594999999pt/></p>

4. 重复2和3直到收敛, 返回<img src="/HMM/tex/4ddffcd42610c451b271272b7ec53505.svg?invert_in_darkmode&sanitize=true" align=middle width=12.32879834999999pt height=22.465723500000017pt/>和<img src="/HMM/tex/1eb95ebf2173f6c5b3788ff373fd443e.svg?invert_in_darkmode&sanitize=true" align=middle width=13.29340979999999pt height=22.465723500000017pt/>.
