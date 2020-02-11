# [目录](../README.md)

# Linear Regression

## Definition
对于回归问题, 假设有一堆训练集, 记:
* <img src="/2.Linear_Regression/tex/7371e4a1b4ff766095a123b7f0023f5c.svg?invert_in_darkmode&sanitize=true" align=middle width=14.433101099999991pt height=14.15524440000002pt/> - 训练集的样本数量.
* <img src="/2.Linear_Regression/tex/8dde4837326a1a7c455b0ed833248442.svg?invert_in_darkmode&sanitize=true" align=middle width=15.599359049999991pt height=14.15524440000002pt/> - 输入变量/特征.
* <img src="/2.Linear_Regression/tex/68e88a2e78e9cd82aa3cdf41067c18c8.svg?invert_in_darkmode&sanitize=true" align=middle width=14.26380119999999pt height=14.15524440000002pt/> - 输出变量/目标变量.
* <img src="/2.Linear_Regression/tex/c195cd8912f414ba9af73b2c2aafd2ed.svg?invert_in_darkmode&sanitize=true" align=middle width=38.135511149999985pt height=24.65753399999998pt/> - 一个样本对.
* <img src="/2.Linear_Regression/tex/eb9e265576aca876700376c25e3c2a4f.svg?invert_in_darkmode&sanitize=true" align=middle width=69.62915025pt height=29.190975000000005pt/> - 第<img src="/2.Linear_Regression/tex/8fceb32bd3f6803b77bbe1b1758a60b6.svg?invert_in_darkmode&sanitize=true" align=middle width=5.663225699999989pt height=21.68300969999999pt/>个样本对.

## Model Representation
学习算法通过对训练数据的学习来获取模型<img src="/2.Linear_Regression/tex/27611da5ba44a199a0b2fb205c415dc3.svg?invert_in_darkmode&sanitize=true" align=middle width=76.84518929999999pt height=22.831056599999986pt/>, 也称作hypothesis.
在预测阶段, 将<img src="/2.Linear_Regression/tex/e4fd027188c5ecbf6abde58e5b94bcd5.svg?invert_in_darkmode&sanitize=true" align=middle width=9.39498779999999pt height=14.15524440000002pt/>输入模型<img src="/2.Linear_Regression/tex/16d81688eb8abf34581ea81bc111629b.svg?invert_in_darkmode&sanitize=true" align=middle width=9.47111549999999pt height=22.831056599999986pt/>得到预测的<img src="/2.Linear_Regression/tex/a3bd584dc0ef15b1884333c4d22133cf.svg?invert_in_darkmode&sanitize=true" align=middle width=8.649225749999989pt height=14.15524440000002pt/>.
<div align=center><img width="250" src="figure/1.png" alt=" "/></div>

## Cost Function
我们可以采用代价函数来评估模型的准确性.

假设模型为:
<p align="center"><img src="/2.Linear_Regression/tex/7bb87a4078c12651492879bc55608d83.svg?invert_in_darkmode&sanitize=true" align=middle width=120.67521674999999pt height=16.438356pt/></p>

其中, <img src="/2.Linear_Regression/tex/2236187420fb2bfcf28d7dfd16ed31e1.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>和<img src="/2.Linear_Regression/tex/233284b1a493a6306b3660ec1885a6f2.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>是待定参数, 不同的参数得到的模型也不同.

目标是选取最好的<img src="/2.Linear_Regression/tex/2236187420fb2bfcf28d7dfd16ed31e1.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>和<img src="/2.Linear_Regression/tex/233284b1a493a6306b3660ec1885a6f2.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>, 使得模型对训练集的拟合程度较好,
即<img src="/2.Linear_Regression/tex/55eb17f084103c0188d2bfd4176e6f99.svg?invert_in_darkmode&sanitize=true" align=middle width=39.088702949999984pt height=24.65753399999998pt/>尽可能与<img src="/2.Linear_Regression/tex/a3bd584dc0ef15b1884333c4d22133cf.svg?invert_in_darkmode&sanitize=true" align=middle width=8.649225749999989pt height=14.15524440000002pt/>接近, 那么可以将代价函数写成:
<p align="center"><img src="/2.Linear_Regression/tex/7040a6ef593e40044bc5f22fe1612b2a.svg?invert_in_darkmode&sanitize=true" align=middle width=254.63021925pt height=44.89738935pt/></p>

