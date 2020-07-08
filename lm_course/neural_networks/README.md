# [目录](../README.md)

# Neural Networks

## Model Representation

神经网络可以表示如下:

<div align=center><img width="350" src="figure/1.png" alt=" "/></div>

假设有<img src="/lm_course/neural_networks/tex/7371e4a1b4ff766095a123b7f0023f5c.svg?invert_in_darkmode&sanitize=true" align=middle width=14.433101099999991pt height=14.15524440000002pt/>个训练样本: <img src="/lm_course/neural_networks/tex/9f82bc8a04e7c0ceb9d4239b844f3a0a.svg?invert_in_darkmode&sanitize=true" align=middle width=308.60382465pt height=29.190975000000005pt/>, 定义<img src="/lm_course/neural_networks/tex/6e75432f3e00dc52c8ba25566dcdf692.svg?invert_in_darkmode&sanitize=true" align=middle width=11.18724254999999pt height=22.465723500000017pt/>为网络的层数,
<img src="/lm_course/neural_networks/tex/db186aadfa4df23478b898c594ff33fc.svg?invert_in_darkmode&sanitize=true" align=middle width=11.92926734999999pt height=14.15524440000002pt/>为第<img src="/lm_course/neural_networks/tex/6361dd721b68dd339b33b2652c0abd4b.svg?invert_in_darkmode&sanitize=true" align=middle width=5.2283516999999895pt height=22.831056599999986pt/>层的单元数(不包含偏置单元数).

对于二分类问题, <img src="/lm_course/neural_networks/tex/32978bfb8134984e80f7457b29f7a438.svg?invert_in_darkmode&sanitize=true" align=middle width=38.78604674999999pt height=21.18721440000001pt/> 或者 <img src="/lm_course/neural_networks/tex/6e801e4d7f6a417a4c8efd5be4719b22.svg?invert_in_darkmode&sanitize=true" align=middle width=38.78604674999999pt height=21.18721440000001pt/>.

对于多分类问题, 输出为one-hot向量,
例如<img src="/lm_course/neural_networks/tex/0a5dd30ad92975dfc165839a00b93e3c.svg?invert_in_darkmode&sanitize=true" align=middle width=30.13708169999999pt height=87.12407549999999pt/>.

## Cost Function

神经网络的代价函数是逻辑回归更加一般化的表达:

<p align="center"><img src="/lm_course/neural_networks/tex/2e7416997799bc04748c5ef031a3fa9e.svg?invert_in_darkmode&sanitize=true" align=middle width=519.8380869pt height=108.4456593pt/></p>

其中, <img src="/lm_course/neural_networks/tex/7fdca86fa5369346e24865b4b84db64a.svg?invert_in_darkmode&sanitize=true" align=middle width=15.13700594999999pt height=22.465723500000017pt/>为分类数, <img src="/lm_course/neural_networks/tex/e21f6629c0fd3bb7dbe387a0b7541ea8.svg?invert_in_darkmode&sanitize=true" align=middle width=78.36310515pt height=29.190975000000005pt/>为第<img src="/lm_course/neural_networks/tex/0513e5ea3aca37742a6d9d75796a34c9.svg?invert_in_darkmode&sanitize=true" align=middle width=9.075367949999992pt height=22.831056599999986pt/>类输出.

## Vectorized

记:

<p align="center"><img src="/lm_course/neural_networks/tex/c7c6fd80e824f5b5ea62a1389c66f635.svg?invert_in_darkmode&sanitize=true" align=middle width=181.392618pt height=78.9048876pt/></p>

那么可以将前向计算向量化为:

<p align="center"><img src="/lm_course/neural_networks/tex/a6f7bf12b4a1ae94ac7bdc29df680db7.svg?invert_in_darkmode&sanitize=true" align=middle width=159.9695625pt height=132.92097554999998pt/></p>

