# [目录](../README.md)

# Logistic Regression

## Hypothesis Representation
对于二分类问题, 可以采用逻辑回归模型. 逻辑回归模型的输出满足:

<p align="center"><img src="/LogisticRegression/tex/15e2ffed319134ffd832927b556f1915.svg?invert_in_darkmode&sanitize=true" align=middle width=77.4447531pt height=16.438356pt/></p>

这样, 可以设定一个阈值来进行二分类.

逻辑回归模型表示为:

<p align="center"><img src="/LogisticRegression/tex/2d7a274decefe3aeeb9e5d33df752126.svg?invert_in_darkmode&sanitize=true" align=middle width=110.1462318pt height=18.7598829pt/></p>

<p align="center"><img src="/LogisticRegression/tex/00892d62bddb0ae4eb3d2cd5a9b54336.svg?invert_in_darkmode&sanitize=true" align=middle width=107.28642869999999pt height=34.3600389pt/></p>

式中, <img src="/LogisticRegression/tex/2ece8d1b43987193f87fca2268326d8a.svg?invert_in_darkmode&sanitize=true" align=middle width=29.58340934999999pt height=24.65753399999998pt/>也称作sigmoid函数, 如下图.

<div align=center><img width="250" src="figure/1.png" alt=" "/></div>

可以看出, sigmoid函数使得输出范围在[0, 1]之间.

逻辑回归模型也看作对于输入<img src="/LogisticRegression/tex/e4fd027188c5ecbf6abde58e5b94bcd5.svg?invert_in_darkmode&sanitize=true" align=middle width=9.39498779999999pt height=14.15524440000002pt/>, 预测得到输入为<img src="/LogisticRegression/tex/a3bd584dc0ef15b1884333c4d22133cf.svg?invert_in_darkmode&sanitize=true" align=middle width=8.649225749999989pt height=14.15524440000002pt/>的概率, 即:

<p align="center"><img src="/LogisticRegression/tex/48867f0d5eff5bbcbb528c12f32fd2f6.svg?invert_in_darkmode&sanitize=true" align=middle width=184.95623189999998pt height=16.438356pt/></p>

由于二分类问题的输出只是为0和1, 因此满足:

<p align="center"><img src="/LogisticRegression/tex/4c95f4d03b1d6d4b5fba356f139b981b.svg?invert_in_darkmode&sanitize=true" align=middle width=237.9257793pt height=16.438356pt/></p>