因此, 目标就转化为最小化代价函数:
<p align="center"><img src="/2.Linear_Regression/tex/53075bce8556edd7a9e85ba2d373dce5.svg?invert_in_darkmode&sanitize=true" align=middle width=93.67323404999999pt height=25.2967704pt/></p>

可以将代价函数对<img src="/2.Linear_Regression/tex/2236187420fb2bfcf28d7dfd16ed31e1.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>和<img src="/2.Linear_Regression/tex/233284b1a493a6306b3660ec1885a6f2.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>求偏导并等于0, 从而得到最优的参数.

## Gradient Descent
给定不同的参数<img src="/2.Linear_Regression/tex/2236187420fb2bfcf28d7dfd16ed31e1.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>和<img src="/2.Linear_Regression/tex/233284b1a493a6306b3660ec1885a6f2.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>, 得到的代价函数值也不一样,
可以将代价函数随着参数变化的曲面绘制出来. 代价函数最小的点, 也就是曲线上最低的点,
此时的参数就是最优模型. 给定初始的参数<img src="/2.Linear_Regression/tex/2236187420fb2bfcf28d7dfd16ed31e1.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>和<img src="/2.Linear_Regression/tex/233284b1a493a6306b3660ec1885a6f2.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>,
采用梯度下降算法对参数不断更新, 在曲面上不断"下山", 直到最低点得到最优的参数.

<div align=center><img width="400" src="figure/2.png" alt=" "/></div>

梯度下降算法:
<p align="center"><img src="/2.Linear_Regression/tex/c0776618afba758698a62edd45b1b658.svg?invert_in_darkmode&sanitize=true" align=middle width=241.79507715pt height=38.5152603pt/></p>

上式中, <img src="/2.Linear_Regression/tex/ebb66f0e96fcb4a8d842166969b28831.svg?invert_in_darkmode&sanitize=true" align=middle width=10.57650494999999pt height=14.15524440000002pt/>称作学习率. 如果学习率较大, 梯度下降就会采用较大的步长下降;
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
<p align="center"><img src="/2.Linear_Regression/tex/787b76333e5ed8804ba48c82600edd03.svg?invert_in_darkmode&sanitize=true" align=middle width=552.40624395pt height=44.89738935pt/></p>

可以求出<img src="/2.Linear_Regression/tex/28be737271b93c0d86f3eb9e163fce80.svg?invert_in_darkmode&sanitize=true" align=middle width=37.84725779999999pt height=21.68300969999999pt/>和<img src="/2.Linear_Regression/tex/74ee9da34024f67e90043f20c0d73ad1.svg?invert_in_darkmode&sanitize=true" align=middle width=37.84725779999999pt height=21.68300969999999pt/>时的偏导项为:
<p align="center"><img src="/2.Linear_Regression/tex/7022b9c6441ec39eb5e46a1e20e3dd44.svg?invert_in_darkmode&sanitize=true" align=middle width=466.03110014999993pt height=44.89738935pt/></p>

<p align="center"><img src="/2.Linear_Regression/tex/2eb1da774f78ba5377f51a0e2434b430.svg?invert_in_darkmode&sanitize=true" align=middle width=539.2367904pt height=44.89738935pt/></p>

那么梯度下降算法变为:

<p align="center"><img src="/2.Linear_Regression/tex/faf137dd895970c5d7ce2e170b35be10.svg?invert_in_darkmode&sanitize=true" align=middle width=244.3047156pt height=44.89738935pt/></p>

<p align="center"><img src="/2.Linear_Regression/tex/dde3241b2aef27cfae1113f7365976de.svg?invert_in_darkmode&sanitize=true" align=middle width=280.49661585pt height=44.89738935pt/></p>

<div align=center><img src="figure/5.png" alt=" "/></div>

注意: 线性回归的搜索空间为凸函数, 因此仅存在全局最优解.

