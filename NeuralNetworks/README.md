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

## Quiz
1. Which of the following statements are true? Check all that apply. <br/>
(AC) <br/>
A. Any logical function over binary-valued (0 or 1) inputs <img src="/NeuralNetworks/tex/6bd71d4c07531ce53dc5d08d0d7e1524.svg?invert_in_darkmode&sanitize=true" align=middle width=15.94753544999999pt height=14.15524440000002pt/> and
<img src="/NeuralNetworks/tex/aa0968eba9d0dd34149c2ae25c317f26.svg?invert_in_darkmode&sanitize=true" align=middle width=15.94753544999999pt height=14.15524440000002pt/> can be (approximately) represented using some neural network. <br/>
B. Suppose you have a multi-class classification problem with three
classes, trained with a 3 layer network.
Let <img src="/NeuralNetworks/tex/bed7262bf28ca97804e5a063e597fe04.svg?invert_in_darkmode&sanitize=true" align=middle width=110.15807054999999pt height=34.337843099999986pt/> be the activation of the first
output unit, and similarly <img src="/NeuralNetworks/tex/797dc3c3796c9230d69fa7c6cd6a32ff.svg?invert_in_darkmode&sanitize=true" align=middle width=110.15807054999999pt height=34.337843099999986pt/> and
<img src="/NeuralNetworks/tex/a3ff59afd26cb2ca1239b9aec6c73584.svg?invert_in_darkmode&sanitize=true" align=middle width=110.15807054999999pt height=34.337843099999986pt/> . Then for any input <img src="/NeuralNetworks/tex/e4fd027188c5ecbf6abde58e5b94bcd5.svg?invert_in_darkmode&sanitize=true" align=middle width=9.39498779999999pt height=14.15524440000002pt/>, it must be
the case that <img src="/NeuralNetworks/tex/613274a2c63e1bce8514c4dc3cf8dfb3.svg?invert_in_darkmode&sanitize=true" align=middle width=149.33213295pt height=34.337843099999986pt/>. <br/>
C. The activation values of the hidden units in a neural network, with
the sigmoid activation function applied at every layer, are always in
the range (0, 1). <br/>
D. A two layer (one input layer, one output layer; no hidden layer)
neural network can represent the XOR function. <br/>

2. Consider the following neural network which takes two binary-valued
inputs <img src="/NeuralNetworks/tex/e56570e67eeebd17b1633e437ce24040.svg?invert_in_darkmode&sanitize=true" align=middle width=106.59808169999998pt height=24.65753399999998pt/> and outputs <img src="/NeuralNetworks/tex/dd02063f2b3c169f4438637a75f2a4b4.svg?invert_in_darkmode&sanitize=true" align=middle width=42.56482229999999pt height=24.65753399999998pt/>. Which of
the following logical functions does it (approximately) compute? <br/>
(A) <br/>
A. OR <br/>
B. AND <br/>
C. NOT AND <br/>
D. XOR <br/>

<div align=center><img width="350" src="figure/2.png" alt=" "/></div>

3. Consider the neural network given below. Which of the following
equations correctly computes the activation <img src="/NeuralNetworks/tex/49349cfe6ea1bf346e639b6598ede31d.svg?invert_in_darkmode&sanitize=true" align=middle width=25.515733649999987pt height=34.337843099999986pt/>?
Note: <img src="/NeuralNetworks/tex/2ece8d1b43987193f87fca2268326d8a.svg?invert_in_darkmode&sanitize=true" align=middle width=29.58340934999999pt height=24.65753399999998pt/>is the sigmoid activation function. <br/>
(A) <br/>
A. <img src="/NeuralNetworks/tex/ab3355c12342aa2e4d57a5e3ccc1b126.svg?invert_in_darkmode&sanitize=true" align=middle width=290.10495855pt height=37.80850590000001pt/> <br/>
B. <img src="/NeuralNetworks/tex/fa40a5f9c5f0d2ab0f00e78d56d01ea0.svg?invert_in_darkmode&sanitize=true" align=middle width=290.10495855pt height=37.80850590000001pt/> <br/>
C. <img src="/NeuralNetworks/tex/0b1cdaabc6d0198843f71dccb0ffe98e.svg?invert_in_darkmode&sanitize=true" align=middle width=290.10495855pt height=37.80850590000001pt/> <br/>
D. <img src="/NeuralNetworks/tex/36eb282f78ddb86182c18f9b86cb8fdc.svg?invert_in_darkmode&sanitize=true" align=middle width=290.10495855pt height=37.80850590000001pt/> <br/>

