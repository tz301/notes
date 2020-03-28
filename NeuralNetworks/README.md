# [目录](../README.md)

# Neural Networks

## Forward Propagation

神经网络可以表示如下:

<div align=center><img width="450" src="figure/1.png" alt=" "/></div>

其中, <img src="/NeuralNetworks/tex/d99cee510704244f8fcfb59040c2cc70.svg?invert_in_darkmode&sanitize=true" align=middle width=25.067672849999987pt height=34.337843099999986pt/>称作第<img src="/NeuralNetworks/tex/e62c4c55196ed02fd2fa7c51b8c03611.svg?invert_in_darkmode&sanitize=true" align=middle width=7.710416999999989pt height=21.68300969999999pt/>层的第<img src="/NeuralNetworks/tex/8fceb32bd3f6803b77bbe1b1758a60b6.svg?invert_in_darkmode&sanitize=true" align=middle width=5.663225699999989pt height=21.68300969999999pt/>个单元的激活(activation),
<img src="/NeuralNetworks/tex/7b9cb8b4adcde0a38b29720400765de6.svg?invert_in_darkmode&sanitize=true" align=middle width=29.16395294999999pt height=29.190975000000005pt/>为权重矩阵, 表示第<img src="/NeuralNetworks/tex/e62c4c55196ed02fd2fa7c51b8c03611.svg?invert_in_darkmode&sanitize=true" align=middle width=7.710416999999989pt height=21.68300969999999pt/>层到第<img src="/NeuralNetworks/tex/edd89410e3ea1e740bc429c05aa17ec6.svg?invert_in_darkmode&sanitize=true" align=middle width=36.02081834999999pt height=21.68300969999999pt/>层之间的映射关系.

前向计算如下:

<p align="center"><img src="/NeuralNetworks/tex/591d252f6de4d7314d954a3331be24ac.svg?invert_in_darkmode&sanitize=true" align=middle width=430.90221899999995pt height=138.08332065pt/></p>

## Vectorized

记:

<p align="center"><img src="/NeuralNetworks/tex/c7c6fd80e824f5b5ea62a1389c66f635.svg?invert_in_darkmode&sanitize=true" align=middle width=181.392618pt height=78.9048876pt/></p>

那么可以将前向计算向量化为:

<p align="center"><img src="/NeuralNetworks/tex/a6f7bf12b4a1ae94ac7bdc29df680db7.svg?invert_in_darkmode&sanitize=true" align=middle width=159.9695625pt height=132.92097554999998pt/></p>
