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

## Quiz
1. Suppose that you have trained a logistic regression classifier, and
it outputs on a new example <img src="/LogisticRegression/tex/e4fd027188c5ecbf6abde58e5b94bcd5.svg?invert_in_darkmode&sanitize=true" align=middle width=9.39498779999999pt height=14.15524440000002pt/> a prediction <img src="/LogisticRegression/tex/18702c15739a48c1ef1a292928623f60.svg?invert_in_darkmode&sanitize=true" align=middle width=82.01097629999998pt height=24.65753399999998pt/>.
This means (check all that apply): <br/>
(AD) <br/>
A. Our estimate for <img src="/LogisticRegression/tex/3b2323922a052ee184472248f4460a81.svg?invert_in_darkmode&sanitize=true" align=middle width=85.67534744999999pt height=24.65753399999998pt/> is 0.3. <br/>
B. Our estimate for <img src="/LogisticRegression/tex/3b2323922a052ee184472248f4460a81.svg?invert_in_darkmode&sanitize=true" align=middle width=85.67534744999999pt height=24.65753399999998pt/> is 0.7. <br/>
C. Our estimate for <img src="/LogisticRegression/tex/1737ce19c93158520b77048cd248ebf5.svg?invert_in_darkmode&sanitize=true" align=middle width=85.67534744999999pt height=24.65753399999998pt/> is 0.3. <br/>
D. Our estimate for <img src="/LogisticRegression/tex/1737ce19c93158520b77048cd248ebf5.svg?invert_in_darkmode&sanitize=true" align=middle width=85.67534744999999pt height=24.65753399999998pt/> is 0.7.

<div align=center><img width="250" src="figure/2.png" alt=" "/></div>

2. Suppose you have the following training set, and fit a logistic
regression classifier
<img src="/LogisticRegression/tex/b13f10a75ac9f00a30a45da83c57e609.svg?invert_in_darkmode&sanitize=true" align=middle width=201.21745875pt height=24.65753399999998pt/>. <br/>
Which of the following are true? Check all that apply. <br/>
(AB) <br/>
A. Adding polynomial features (e.g., instead using
<img src="/LogisticRegression/tex/80f85be22de20b312a36e8178f04749b.svg?invert_in_darkmode&sanitize=true" align=middle width=373.84288094999994pt height=26.76175259999998pt/>)
could increase how well we can fit the training data. <br/>
B. At the optimal value of <img src="/LogisticRegression/tex/6dc297c35dfa9049f077582466f9b777.svg?invert_in_darkmode&sanitize=true" align=middle width=8.17352744999999pt height=22.831056599999986pt/>, we will have
<img src="/LogisticRegression/tex/728c1ea4d9acf3d148edb25fb6a4bb61.svg?invert_in_darkmode&sanitize=true" align=middle width=61.79215184999999pt height=24.65753399999998pt/>. <br/>
C. Adding polynomial features (e.g., instead using
<img src="/LogisticRegression/tex/80f85be22de20b312a36e8178f04749b.svg?invert_in_darkmode&sanitize=true" align=middle width=373.84288094999994pt height=26.76175259999998pt/>)
would increase <img src="/LogisticRegression/tex/da87e8d6186f7c20976773c00d9edbef.svg?invert_in_darkmode&sanitize=true" align=middle width=31.655311049999987pt height=24.65753399999998pt/> because we are now summing over more terms. <br/>
D. If we train gradient descent for enough iterations, for some examples
<img src="/LogisticRegression/tex/84e0bf804573400bad7f9d5c5633506d.svg?invert_in_darkmode&sanitize=true" align=middle width=24.319919249999987pt height=29.190975000000005pt/> in the training set it is possible to obtain
<img src="/LogisticRegression/tex/93240de66cf53a69baaceddbfe59c8e2.svg?invert_in_darkmode&sanitize=true" align=middle width=84.97236329999998pt height=29.190975000000005pt/>.

3. For logistic regression, the gradient is given by
<img src="/LogisticRegression/tex/493e2217e94ec888748531dbe8c5ef46.svg?invert_in_darkmode&sanitize=true" align=middle width=300.0229551pt height=34.337843099999986pt/>.
Which of these is a correct gradient descent update for logistic
regression with a learning rate of <img src="/LogisticRegression/tex/ebb66f0e96fcb4a8d842166969b28831.svg?invert_in_darkmode&sanitize=true" align=middle width=10.57650494999999pt height=14.15524440000002pt/>? Check all that apply. <br/>
(BD) <br/>
A. <img src="/LogisticRegression/tex/3b600bed441cb024b866370402ef69ac.svg?invert_in_darkmode&sanitize=true" align=middle width=280.68428685pt height=29.190975000000005pt/>
(simultaneously update for all jj). <br/>
B. <img src="/LogisticRegression/tex/d30f43f8435333e9d5257b96a216eb3d.svg?invert_in_darkmode&sanitize=true" align=middle width=310.28823374999996pt height=37.80850590000001pt/>
(simultaneously update for all jj). <br/>
C. <img src="/LogisticRegression/tex/fad5ed690a92b4a5d56fe6809f655171.svg?invert_in_darkmode&sanitize=true" align=middle width=307.0276175999999pt height=29.190975000000005pt/> \theta_j := \theta_j - \alpha \frac {1} {m} \sum_{i=1}^m
(h_\theta(x^{(i)}) - y^{(i)}) x_j^{(i)} <img src="/LogisticRegression/tex/5b132f13df72d7757f3930066a5ffba6.svg?invert_in_darkmode&sanitize=true" align=middle width=700.2745497pt height=85.29680940000001pt/> g(z) = \frac {1} {1 + e^{-z}} <img src="/LogisticRegression/tex/4ef87cb749fc2512620659c5e815bd2f.svg?invert_in_darkmode&sanitize=true" align=middle width=381.3254445pt height=24.65753399999998pt/> J(\theta) <img src="/LogisticRegression/tex/a427170846f486fb8d42d8a7492a0b3e.svg?invert_in_darkmode&sanitize=true" align=middle width=245.2803573pt height=22.831056599999986pt/> m \geq 1 <img src="/LogisticRegression/tex/c5bee62261d36c672201728c05ef0ae1.svg?invert_in_darkmode&sanitize=true" align=middle width=1729.8360222pt height=124.74886710000001pt/> h_\theta(x) = g(\theta_0 + \theta_1 x_1 + \theta_2 x_2) <img src="/LogisticRegression/tex/8485bf2a4cc63deaaaf8eb0266c87f1f.svg?invert_in_darkmode&sanitize=true" align=middle width=64.8726804pt height=22.465723500000017pt/> \theta_0 = 6, \theta_1 = 0, \theta_2 = -1θ $.
Which of the following figures represents the decision boundary found
by your classifier? <br/>
(C) <br/>
A. <br/>
  <img width="150" src="figure/3.png" alt=" "/> <br/>
B. <br/>
  <img width="150" src="figure/4.png" alt=" "/> <br/>
C. <br/>
  <img width="150" src="figure/5.png" alt=" "/> <br/>
D. <br/>
  <img width="150" src="figure/6.png" alt=" "/> <br/>
