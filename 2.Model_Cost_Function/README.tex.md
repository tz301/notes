# [目录](../README.md)

# Model and Cost Function

## Definition
对于回归问题, 假设有一堆训练集, 记:
* $m$ - 训练集的样本数量 <br/>
* $x_s$ - 输入变量/特征 <br/>
* $y_s$ - 输出变量/目标变量 <br/>
* $(x, y)$ - 一个样本对 <br/>
* $(x^{(i)}, y^{(i)})$ - 第$i$个样本对 <br/>

## Model Representation
学习算法通过对训练数据的学习来获取模型$h: X \rightarrow Y$, 也称作hypothesis.
在预测阶段, 将$x$输入模型$h$得到预测的$y$. <br/>
<div align=center><img width="150" height="150" src="1.png"/></div>

## Cost Function
代价函数指导了模型拟合的方向. <br/>
假设模型为: <br/>
<div align=center>$$h_\theta(x)=\theta_0+\theta_1x$$</div>

其中, $\theta_0$和$\theta_1$是待定参数, 不同的参数得到的模型也不同. <br/><br/>
目标是选取最好的$\theta_0$和$\theta_1$, 使得模型对训练集的拟合程度较好, 即
$h_\theta(x)$尽可能与$y$接近, 那么可以将代价函数写成: <br/>
<div align=center>$$J(\theta_0, \theta_1)=\frac {1} {2m}\sum_{i=1}^{m}
(h_\theta(x^{(i)})-y^{(i)})^2$$</div> <br/>
目标就是最小化代价函数
<div align=center>$$\mathop{minimize}\limits_{\theta_0, \theta_1}
J(\theta_0, \theta_1)$$</div> <br/><br/>
可以将代价函数对$\theta_0$和$\theta_1$求偏导并等于0, 从而得到最优的参数.<br/>

可以将代价函数对$\theta_0$和$\theta_1$求偏导并等于0, 从而得到最优的参数.<br/>
$\theta_0$ and $\theta_1$

## Quiz
