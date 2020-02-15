# [目录](../README.md)

# Logistic Regression

## Hypothesis Representation
对于二分类问题, 可以采用逻辑回归模型. 逻辑回归模型的输出满足:

<p align="center"><img src="/LogisticRegression/tex/1868613cf21b409b5be556cf4035300c.svg?invert_in_darkmode&sanitize=true" align=middle width=99.36238289999999pt height=16.438356pt/></p>

这样, 可以设定一个阈值来进行二分类.

逻辑回归模型为:

<p align="center"><img src="/LogisticRegression/tex/2d7a274decefe3aeeb9e5d33df752126.svg?invert_in_darkmode&sanitize=true" align=middle width=110.1462318pt height=18.7598829pt/></p>

<p align="center"><img src="/LogisticRegression/tex/00892d62bddb0ae4eb3d2cd5a9b54336.svg?invert_in_darkmode&sanitize=true" align=middle width=107.28642869999999pt height=34.3600389pt/></p>

式中, <img src="/LogisticRegression/tex/2ece8d1b43987193f87fca2268326d8a.svg?invert_in_darkmode&sanitize=true" align=middle width=29.58340934999999pt height=24.65753399999998pt/>也称作sigmoid函数, 如下图.

<div align=center><img width="250" src="figure/1.png" alt=" "/></div>

可以看出, sigmoid函数使得输出范围在[0, 1]之间.

逻辑回归模型也看作对于输入<img src="/LogisticRegression/tex/e4fd027188c5ecbf6abde58e5b94bcd5.svg?invert_in_darkmode&sanitize=true" align=middle width=9.39498779999999pt height=14.15524440000002pt/>, 预测得到输入为<img src="/LogisticRegression/tex/a3bd584dc0ef15b1884333c4d22133cf.svg?invert_in_darkmode&sanitize=true" align=middle width=8.649225749999989pt height=14.15524440000002pt/>的概率, 即:

<p align="center"><img src="/LogisticRegression/tex/6b3e5fc10bca4afd446e93248eb21882.svg?invert_in_darkmode&sanitize=true" align=middle width=154.85520764999998pt height=16.438356pt/></p>

由于二分类问题的输出只是为0和1, 因此满足:

<p align="center"><img src="/LogisticRegression/tex/4c95f4d03b1d6d4b5fba356f139b981b.svg?invert_in_darkmode&sanitize=true" align=middle width=237.9257793pt height=16.438356pt/></p>

## Cost Function
假如采用类似线性回归的均方误差代价函数, 那么逻辑回归的代价函数是非凸函数,
可能拥有很多局部最优. 因此, 根据逻辑回归的定义, 可以采用如下的代价函数:

<p align="center"><img src="/LogisticRegression/tex/c8a654c0608f754679e3c1fb6b191ae4.svg?invert_in_darkmode&sanitize=true" align=middle width=293.50756545pt height=49.315569599999996pt/></p>

可以看出:
* 当<img src="/LogisticRegression/tex/807e16471a57847c1e6b960d8cf0f0b8.svg?invert_in_darkmode&sanitize=true" align=middle width=69.65555849999998pt height=24.65753399999998pt/>时, 代价函数为0.
* 当<img src="/LogisticRegression/tex/bea07ebf866ba452709545546d622091.svg?invert_in_darkmode&sanitize=true" align=middle width=118.97044334999998pt height=24.65753399999998pt/>时, 代价函数趋向于无穷大.
* 当<img src="/LogisticRegression/tex/8cabf826ba165fa2dd3c5ea65a5930be.svg?invert_in_darkmode&sanitize=true" align=middle width=118.97044334999998pt height=24.65753399999998pt/>时, 代价函数趋向于无穷大.

为了便于推导梯度下降, 可以将代价函数写成更简单的形式:

<p align="center"><img src="/LogisticRegression/tex/e77b4eabb0548209033b818e8546f4d6.svg?invert_in_darkmode&sanitize=true" align=middle width=367.02625904999996pt height=16.438356pt/></p>

上式为仅针对一个样本的代价函数, 对于一个数据集, 代价函数写成:

<p align="center"><img src="/LogisticRegression/tex/38a38a8d9ef62acb8ce8f4981422d801.svg?invert_in_darkmode&sanitize=true" align=middle width=449.92344705pt height=44.89738935pt/></p>

这个代价函数的优点在于它是凸函数, 也可以用最大似然法求解得到.

## Gradient Descent
梯度下降算法为:

<p align="center"><img src="/LogisticRegression/tex/58bcfa503ce25ceca8074da708edaaf3.svg?invert_in_darkmode&sanitize=true" align=middle width=146.3223399pt height=38.5152603pt/></p>

由于:

<p align="center"><img src="/LogisticRegression/tex/1a75c0151a6fcc2a2bb4e4a316aeb58a.svg?invert_in_darkmode&sanitize=true" align=middle width=133.19870024999997pt height=34.9287444pt/></p>

可得:

<p align="center"><img src="/LogisticRegression/tex/374236b429e83fc7c313d7dab9619498.svg?invert_in_darkmode&sanitize=true" align=middle width=282.92986095pt height=157.33944764999998pt/></p>

可得:

<p align="center"><img src="/LogisticRegression/tex/a45a2c3afd74a24fe3ecdcc5b96f5b32.svg?invert_in_darkmode&sanitize=true" align=middle width=321.2960685pt height=258.2016657pt/></p>

通过上式可以得到梯度下降为:

<p align="center"><img src="/LogisticRegression/tex/de33fbbe963b830b0bcacc0af5b8a6bd.svg?invert_in_darkmode&sanitize=true" align=middle width=267.7285215pt height=44.89738935pt/></p>