<div align=center><img width="350" src="figure/3.png" alt=" "/></div>

4. You have the following neural network. You'd like to compute the
activations of the hidden layer <img src="/NeuralNetworks/tex/618f6ec6d89efea72cc409ccafa6182e.svg?invert_in_darkmode&sanitize=true" align=middle width=25.515733649999987pt height=29.190975000000005pt/>. You want to have a
vectorized implementation. Which of the following implementations
correctly compute? Check all that apply. <br>
(A) <br/>
A. <img src="/NeuralNetworks/tex/63421037aad93d22991e72b11c2cdc78.svg?invert_in_darkmode&sanitize=true" align=middle width=154.2659316pt height=24.65753399999998pt/> <br/>
B. <img src="/NeuralNetworks/tex/f256203daef04810706f51e1d621b67c.svg?invert_in_darkmode&sanitize=true" align=middle width=154.2659316pt height=24.65753399999998pt/> <br/>
C. <img src="/NeuralNetworks/tex/1548fec64d4e3cf8c9bd750a31ebf599.svg?invert_in_darkmode&sanitize=true" align=middle width=154.2659316pt height=24.65753399999998pt/> <br/>
D. <img src="/NeuralNetworks/tex/8136e1e8a964443682c740580e0b678a.svg?invert_in_darkmode&sanitize=true" align=middle width=202.09680149999997pt height=24.65753399999998pt/> <br/>

<div align=center><img width="350" src="figure/4.png" alt=" "/></div>

5. You are using the neural network pictured below and have learned the
parameters
<img src="/NeuralNetworks/tex/50d7b5f27171646137759f0b8972cc04.svg?invert_in_darkmode&sanitize=true" align=middle width=165.59383169999998pt height=47.6716218pt/>
(used to compute <img src="/NeuralNetworks/tex/618f6ec6d89efea72cc409ccafa6182e.svg?invert_in_darkmode&sanitize=true" align=middle width=25.515733649999987pt height=29.190975000000005pt/>) and
<img src="/NeuralNetworks/tex/85830eee07f18d8e7a5db5b0c6139596.svg?invert_in_darkmode&sanitize=true" align=middle width=161.94085049999998pt height=29.190975000000005pt/>
(used to compute <img src="/NeuralNetworks/tex/c7bd5d177078fe65adea0eec8a40e3a5.svg?invert_in_darkmode&sanitize=true" align=middle width=25.515733649999987pt height=29.190975000000005pt/> as a function of <img src="/NeuralNetworks/tex/618f6ec6d89efea72cc409ccafa6182e.svg?invert_in_darkmode&sanitize=true" align=middle width=25.515733649999987pt height=29.190975000000005pt/>).
Suppose you swap the parameters for the first hidden layer between its
two units so
<img src="/NeuralNetworks/tex/5ae2899540ac0f70cdfe178fe922dc84.svg?invert_in_darkmode&sanitize=true" align=middle width=165.59383169999998pt height=47.6716218pt/>
and also swap the output layer so
<img src="/NeuralNetworks/tex/f589743e7fe12acd24a065ef4df0d751.svg?invert_in_darkmode&sanitize=true" align=middle width=161.94085049999998pt height=29.190975000000005pt/>.
How will this change the value of the output <img src="/NeuralNetworks/tex/dd02063f2b3c169f4438637a75f2a4b4.svg?invert_in_darkmode&sanitize=true" align=middle width=42.56482229999999pt height=24.65753399999998pt/>? <br/>
(A) <br/>
A. It will stay the same. <br/>
B. It will increase. <br/>
C. It will decrease. <br/>
D. Insufficient information to tell: it may increase or decrease. <br/>

<div align=center><img width="350" src="figure/5.png" alt=" "/></div>
