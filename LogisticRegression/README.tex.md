# [目录](../README.md)

# Logistic Regression

## Hypothesis Representation
对于二分类问题, 可以采用逻辑回归模型. 逻辑回归模型的输出满足:

$$ 0 \leq h_\theta(x) \leq 1 $$

这样, 可以设定一个阈值来进行二分类.

逻辑回归模型为:

$$ h_\theta(x) = g(\theta^T x) $$

$$ g(z) = \frac {1} {1 + e^{-z}} $$

式中, $ g(z) $也称作sigmoid函数, 如下图.

<div align=center><img width="250" src="figure/1.png" alt=" "/></div>

可以看出, sigmoid函数使得输出范围在[0, 1]之间.

逻辑回归模型也看作对于输入$ x $, 预测得到输入为$ y $的概率, 即:

$$ h_\theta(x) = P(y = 1 | x; \theta) $$

由于二分类问题的输出只是为0和1, 因此满足:

$$ P(y = 0 | x; \theta) + P(y = 1 | x; \theta) = 1 $$

## Cost Function
假如采用类似线性回归的均方误差代价函数, 那么逻辑回归的代价函数是非凸函数,
可能拥有很多局部最优. 因此, 根据逻辑回归的定义, 可以采用如下的代价函数:

$$
J(h_\theta(x), y) =
\left\{
\begin{aligned}
\ \ \ -log(h_\theta(x)) \ if \ y = 1 \\
-log(1 - h_\theta(x)) \ if \ y = 0 \\
\end{aligned}
\right.
$$

可以看出:
* 当$ h_\theta(x) = y $时, 代价函数为0.
* 当$ y = 0, h_\theta(x) \rightarrow 1 $时, 代价函数趋向于无穷大.
* 当$ y = 1, h_\theta(x) \rightarrow 0 $时, 代价函数趋向于无穷大.

为了便于推导梯度下降, 可以将代价函数写成更简单的形式:

$$ J(h_\theta(x), y) = - y log(h_\theta(x))
                       - (1 - y) log(1 - h_\theta(x)) $$

上式为仅针对一个样本的代价函数, 对于一个数据集, 代价函数写成:

$$ J(\theta) = - \frac {1} {m} \sum_{i = 1}^m
[ - y^{(i)} log(h_\theta(x^{(i)}))
  - (1 - y^{(i)}) log(1 - h_\theta(x^{(i)}))] $$

这个代价函数的优点在于它是凸函数, 也可以用最大似然法求解得到.

## Gradient Descent

