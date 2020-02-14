# [目录](../README.md)

# Logistic Regression

## Hypothesis Representation
对于二分类问题, 可以采用逻辑回归模型. 逻辑回归模型的输出满足:

$$ 0 \leq h_\theta(x) \lep 1 $$

这样, 可以设定一个阈值来进行二分类.

逻辑回归模型表示为:

$$ h_\theta(x) = g(\theta^T x) $$

$$ g(z) = \frac {1} {1 + e^{-z}} $$

式中, $ g(z) $也称作sigmoid函数, 如下图.

<div align=center><img width="250" src="figure/1.png" alt=" "/></div>

可以看出, sigmoid函数使得输出范围在[0, 1]之间.

逻辑回归模型也看作对于输入$ x $, 预测得到输入为$ y $的概率, 即:

$$ h_theta(x) = P(y = 1 | x; \theta) $$

由于二分类问题的输出只是为0和1, 因此满足:

$$ P(y = 0 | x; \theta) + P(y = 1 | x; \theta) = 1 $$
