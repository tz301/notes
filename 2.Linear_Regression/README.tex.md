# [目录](../README.md)

# Linear Regression

## Definition
对于回归问题, 假设有一堆训练集, 记:
* $ m $ - 训练集的样本数量.
* $ x_s $ - 输入变量/特征.
* $ y_s $ - 输出变量/目标变量.
* $ (x, y) $ - 一个样本对.
* $ (x^{(i)}, y^{(i)}) $ - 第$ i $个样本对.

## Model Representation
学习算法通过对训练数据的学习来获取模型$ h: X \rightarrow Y $, 也称作hypothesis.
在预测阶段, 将$ x $输入模型$ h $得到预测的$ y $.
<div align=center><img width="250" src="figure/1.png" alt=" "/></div>

## Cost Function
我们可以采用代价函数来评估模型的准确性.

假设模型为:
$$ h_\theta(x) = \theta_0 + \theta_1 x $$

其中, $ \theta_0 $和$ \theta_1 $是待定参数, 不同的参数得到的模型也不同.

目标是选取最好的$ \theta_0 $和$ \theta_1 $, 使得模型对训练集的拟合程度较好,
即$ h_\theta(x) $尽可能与$ y $接近, 那么可以将代价函数写成:
$$ J(\theta_0, \theta_1) = \frac {1} {2m} \sum_{i=1}^{m}
(h_\theta(x^{(i)}) - y^{(i)}) ^2 $$

因此, 目标就转化为最小化代价函数:
$$ \mathop{min}\limits_{\theta_0, \theta_1} J(\theta_0, \theta_1) $$

可以将代价函数对$ \theta_0 $和$ \theta_1 $求偏导并等于0, 从而得到最优的参数.

## Gradient Descent
给定不同的参数$ \theta_0 $和$ \theta_1 $, 得到的代价函数值也不一样,
可以将代价函数随着参数变化的曲面绘制出来. 代价函数最小的点, 也就是曲线上最低的点,
此时的参数就是最优模型. 给定初始的参数$ \theta_0 $和$ \theta_1 $,
采用梯度下降算法对参数不断更新, 在曲面上不断"下山", 直到最低点得到最优的参数.

<div align=center><img width="400" src="figure/2.png" alt=" "/></div>

梯度下降算法:
$$ \theta_j := \theta_j - \alpha \frac {\partial} {\partial {\theta_j}}
J(\theta_0, \theta_1), \  j = 0,1 $$

上式中, $ \alpha $称作学习率. 如果学习率较大, 梯度下降就会采用较大的步长下降;
如果学习率较小, 梯度下降就会采用较小的步长下降.

梯度下降算法根据每次更新使用的数据量, 分为:
* Batch Gradient Descent: 每次使用所有训练数据.
* Mini-Batch Gradient Descent: 每次使用训练数据的一个子集.

## Learning Rate
学习率太小, 梯度下降速度可能会很慢.

学习率太大, 梯度下降可能错过局部最优点, 可能不会收敛, 甚至发散.

<div align=center><img width="250" src="figure/3.png" alt=" "/></div>

如果达到最优点, 此时梯度下降算法再更新, 参数就不会再发生变化.

<div align=center><img width="300" src="figure/4.png" alt=" "/></div>

由于梯度下降过程中, 梯度项会不断减小, 因此, 即时学习率固定, 也可以收敛到局部最优.

## Gradient Descent For Linear Regression
将线性回归的模型代入梯度下降的公式, 偏导项变为:
$$ \frac {\partial} {\partial {\theta_j}} J(\theta_0, \theta_1) =
\frac {\partial} {\partial {\theta_j}} \frac {1} {2m}
\sum_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)}) ^2 =
\frac {\partial} {\partial {\theta_j}} \frac {1} {2m}
\sum_{i=1}^m (\theta_0 + \theta_1 x^{(i)} - y^{(i)}) ^2 $$

可以求出$ j=0 $和$ j=1 $时的偏导项为:
$$ \frac {\partial} {\partial {\theta_0}} J(\theta_0, \theta_1) =
\frac {1} {m} \sum_{i=1}^m (\theta_0 + \theta_1 x^{(i)} - y^{(i)}) =
\frac {1} {m} \sum_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)}) $$

$$ \frac {\partial} {\partial {\theta_1}} J(\theta_0, \theta_1) =
\frac {1} {m}\sum_{i=1}^m (\theta_0 + \theta_1 x^{(i)} - y^{(i)})
\cdot x^{(i)} =
\frac {1} {m}\sum_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)}) \cdot x^{(i)} $$

那么梯度下降算法变为:

$$ \theta_0 := \theta_0 - \alpha \frac {1} {m} \sum_{i=1}^m
(h_\theta(x^{(i)}) - y^{(i)}) $$

$$ \theta_1 := \theta_1 - \alpha \frac {1} {m} \sum_{i=1}^m
(h_\theta(x^{(i)}) - y^{(i)}) \cdot x^{(i)} $$

<div align=center><img src="figure/5.png" alt=" "/></div>

注意: 线性回归的搜索空间为凸函数, 因此仅存在全局最优解.

## Multivariate Linear Regression
拓展到更一般的形式, 记:
* $ n $ - 特征的维度.
* $ x^{(i)} $ - 第$ i $个样本.
* $ x_j^{(i)} $ - 第$ i $个样本的第$ j $个特征.

将模型写成:
$$ h_\theta(x) = \theta_0 + \theta_1 x_1 + \theta_2 x_2 + \cdots +
                 \theta_n x_n $$