## Quiz
1. Which of the following statements are true? Check all that apply. <br/>
(AC) <br/>
A. Any logical function over binary-valued (0 or 1) inputs <img src="/lm_course/neural_networks/tex/6bd71d4c07531ce53dc5d08d0d7e1524.svg?invert_in_darkmode&sanitize=true" align=middle width=15.94753544999999pt height=14.15524440000002pt/> and
<img src="/lm_course/neural_networks/tex/aa0968eba9d0dd34149c2ae25c317f26.svg?invert_in_darkmode&sanitize=true" align=middle width=15.94753544999999pt height=14.15524440000002pt/> can be (approximately) represented using some neural network. <br/>
B. Suppose you have a multi-class classification problem with three
classes, trained with a 3 layer network.
Let <img src="/lm_course/neural_networks/tex/bed7262bf28ca97804e5a063e597fe04.svg?invert_in_darkmode&sanitize=true" align=middle width=110.15807054999999pt height=34.337843099999986pt/> be the activation of the first
output unit, and similarly <img src="/lm_course/neural_networks/tex/797dc3c3796c9230d69fa7c6cd6a32ff.svg?invert_in_darkmode&sanitize=true" align=middle width=110.15807054999999pt height=34.337843099999986pt/> and
<img src="/lm_course/neural_networks/tex/a3ff59afd26cb2ca1239b9aec6c73584.svg?invert_in_darkmode&sanitize=true" align=middle width=110.15807054999999pt height=34.337843099999986pt/> . Then for any input <img src="/lm_course/neural_networks/tex/e4fd027188c5ecbf6abde58e5b94bcd5.svg?invert_in_darkmode&sanitize=true" align=middle width=9.39498779999999pt height=14.15524440000002pt/>, it must be
the case that <img src="/lm_course/neural_networks/tex/613274a2c63e1bce8514c4dc3cf8dfb3.svg?invert_in_darkmode&sanitize=true" align=middle width=149.33213295pt height=34.337843099999986pt/>. <br/>
C. The activation values of the hidden units in a neural network, with
the sigmoid activation function applied at every layer, are always in
the range (0, 1). <br/>
D. A two layer (one input layer, one output layer; no hidden layer)
neural network can represent the XOR function. <br/>

2. Consider the following neural network which takes two binary-valued
inputs <img src="/lm_course/neural_networks/tex/e56570e67eeebd17b1633e437ce24040.svg?invert_in_darkmode&sanitize=true" align=middle width=106.59808169999998pt height=24.65753399999998pt/> and outputs <img src="/lm_course/neural_networks/tex/dd02063f2b3c169f4438637a75f2a4b4.svg?invert_in_darkmode&sanitize=true" align=middle width=42.56482229999999pt height=24.65753399999998pt/>. Which of
the following logical functions does it (approximately) compute? <br/>
(A) <br/>
A. OR <br/>
B. AND <br/>
C. NOT AND <br/>
D. XOR <br/>

<div align=center><img width="350" src="figure/2.png" alt=" "/></div>

3. Consider the neural network given below. Which of the following
equations correctly computes the activation <img src="/lm_course/neural_networks/tex/49349cfe6ea1bf346e639b6598ede31d.svg?invert_in_darkmode&sanitize=true" align=middle width=25.515733649999987pt height=34.337843099999986pt/>?
Note: <img src="/lm_course/neural_networks/tex/2ece8d1b43987193f87fca2268326d8a.svg?invert_in_darkmode&sanitize=true" align=middle width=29.58340934999999pt height=24.65753399999998pt/>is the sigmoid activation function. <br/>
(A) <br/>
A. <img src="/lm_course/neural_networks/tex/ab3355c12342aa2e4d57a5e3ccc1b126.svg?invert_in_darkmode&sanitize=true" align=middle width=290.10495855pt height=37.80850590000001pt/> <br/>
B. <img src="/lm_course/neural_networks/tex/fa40a5f9c5f0d2ab0f00e78d56d01ea0.svg?invert_in_darkmode&sanitize=true" align=middle width=290.10495855pt height=37.80850590000001pt/> <br/>
C. <img src="/lm_course/neural_networks/tex/0b1cdaabc6d0198843f71dccb0ffe98e.svg?invert_in_darkmode&sanitize=true" align=middle width=290.10495855pt height=37.80850590000001pt/> <br/>
D. <img src="/lm_course/neural_networks/tex/36eb282f78ddb86182c18f9b86cb8fdc.svg?invert_in_darkmode&sanitize=true" align=middle width=290.10495855pt height=37.80850590000001pt/> <br/>

