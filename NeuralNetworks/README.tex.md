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

## Quiz
1. Which of the following statements are true? Check all that apply. <br/>
(AC) <br/>
A. Any logical function over binary-valued (0 or 1) inputs $ x_1 $ and
$ x_2 $ can be (approximately) represented using some neural network. <br/>
B. Suppose you have a multi-class classification problem with three
classes, trained with a 3 layer network.
Let $ a_1^{(3)} = (h_{\Theta}(x))_1 $ be the activation of the first
output unit, and similarly $ a_2^{(3)} = (h_{\Theta}(x))_2 $ and
$ a_3^{(3)} = (h_{\Theta}(x))_3 $ . Then for any input $ x $, it must be
the case that $ a_1^{(3)} + a_2^{(3)} + a_3^{(3)} = 1 $. <br/>
C. The activation values of the hidden units in a neural network, with
the sigmoid activation function applied at every layer, are always in
the range (0, 1). <br/>
D. A two layer (one input layer, one output layer; no hidden layer)
neural network can represent the XOR function. <br/>

2. Consider the following neural network which takes two binary-valued
inputs $ x_1,\ x_2 \in \{0, 1\} $ and outputs $ h_{\Theta}(x) $. Which of
the following logical functions does it (approximately) compute? <br/>
(A) <br/>
A. OR <br/>
B. AND <br/>
C. NOT AND <br/>
D. XOR <br/>

<div align=center><img width="350" src="figure/2.png" alt=" "/></div>

3. Consider the neural network given below. Which of the following
equations correctly computes the activation $ a_1^{(3)} $?
Note: $ g(z) $is the sigmoid activation function. <br/>
(A) <br/>
A. $ a_1^{(3)} & = g \left( \Theta_{1,0}^{(2)} a_0^{(2)} +
\Theta_{1,1}^{(2)} a_1^{(2)} + \Theta_{1,2}^{(2)} a_2^{(2)}\right) $ <br/>
B. $ a_1^{(3)} & = g \left( \Theta_{1,0}^{(2)} a_0^{(1)} +
\Theta_{1,1}^{(2)} a_1^{(1)} + \Theta_{1,2}^{(2)} a_2^{(1)}\right) $ <br/>
C. $ a_1^{(3)} & = g \left( \Theta_{1,0}^{(1)} a_0^{(2)} +
\Theta_{1,1}^{(1)} a_1^{(2)} + \Theta_{1,2}^{(1)} a_2^{(2)}\right) $ <br/>
D. $ a_1^{(3)} & = g \left( \Theta_{2,0}^{(2)} a_0^{(2)} +
\Theta_{2,1}^{(2)} a_1^{(2)} + \Theta_{2,2}^{(2)} a_2^{(2)}\right) $ <br/>

<div align=center><img width="350" src="figure/3.png" alt=" "/></div>

4. You have the following neural network. You'd like to compute the
activations of the hidden layer $ a^{(2)} $. You want to have a
vectorized implementation. Which of the following implementations
correctly compute? Check all that apply. <br>
(A) <br/>
A. $ a_2 = sigmoid(\Theta_1 * x) $ <br/>
B. $ a_2 = sigmoid(x * \Theta_1) $ <br/>
C. $ a_2 = sigmoid(\Theta_2 * x) $ <br/>
D. $ z = sigmoid(x); a2 = \Theta_1 * x $ <br/>

<div align=center><img width="350" src="figure/4.png" alt=" "/></div>

5. You are using the neural network pictured below and have learned the
parameters $ \Theta^{(1)} = \left[ \begin{matrix} 1 & -1.5 & 3.7 \\
                1 & 5.1 & 2.3 \end{matrix} \right] $
(used to compute $ a^{(2)} $) and
$ \Theta^{(2)} = \left[ \begin{matrix} 1 & 0.6 & -0.8
    \end{matrix} \right]$
(used to compute $ a^{(3)} $ as a function of $ a^{(2)} $).
Suppose you swap the parameters for the first hidden layer between its
two units so
$ \Theta^{(1)} = \left[ \begin{matrix} 1 & 5.1 & 2.3 \\
    1 & -1.5 & 3.7 \end{matrix} \right] $
and also swap the output layer so
$ \Theta^{(2)} = \left[ \begin{matrix} 1 & -0.8 & 0.6
    \end{matrix} \right] $.
How will this change the value of the output $ h_{\Theta}(x) $? <br/>
(A) <br/>
A. It will stay the same. <br/>
B. It will increase. <br/>
C. It will decrease. <br/>
D. Insufficient information to tell: it may increase or decrease. <br/>

<div align=center><img width="350" src="figure/5.png" alt=" "/></div>