将上式向量化, 记:

<div align=center>
$
\bold{\theta}=
\left[
\begin{matrix}
  \theta_0 \\
  \theta_1 \\
  \vdots \\
  \theta_n
\end{matrix}
\right]
$, $
\bold{x}=
\left[
\begin{matrix}
  1 \\
  x_1 \\
  \vdots \\
  x_n
\end{matrix}
\right]
$
</div>

将样就可以将模型写成:
$$ h_\theta(x) = \bold{\theta}^T \bold{x} $$

代价函数为:
$$ J(\bold{\theta}) = \frac {1} {2m}
\sum_{i=1}^m (h_\theta(x^{(i)}) - y^{(i)}) ^2 $$

梯度下降为:
$$ \theta_j := \theta_j - \alpha \frac {\partial} {\partial \theta_j}
J(\bold{\theta}), \ j = 0, 1, \cdots, n $$

将线性回归模型代入代价函数可以推导出梯度下降为:
$$ \theta_j := \theta_j - \alpha \frac {1} {m} \sum_{i=1}^m
(h_\theta(x^{(i)}) - y^{(i)}) x_j^{(i)}, \ j = 0, 1, \cdots, n $$

## Quiz
1. Consider the problem of predicting how well a student does in her
second year of college/university, given how well she did in her first
year. <br/>
Specifically, let $ x $ be equal to the number of "A" grades (including
A-. A and A+ grades) that a student receives in their first year of
college (freshmen year). We would like to predict the value of $ y $,
which we define as the number of "A" grades they get in their second
year (sophomore year). <br/>
Refer to the following training set of a small sample of different
students' performances (note that this training set may also be
referenced in other questions in this quiz). Here each row is one
training example. Recall that in linear regression, our hypothesis is
$ h_\theta(x) = \theta_0 + \theta_1 x $, and we use $ m $ to denote the
number of training examples. <br/>
For the training set given above, what is the value of $ m $? <br/>
(4)

<div align=center><img src="figure/6.png" alt=" "/></div>

2. Many substances that can burn (such as gasoline and alcohol) have a
chemical structure based on carbon atoms; for this reason they are
called hydrocarbons. A chemist wants to understand how the number of
carbon atoms in a molecule affects how much energy is released when that
molecule combusts (meaning that it is burned). The chemist obtains the
dataset below. In the column on the right, "kJ/mol" is the unit
measuring the amount of energy released. <br/>
You would like to use linear regression ($ h_\theta(x) = \theta_0 +
\theta_1 x $) to estimate the amount of energy released ($ y $) as a
function of the number of carbon atoms ($ x $). Which of the following
do you think will be the values you obtain for $ \theta_0 $ and
$ \theta_1 $? <br/>
You should be able to select the right answer without actually
implementing linear regression. <br/>
(D) <br/>
A. $ \theta_0 = -1780.0, \theta_1 = 530.9θ $ <br/>
B. $ \theta_0 = -569.6, \theta_1 = 530.9θ $ <br/>
C. $ \theta_0 = -1780.0, \theta_1 = -530.9θ $ <br/>
D. $ \theta_0 = -569.6, \theta_1 = -530.9θ $

<div align=center><img src="figure/7.png" alt=" "/></div>

3. Suppose we set $ \theta_0 = -1, \theta_1 = 2θ $ in the linear
regression hypothesis from Q1. What is $ h_\theta(6) $? <br/>
(11)

4. Let $ f $ be some function so that $ f(\theta_0, \theta_1) $ outputs
a number. For this problem, $ f $ is some arbitrary/unknown smooth
function (not necessarily the cost function of linear regression, so
$ f $ may have local optima). <br/>
Suppose we use gradient descent to try to minimize
$ f(\theta_0, \theta_1) $ as a function of $ \theta_0 $ and $ \theta_1 $.
Which of the following statements are true? (Check all that apply.) <br/>
(AD) <br/>
A. If the learning rate is too small, then gradient descent may take a
very long time to converge. <br/>
B. If $ \theta_0 $ and $ \theta_1 $ are initialized so that
$ \theta_0 = \theta_1 $, then by symmetry (because we do simultaneous
updates to the two parameters), after one iteration of gradient descent,
we will still have $ \theta_0 = \theta_1 $. <br/>
C. Even if the learning rate $ \alpha $ is very large, every iteration of
gradient descent will decrease the value of $ f(\theta_0, \theta_1) $. <br/>
D. If $ \theta_0 $ and $ \theta_1 $ are initialized at a local minimum,
then one iteration will not change their values.

5. Suppose that for some linear regression problem (say, predicting
housing prices as in the lecture), we have some training set, and for
our training set we managed to find some $ \theta_0 $, $ \theta_1 $ such
that $ J(\theta_0, \theta_1) = 0 $. <br/>
Which of the statements below must then be true? (Check all that apply.) <br/>
(D) <br/>
A. For this to be true, we must have $ \theta_0 = 0 $ and
$ \theta_1 = 0 $, so that $ h_\theta(x) = 0 $. <br/>
B. Gradient descent is likely to get stuck at a local minimum and fail
to find the global minimum. <br/>
C. For this to be true, we must have $ y^{(i)} = 0 $ for every value of
$ i = 1, 2, \cdots, m $. <br/>
D. Our training set can be fit perfectly by a straight line, i.e., all
of our training examples lie perfectly on some straight line.
