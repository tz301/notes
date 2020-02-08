# [目录](../README.md)

# Linear Regression

## Definition
对于回归问题, 假设有一堆训练集, 记:
* $m$ - 训练集的样本数量
* $x_s$ - 输入变量/特征
* $y_s$ - 输出变量/目标变量
* $(x, y)$ - 一个样本对
* $(x^{(i)}, y^{(i)})$ - 第$i$个样本对

## Model Representation
学习算法通过对训练数据的学习来获取模型$h: X \rightarrow Y$, 也称作hypothesis.
在预测阶段, 将$x$输入模型$h$得到预测的$y$.
<div align=center><img width="250" height="250" src="1.png"/></div>

## Cost Function
我们可以采用代价函数来评估模型的准确性.

假设模型为:
$$h_\theta(x)=\theta_0+\theta_1x$$

其中, $\theta_0$和$\theta_1$是待定参数, 不同的参数得到的模型也不同.

目标是选取最好的$\theta_0$和$\theta_1$, 使得模型对训练集的拟合程度较好,
即$h_\theta(x)$尽可能与$y$接近, 那么可以将代价函数写成:
$$J(\theta_0, \theta_1)=\frac {1} {2m}\sum_{i=1}^{m}
(h_\theta(x^{(i)})-y^{(i)})^2$$

因此, 目标就转化为最小化代价函数:
$$\mathop{min}\limits_{\theta_0, \theta_1}J(\theta_0, \theta_1)$$

可以将代价函数对$\theta_0$和$\theta_1$求偏导并等于0, 从而得到最优的参数.

## Gradient Descent
给定不同的参数$\theta_0$和$\theta_1$, 得到的代价函数值也不一样,
可以将代价函数随着参数变化的曲面绘制出来. 代价函数最小的点, 也就是曲线上最低的点,
此时的参数就是最优模型. 给定初始的参数$\theta_0$和$\theta_1$,
采用梯度下降算法对参数不断更新, 在曲面上不断"下山", 直到最低点得到最优的参数.

<div align=center><img width="400" height="250" src="2.png"/></div>

梯度下降算法:
$$\theta_j:=\theta_j-\alpha \frac {\partial} {\partial{\theta_j}}
J(\theta_0,\theta_1), \  j=0,1$$

上式中, $\alpha$称作学习率. 如果学习率较大, 梯度下降就会采用较大的步长下降; 如果学
习率较小, 梯度下降就会采用较小的步长下降.

## Quiz