## Multivariate Linear Regression
拓展到更一般的形式, 记:
* <img src="/2.Linear_Regression/tex/1921941e267a38d161d9fcc7b3df9a61.svg?invert_in_darkmode&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/> - 特征的维度.
* <img src="/2.Linear_Regression/tex/84e0bf804573400bad7f9d5c5633506d.svg?invert_in_darkmode&sanitize=true" align=middle width=24.319919249999987pt height=29.190975000000005pt/> - 第<img src="/2.Linear_Regression/tex/8fceb32bd3f6803b77bbe1b1758a60b6.svg?invert_in_darkmode&sanitize=true" align=middle width=5.663225699999989pt height=21.68300969999999pt/>个样本.
* <img src="/2.Linear_Regression/tex/6f28515b640e9a0c84da5afe21e3ce1b.svg?invert_in_darkmode&sanitize=true" align=middle width=24.319919249999987pt height=34.337843099999986pt/> - 第<img src="/2.Linear_Regression/tex/8fceb32bd3f6803b77bbe1b1758a60b6.svg?invert_in_darkmode&sanitize=true" align=middle width=5.663225699999989pt height=21.68300969999999pt/>个样本的第<img src="/2.Linear_Regression/tex/e62c4c55196ed02fd2fa7c51b8c03611.svg?invert_in_darkmode&sanitize=true" align=middle width=7.710416999999989pt height=21.68300969999999pt/>个特征.

将模型写成:
<p align="center"><img src="/2.Linear_Regression/tex/6fd0b86e597971a3528fcbd6a1d09305.svg?invert_in_darkmode&sanitize=true" align=middle width=273.54788175pt height=16.438356pt/></p>

将上式向量化, 记:

<div align=center>
<img src="/2.Linear_Regression/tex/0a4ce344df6cead5e60550980669b35f.svg?invert_in_darkmode&sanitize=true" align=middle width=68.67386624999999pt height=96.98719139999999pt/>, <img src="/2.Linear_Regression/tex/6fc546ae376be7216667971db85c9f56.svg?invert_in_darkmode&sanitize=true" align=middle width=72.15552794999999pt height=96.98719139999999pt/>
</div>

将样就可以将模型写成:
<p align="center"><img src="/2.Linear_Regression/tex/67bf6821f850a2b5aca64400688c8b6d.svg?invert_in_darkmode&sanitize=true" align=middle width=89.5125693pt height=18.7598829pt/></p>

代价函数为:
<p align="center"><img src="/2.Linear_Regression/tex/20639f1bfa6c7db123ddad8a0821a0f4.svg?invert_in_darkmode&sanitize=true" align=middle width=225.31515929999998pt height=44.89738935pt/></p>

梯度下降为:
<p align="center"><img src="/2.Linear_Regression/tex/7b5a86291511bb54b96c86f3516d5d48.svg?invert_in_darkmode&sanitize=true" align=middle width=261.61596779999996pt height=38.5152603pt/></p>

将线性回归模型代入代价函数可以推导出梯度下降为:
<p align="center"><img src="/2.Linear_Regression/tex/0d77b0dedeb41885a428df97a67013f4.svg?invert_in_darkmode&sanitize=true" align=middle width=383.84403749999996pt height=44.89738935pt/></p>

## Quiz
1. Consider the problem of predicting how well a student does in her
second year of college/university, given how well she did in her first
year. <br/>
Specifically, let <img src="/2.Linear_Regression/tex/e4fd027188c5ecbf6abde58e5b94bcd5.svg?invert_in_darkmode&sanitize=true" align=middle width=9.39498779999999pt height=14.15524440000002pt/> be equal to the number of "A" grades (including
A-. A and A+ grades) that a student receives in their first year of
college (freshmen year). We would like to predict the value of <img src="/2.Linear_Regression/tex/a3bd584dc0ef15b1884333c4d22133cf.svg?invert_in_darkmode&sanitize=true" align=middle width=8.649225749999989pt height=14.15524440000002pt/>,
which we define as the number of "A" grades they get in their second
year (sophomore year). <br/>
Refer to the following training set of a small sample of different
students' performances (note that this training set may also be
referenced in other questions in this quiz). Here each row is one
training example. Recall that in linear regression, our hypothesis is
<img src="/2.Linear_Regression/tex/413b295804493a8dca28132d2b0ed2b3.svg?invert_in_darkmode&sanitize=true" align=middle width=120.67521674999999pt height=24.65753399999998pt/>, and we use <img src="/2.Linear_Regression/tex/7371e4a1b4ff766095a123b7f0023f5c.svg?invert_in_darkmode&sanitize=true" align=middle width=14.433101099999991pt height=14.15524440000002pt/> to denote the
number of training examples. <br/>
For the training set given above, what is the value of <img src="/2.Linear_Regression/tex/7371e4a1b4ff766095a123b7f0023f5c.svg?invert_in_darkmode&sanitize=true" align=middle width=14.433101099999991pt height=14.15524440000002pt/>? <br/>
(4)

