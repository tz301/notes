# [目录](../README.md)

# Neural Networks

## Forward Propagation

神经网络可以表示如下:

<div align=center><img width="450" src="figure/1.png" alt=" "/></div>

其中, $ a_i^{(j)} $称作第$ j $层的第$ i $个单元的激活(activation),
$ \Theta ^{(j)} $为权重矩阵, 表示第$ j $层到第$ j + 1 $层之间的映射关系.

前向计算如下:

$$
\begin{aligned}
a_1^{(2)} & = g \left( \Theta_{10}^{(1)} x_0 + \Theta_{11}^{(1)} x_1 +
              \Theta_{12}^{(1)} x_2 + \Theta_{13}^{(1)} x_3 \right) \\
a_2^{(2)} & = g \left( \Theta_{20}^{(1)} x_0 + \Theta_{21}^{(1)} x_1 +
              \Theta_{22}^{(1)} x_2 + \Theta_{23}^{(1)} x_3 \right) \\
a_3^{(2)} & = g \left( \Theta_{30}^{(1)} x_0 + \Theta_{31}^{(1)} x_1 +
              \Theta_{32}^{(1)} x_2 + \Theta_{33}^{(1)} x_3 \right) \\
h_{\Theta}(x) & = a_1^{(3)} = g \left(\Theta_{10}^{(2)} a_0^{(2)} +
              \Theta_{11}^{(2)} a_1^{(2)} + \Theta_{12}^{(2)} a_2^{(2)}
              + \Theta_{13}^{(2)} a_3^{(2)} \right)
\end{aligned}
$$

## Vectorized

记:

$$
x=\left[ \begin{matrix} x_0 \\ x_1 \\ x_2 \\ x_3 \end{matrix} \right],
\ z^{(2)}= \left[ \begin{matrix} z_1^{(2)} \\ z_2^{(2)} \\ z_3^{(2)}
                  \end{matrix} \right]
$$

那么可以将前向计算向量化为:

$$
\begin{aligned}
z^{(2)} &= \Theta^{(1)} \\
a^{(2)} &= g(z^{(2)}) \\
a_0^{(2)} &= 1 \\
z^{(3)} &= \Theta^{(2)} a^{(2)} \\
h_{\Theta}(x) &= a^{(3)} = g(z^{(3)})
\end{aligned}
$$