<div align=center><img width="350" src="figure/3.png" alt=" "/></div>

4. You have the following neural network. You'd like to compute the
activations of the hidden layer <img src="/lm_course/neural_networks/tex/618f6ec6d89efea72cc409ccafa6182e.svg?invert_in_darkmode&sanitize=true" align=middle width=25.515733649999987pt height=29.190975000000005pt/>. You want to have a
vectorized implementation. Which of the following implementations
correctly compute? Check all that apply. <br>
(A) <br/>
A. <img src="/lm_course/neural_networks/tex/63421037aad93d22991e72b11c2cdc78.svg?invert_in_darkmode&sanitize=true" align=middle width=154.2659316pt height=24.65753399999998pt/> <br/>
B. <img src="/lm_course/neural_networks/tex/f256203daef04810706f51e1d621b67c.svg?invert_in_darkmode&sanitize=true" align=middle width=154.2659316pt height=24.65753399999998pt/> <br/>
C. <img src="/lm_course/neural_networks/tex/1548fec64d4e3cf8c9bd750a31ebf599.svg?invert_in_darkmode&sanitize=true" align=middle width=154.2659316pt height=24.65753399999998pt/> <br/>
D. <img src="/lm_course/neural_networks/tex/8136e1e8a964443682c740580e0b678a.svg?invert_in_darkmode&sanitize=true" align=middle width=202.09680149999997pt height=24.65753399999998pt/> <br/>

<div align=center><img width="350" src="figure/4.png" alt=" "/></div>

5. You are using the neural network pictured below and have learned the
parameters <img src="/lm_course/neural_networks/tex/235e70c0a8ff49e7ca1e0346e3561320.svg?invert_in_darkmode&sanitize=true" align=middle width=165.59383169999998pt height=47.6716218pt/>
(used to compute <img src="/lm_course/neural_networks/tex/618f6ec6d89efea72cc409ccafa6182e.svg?invert_in_darkmode&sanitize=true" align=middle width=25.515733649999987pt height=29.190975000000005pt/>) and <img src="/lm_course/neural_networks/tex/66e31453699f94d503677cbaaae47036.svg?invert_in_darkmode&sanitize=true" align=middle width=161.94085049999998pt height=29.190975000000005pt/>
(used to compute <img src="/lm_course/neural_networks/tex/c7bd5d177078fe65adea0eec8a40e3a5.svg?invert_in_darkmode&sanitize=true" align=middle width=25.515733649999987pt height=29.190975000000005pt/> as a function of <img src="/lm_course/neural_networks/tex/618f6ec6d89efea72cc409ccafa6182e.svg?invert_in_darkmode&sanitize=true" align=middle width=25.515733649999987pt height=29.190975000000005pt/>).
Suppose you swap the parameters for the first hidden layer between its
two units so <img src="/lm_course/neural_networks/tex/b434a27dd623a77fc957b03ac151efb3.svg?invert_in_darkmode&sanitize=true" align=middle width=165.59383169999998pt height=47.6716218pt/> and also swap the output layer so
<img src="/lm_course/neural_networks/tex/cc0fb2250da0ead03c70a8976dd0c5b6.svg?invert_in_darkmode&sanitize=true" align=middle width=161.94085049999998pt height=29.190975000000005pt/>. How will this change the value of the output
<img src="/lm_course/neural_networks/tex/dd02063f2b3c169f4438637a75f2a4b4.svg?invert_in_darkmode&sanitize=true" align=middle width=42.56482229999999pt height=24.65753399999998pt/>? <br/>
(A) <br/>
A. It will stay the same. <br/>
B. It will increase. <br/>
C. It will decrease. <br/>
D. Insufficient information to tell: it may increase or decrease. <br/>

<div align=center><img width="350" src="figure/5.png" alt=" "/></div>

## Exercise

手写数字识别, 通过神经网络识别数字0 ~ 9, 代码见[exercise.py](exercise.py).

输入样本数量为5000, 每张数字图像的像素点数为400, 即20 × 20.

随机抽取100张绘图如下:

<div align=center><img width="450" src="figure/6.png" alt=" "/></div>