<div align=center><img src="figure/6.png" alt=" "/></div>

2. Many substances that can burn (such as gasoline and alcohol) have a
chemical structure based on carbon atoms; for this reason they are
called hydrocarbons. A chemist wants to understand how the number of
carbon atoms in a molecule affects how much energy is released when that
molecule combusts (meaning that it is burned). The chemist obtains the
dataset below. In the column on the right, "kJ/mol" is the unit
measuring the amount of energy released. <br/>
You would like to use linear regression (<img src="/2.Linear_Regression/tex/f490e01ff81c1c7e0df0d309c2f6a0d9.svg?invert_in_darkmode&sanitize=true" align=middle width=120.67521674999999pt height=24.65753399999998pt/>) to estimate the amount of energy released (<img src="/2.Linear_Regression/tex/a3bd584dc0ef15b1884333c4d22133cf.svg?invert_in_darkmode&sanitize=true" align=middle width=8.649225749999989pt height=14.15524440000002pt/>) as a
function of the number of carbon atoms (<img src="/2.Linear_Regression/tex/e4fd027188c5ecbf6abde58e5b94bcd5.svg?invert_in_darkmode&sanitize=true" align=middle width=9.39498779999999pt height=14.15524440000002pt/>). Which of the following
do you think will be the values you obtain for <img src="/2.Linear_Regression/tex/2236187420fb2bfcf28d7dfd16ed31e1.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/> and
<img src="/2.Linear_Regression/tex/233284b1a493a6306b3660ec1885a6f2.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>? <br/>
You should be able to select the right answer without actually
implementing linear regression. <br/>
(D) <br/>
A. <img src="/2.Linear_Regression/tex/1efd9bc9ebe93a7759da5c3849994e9e.svg?invert_in_darkmode&sanitize=true" align=middle width=177.21461505pt height=22.831056599999986pt/> <br/>
B. <img src="/2.Linear_Regression/tex/d017183c2ff2812c716050c06a006a86.svg?invert_in_darkmode&sanitize=true" align=middle width=168.9954057pt height=22.831056599999986pt/> <br/>
C. <img src="/2.Linear_Regression/tex/6487546232b8ea3e33d319806b4795c3.svg?invert_in_darkmode&sanitize=true" align=middle width=190.0000476pt height=22.831056599999986pt/> <br/>
D. <img src="/2.Linear_Regression/tex/1fe60f9029d43d961b06fbb8be8675b0.svg?invert_in_darkmode&sanitize=true" align=middle width=181.78083825pt height=22.831056599999986pt/>

<div align=center><img src="figure/7.png" alt=" "/></div>

3. Suppose we set <img src="/2.Linear_Regression/tex/f9448acbb3a2f2ce879d11cebea77ba0.svg?invert_in_darkmode&sanitize=true" align=middle width=110.54770154999999pt height=22.831056599999986pt/> in the linear
regression hypothesis from Q1. What is <img src="/2.Linear_Regression/tex/9d78133d85e15f9c067a8ced192c769a.svg?invert_in_darkmode&sanitize=true" align=middle width=37.91292449999999pt height=24.65753399999998pt/>? <br/>
(11)

4. Let <img src="/2.Linear_Regression/tex/79986cadd9fb05185bb29bf10739134b.svg?invert_in_darkmode&sanitize=true" align=middle width=9.81741584999999pt height=22.831056599999986pt/> be some function so that <img src="/2.Linear_Regression/tex/7cb0502f5ecaac5bd60f01044f8db685.svg?invert_in_darkmode&sanitize=true" align=middle width=60.09143414999999pt height=24.65753399999998pt/> outputs
a number. For this problem, <img src="/2.Linear_Regression/tex/79986cadd9fb05185bb29bf10739134b.svg?invert_in_darkmode&sanitize=true" align=middle width=9.81741584999999pt height=22.831056599999986pt/> is some arbitrary/unknown smooth
function (not necessarily the cost function of linear regression, so
<img src="/2.Linear_Regression/tex/79986cadd9fb05185bb29bf10739134b.svg?invert_in_darkmode&sanitize=true" align=middle width=9.81741584999999pt height=22.831056599999986pt/> may have local optima). <br/>
Suppose we use gradient descent to try to minimize
<img src="/2.Linear_Regression/tex/7cb0502f5ecaac5bd60f01044f8db685.svg?invert_in_darkmode&sanitize=true" align=middle width=60.09143414999999pt height=24.65753399999998pt/> as a function of <img src="/2.Linear_Regression/tex/2236187420fb2bfcf28d7dfd16ed31e1.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/> and <img src="/2.Linear_Regression/tex/233284b1a493a6306b3660ec1885a6f2.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>.
Which of the following statements are true? (Check all that apply.) <br/>
(AD) <br/>
A. If the learning rate is too small, then gradient descent may take a
very long time to converge. <br/>
B. If <img src="/2.Linear_Regression/tex/2236187420fb2bfcf28d7dfd16ed31e1.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/> and <img src="/2.Linear_Regression/tex/233284b1a493a6306b3660ec1885a6f2.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/> are initialized so that
<img src="/2.Linear_Regression/tex/8803ce22d949dc9cb80a6ba012e61974.svg?invert_in_darkmode&sanitize=true" align=middle width=51.27842114999999pt height=22.831056599999986pt/>, then by symmetry (because we do simultaneous
updates to the two parameters), after one iteration of gradient descent,
we will still have <img src="/2.Linear_Regression/tex/8803ce22d949dc9cb80a6ba012e61974.svg?invert_in_darkmode&sanitize=true" align=middle width=51.27842114999999pt height=22.831056599999986pt/>. <br/>
C. Even if the learning rate <img src="/2.Linear_Regression/tex/ebb66f0e96fcb4a8d842166969b28831.svg?invert_in_darkmode&sanitize=true" align=middle width=10.57650494999999pt height=14.15524440000002pt/> is very large, every iteration of
gradient descent will decrease the value of <img src="/2.Linear_Regression/tex/7cb0502f5ecaac5bd60f01044f8db685.svg?invert_in_darkmode&sanitize=true" align=middle width=60.09143414999999pt height=24.65753399999998pt/>. <br/>
D. If <img src="/2.Linear_Regression/tex/2236187420fb2bfcf28d7dfd16ed31e1.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/> and <img src="/2.Linear_Regression/tex/233284b1a493a6306b3660ec1885a6f2.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/> are initialized at a local minimum,
then one iteration will not change their values.

5. Suppose that for some linear regression problem (say, predicting
housing prices as in the lecture), we have some training set, and for
our training set we managed to find some <img src="/2.Linear_Regression/tex/2236187420fb2bfcf28d7dfd16ed31e1.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>, <img src="/2.Linear_Regression/tex/233284b1a493a6306b3660ec1885a6f2.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/> such
that <img src="/2.Linear_Regression/tex/d65706b0c2b23ae80bbd28b54d2ad6ef.svg?invert_in_darkmode&sanitize=true" align=middle width=91.10721179999999pt height=24.65753399999998pt/>. <br/>
Which of the statements below must then be true? (Check all that apply.) <br/>
(D) <br/>
A. For this to be true, we must have <img src="/2.Linear_Regression/tex/e2bfcb82ca3c43e51f67b25e8ef2c76d.svg?invert_in_darkmode&sanitize=true" align=middle width=45.22819289999998pt height=22.831056599999986pt/> and
<img src="/2.Linear_Regression/tex/6abdd5dfb79819fa50ccbdabc9c065b9.svg?invert_in_darkmode&sanitize=true" align=middle width=45.22819289999998pt height=22.831056599999986pt/>, so that <img src="/2.Linear_Regression/tex/509b732a5847eca7c3f9088fbdf48db2.svg?invert_in_darkmode&sanitize=true" align=middle width=69.22554374999999pt height=24.65753399999998pt/>. <br/>
B. Gradient descent is likely to get stuck at a local minimum and fail
to find the global minimum. <br/>
C. For this to be true, we must have <img src="/2.Linear_Regression/tex/499d6af654bef2b57024cad71dacd3aa.svg?invert_in_darkmode&sanitize=true" align=middle width=54.532866299999995pt height=29.190975000000005pt/> for every value of
<img src="/2.Linear_Regression/tex/bb59f5a1494e2d65f0800ff2d5aba6c3.svg?invert_in_darkmode&sanitize=true" align=middle width=105.0273345pt height=21.68300969999999pt/>. <br/>
D. Our training set can be fit perfectly by a straight line, i.e., all
of our training examples lie perfectly on some straight line.
