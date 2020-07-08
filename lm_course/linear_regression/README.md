# [目录](../README.md)

# Linear Regression

## Definition
对于回归问题, 假设有一堆训练集, 记:
* <img src="/lm_course/LinearRegression/tex/abe0fbe21b756ea08ab305f5e3274bae.svg?invert_in_darkmode&sanitize=true" align=middle width=20.369197199999988pt height=20.221802699999984pt/> - 训练集的样本数量.
* <img src="/lm_course/LinearRegression/tex/8dde4837326a1a7c455b0ed833248442.svg?invert_in_darkmode&sanitize=true" align=middle width=15.599359049999991pt height=14.15524440000002pt/> - 输入变量/特征.
* <img src="/lm_course/LinearRegression/tex/68e88a2e78e9cd82aa3cdf41067c18c8.svg?invert_in_darkmode&sanitize=true" align=middle width=14.26380119999999pt height=14.15524440000002pt/> - 输出变量/目标变量.
* <img src="/lm_course/LinearRegression/tex/c195cd8912f414ba9af73b2c2aafd2ed.svg?invert_in_darkmode&sanitize=true" align=middle width=38.135511149999985pt height=24.65753399999998pt/> - 一个样本对.
* <img src="/lm_course/LinearRegression/tex/eb9e265576aca876700376c25e3c2a4f.svg?invert_in_darkmode&sanitize=true" align=middle width=69.62915025pt height=29.190975000000005pt/> - 第<img src="/lm_course/LinearRegression/tex/8fceb32bd3f6803b77bbe1b1758a60b6.svg?invert_in_darkmode&sanitize=true" align=middle width=5.663225699999989pt height=21.68300969999999pt/>个样本对.

## Model Representation
学习算法通过对训练数据的学习来获取模型<img src="/lm_course/LinearRegression/tex/27611da5ba44a199a0b2fb205c415dc3.svg?invert_in_darkmode&sanitize=true" align=middle width=76.84518929999999pt height=22.831056599999986pt/>, 也称作hypothesis.
在预测阶段, 将<img src="/lm_course/LinearRegression/tex/e4fd027188c5ecbf6abde58e5b94bcd5.svg?invert_in_darkmode&sanitize=true" align=middle width=9.39498779999999pt height=14.15524440000002pt/>输入模型<img src="/lm_course/LinearRegression/tex/16d81688eb8abf34581ea81bc111629b.svg?invert_in_darkmode&sanitize=true" align=middle width=9.47111549999999pt height=22.831056599999986pt/>得到预测的<img src="/lm_course/LinearRegression/tex/a3bd584dc0ef15b1884333c4d22133cf.svg?invert_in_darkmode&sanitize=true" align=middle width=8.649225749999989pt height=14.15524440000002pt/>.
<div align=center><img width="250" src="figure/1.png" alt=" "/></div>

## Cost Function
我们可以采用代价函数来评估模型的准确性.

假设模型为:
<p align="center"><img src="/lm_course/linear_regression/tex/7bb87a4078c12651492879bc55608d83.svg?invert_in_darkmode&sanitize=true" align=middle width=120.67521674999999pt height=16.438356pt/></p>

其中, <img src="/lm_course/LinearRegression/tex/2236187420fb2bfcf28d7dfd16ed31e1.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>和<img src="/lm_course/LinearRegression/tex/233284b1a493a6306b3660ec1885a6f2.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>是待定参数, 不同的参数得到的模型也不同.

目标是选取最好的<img src="/lm_course/LinearRegression/tex/2236187420fb2bfcf28d7dfd16ed31e1.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>和<img src="/lm_course/LinearRegression/tex/233284b1a493a6306b3660ec1885a6f2.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>, 使得模型对训练集的拟合程度较好,
即<img src="/lm_course/LinearRegression/tex/55eb17f084103c0188d2bfd4176e6f99.svg?invert_in_darkmode&sanitize=true" align=middle width=39.088702949999984pt height=24.65753399999998pt/>尽可能与<img src="/lm_course/LinearRegression/tex/a3bd584dc0ef15b1884333c4d22133cf.svg?invert_in_darkmode&sanitize=true" align=middle width=8.649225749999989pt height=14.15524440000002pt/>接近, 那么可以将代价函数写成:
<p align="center"><img src="/lm_course/linear_regression/tex/7040a6ef593e40044bc5f22fe1612b2a.svg?invert_in_darkmode&sanitize=true" align=middle width=254.63021925pt height=44.89738935pt/></p>

因此, 目标就转化为最小化代价函数:
<p align="center"><img src="/lm_course/linear_regression/tex/53075bce8556edd7a9e85ba2d373dce5.svg?invert_in_darkmode&sanitize=true" align=middle width=93.67323404999999pt height=25.2967704pt/></p>

可以将代价函数对<img src="/lm_course/LinearRegression/tex/2236187420fb2bfcf28d7dfd16ed31e1.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>和<img src="/lm_course/LinearRegression/tex/233284b1a493a6306b3660ec1885a6f2.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>求偏导并等于0, 从而得到最优的参数.

## Gradient Descent
给定不同的参数<img src="/lm_course/LinearRegression/tex/2236187420fb2bfcf28d7dfd16ed31e1.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>和<img src="/lm_course/LinearRegression/tex/233284b1a493a6306b3660ec1885a6f2.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>, 得到的代价函数值也不一样,
可以将代价函数随着参数变化的曲面绘制出来. 代价函数最小的点, 也就是曲线上最低的点,
此时的参数就是最优模型. 给定初始的参数<img src="/lm_course/LinearRegression/tex/2236187420fb2bfcf28d7dfd16ed31e1.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>和<img src="/lm_course/LinearRegression/tex/233284b1a493a6306b3660ec1885a6f2.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>,
采用梯度下降算法对参数不断更新, 在曲面上不断"下山", 直到最低点得到最优的参数.

<div align=center><img width="400" src="figure/2.png" alt=" "/></div>

梯度下降算法:
<p align="center"><img src="/lm_course/linear_regression/tex/c0776618afba758698a62edd45b1b658.svg?invert_in_darkmode&sanitize=true" align=middle width=241.79507715pt height=38.5152603pt/></p>

上式中, <img src="/lm_course/LinearRegression/tex/ebb66f0e96fcb4a8d842166969b28831.svg?invert_in_darkmode&sanitize=true" align=middle width=10.57650494999999pt height=14.15524440000002pt/>称作学习率. 如果学习率较大, 梯度下降就会采用较大的步长下降;
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

如果代价函数降低较慢, 或者梯度下降不工作, 使用更小的学习率.

## Gradient Descent For Linear Regression
将线性回归的模型代入梯度下降的公式, 偏导项变为:
<p align="center"><img src="/lm_course/linear_regression/tex/787b76333e5ed8804ba48c82600edd03.svg?invert_in_darkmode&sanitize=true" align=middle width=552.40624395pt height=44.89738935pt/></p>

可以求出<img src="/lm_course/LinearRegression/tex/28be737271b93c0d86f3eb9e163fce80.svg?invert_in_darkmode&sanitize=true" align=middle width=37.84725779999999pt height=21.68300969999999pt/>和<img src="/lm_course/LinearRegression/tex/74ee9da34024f67e90043f20c0d73ad1.svg?invert_in_darkmode&sanitize=true" align=middle width=37.84725779999999pt height=21.68300969999999pt/>时的偏导项为:
<p align="center"><img src="/lm_course/linear_regression/tex/7022b9c6441ec39eb5e46a1e20e3dd44.svg?invert_in_darkmode&sanitize=true" align=middle width=466.03110014999993pt height=44.89738935pt/></p>

<p align="center"><img src="/lm_course/linear_regression/tex/2eb1da774f78ba5377f51a0e2434b430.svg?invert_in_darkmode&sanitize=true" align=middle width=539.2367904pt height=44.89738935pt/></p>

那么梯度下降算法变为:

<p align="center"><img src="/lm_course/linear_regression/tex/faf137dd895970c5d7ce2e170b35be10.svg?invert_in_darkmode&sanitize=true" align=middle width=244.3047156pt height=44.89738935pt/></p>

<p align="center"><img src="/lm_course/linear_regression/tex/dde3241b2aef27cfae1113f7365976de.svg?invert_in_darkmode&sanitize=true" align=middle width=280.49661585pt height=44.89738935pt/></p>

<div align=center><img src="figure/5.png" alt=" "/></div>

注意: 线性回归的搜索空间为凸函数, 因此仅存在全局最优解.

## Multivariate Linear Regression
拓展到更一般的形式, 记:
* <img src="/lm_course/LinearRegression/tex/1921941e267a38d161d9fcc7b3df9a61.svg?invert_in_darkmode&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/> - 特征的维度.
* <img src="/lm_course/LinearRegression/tex/84e0bf804573400bad7f9d5c5633506d.svg?invert_in_darkmode&sanitize=true" align=middle width=24.319919249999987pt height=29.190975000000005pt/> - 第<img src="/lm_course/LinearRegression/tex/8fceb32bd3f6803b77bbe1b1758a60b6.svg?invert_in_darkmode&sanitize=true" align=middle width=5.663225699999989pt height=21.68300969999999pt/>个样本.
* <img src="/lm_course/LinearRegression/tex/6f28515b640e9a0c84da5afe21e3ce1b.svg?invert_in_darkmode&sanitize=true" align=middle width=24.319919249999987pt height=34.337843099999986pt/> - 第<img src="/lm_course/LinearRegression/tex/8fceb32bd3f6803b77bbe1b1758a60b6.svg?invert_in_darkmode&sanitize=true" align=middle width=5.663225699999989pt height=21.68300969999999pt/>个样本的第<img src="/lm_course/LinearRegression/tex/e62c4c55196ed02fd2fa7c51b8c03611.svg?invert_in_darkmode&sanitize=true" align=middle width=7.710416999999989pt height=21.68300969999999pt/>个特征.

将模型写成:
<p align="center"><img src="/lm_course/linear_regression/tex/6fd0b86e597971a3528fcbd6a1d09305.svg?invert_in_darkmode&sanitize=true" align=middle width=273.54788175pt height=16.438356pt/></p>

将上式向量化, 记:

<div align=center>
<img src="/lm_course/linear_regression/tex/0a4ce344df6cead5e60550980669b35f.svg?invert_in_darkmode&sanitize=true" align=middle width=68.67386624999999pt height=96.98719139999999pt/>, <img src="/lm_course/linear_regression/tex/6fc546ae376be7216667971db85c9f56.svg?invert_in_darkmode&sanitize=true" align=middle width=72.15552794999999pt height=96.98719139999999pt/>
</div>

这样就可以将模型写成:
<p align="center"><img src="/lm_course/linear_regression/tex/67bf6821f850a2b5aca64400688c8b6d.svg?invert_in_darkmode&sanitize=true" align=middle width=89.5125693pt height=18.7598829pt/></p>

代价函数为:
<p align="center"><img src="/lm_course/linear_regression/tex/20639f1bfa6c7db123ddad8a0821a0f4.svg?invert_in_darkmode&sanitize=true" align=middle width=225.31515929999998pt height=44.89738935pt/></p>

梯度下降为:
<p align="center"><img src="/lm_course/linear_regression/tex/7b5a86291511bb54b96c86f3516d5d48.svg?invert_in_darkmode&sanitize=true" align=middle width=261.61596779999996pt height=38.5152603pt/></p>

将线性回归模型代入代价函数可以推导出梯度下降为:
<p align="center"><img src="/lm_course/linear_regression/tex/0d77b0dedeb41885a428df97a67013f4.svg?invert_in_darkmode&sanitize=true" align=middle width=383.84403749999996pt height=44.89738935pt/></p>

## Speech Up Gradient Descent
Feature scaling: 将特征除以特征值的范围(最大值 - 最小值),
保证所有特征在近似的尺度.

Mean normalization: 将特征减去特征的平均值, 使得特征近似0均值.

结合feature scaling和mean normalization, 将特征写成:
<p align="center"><img src="/lm_course/linear_regression/tex/e8f178004bd95bcc30e88764a5af861e.svg?invert_in_darkmode&sanitize=true" align=middle width=93.6608838pt height=34.45133834999999pt/></p>

其中, <img src="/lm_course/LinearRegression/tex/688dbd12716c0eaca6462457c9a17196.svg?invert_in_darkmode&sanitize=true" align=middle width=14.555823149999991pt height=14.15524440000002pt/>为所有特征的平均值, <img src="/lm_course/LinearRegression/tex/400f4e35cd6f84ba45f7b829a2df1668.svg?invert_in_darkmode&sanitize=true" align=middle width=12.35637809999999pt height=14.15524440000002pt/>为特征的最大值 - 最小值,
或者是特征的标准差.

## Normal Equation
线性回归也可以采用下式来直接计算(代价函数求导为0直接推导):

<p align="center"><img src="/lm_course/linear_regression/tex/b5051d1f3821056ae4900c05ef2bc58f.svg?invert_in_darkmode&sanitize=true" align=middle width=134.3524182pt height=18.7598829pt/></p>

如果特征数<img src="/lm_course/LinearRegression/tex/1921941e267a38d161d9fcc7b3df9a61.svg?invert_in_darkmode&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/>比较大, 采用上式会导致计算速度太慢.

## Quiz
1. Consider the problem of predicting how well a student does in her
second year of college/university, given how well she did in her first
year. <br/>
Specifically, let <img src="/lm_course/LinearRegression/tex/e4fd027188c5ecbf6abde58e5b94bcd5.svg?invert_in_darkmode&sanitize=true" align=middle width=9.39498779999999pt height=14.15524440000002pt/> be equal to the number of "A" grades (including
A-. A and A+ grades) that a student receives in their first year of
college (freshmen year). We would like to predict the value of <img src="/lm_course/LinearRegression/tex/a3bd584dc0ef15b1884333c4d22133cf.svg?invert_in_darkmode&sanitize=true" align=middle width=8.649225749999989pt height=14.15524440000002pt/>,
which we define as the number of "A" grades they get in their second
year (sophomore year). <br/>
Refer to the following training set of a small sample of different
students' performances (note that this training set may also be
referenced in other questions in this quiz). Here each row is one
training example. Recall that in linear regression, our hypothesis is
<img src="/lm_course/LinearRegression/tex/413b295804493a8dca28132d2b0ed2b3.svg?invert_in_darkmode&sanitize=true" align=middle width=120.67521674999999pt height=24.65753399999998pt/>, and we use <img src="/lm_course/LinearRegression/tex/7371e4a1b4ff766095a123b7f0023f5c.svg?invert_in_darkmode&sanitize=true" align=middle width=14.433101099999991pt height=14.15524440000002pt/> to denote the
number of training examples. <br/>
For the training set given above, what is the value of <img src="/lm_course/LinearRegression/tex/7371e4a1b4ff766095a123b7f0023f5c.svg?invert_in_darkmode&sanitize=true" align=middle width=14.433101099999991pt height=14.15524440000002pt/>? <br/>
(4)

<div align=center><img src="figure/6.png" alt=" "/></div>

2. Many substances that can burn (such as gasoline and alcohol) have a
chemical structure based on carbon atoms; for this reason they are
called hydrocarbons. A chemist wants to understand how the number of
carbon atoms in a molecule affects how much energy is released when that
molecule combusts (meaning that it is burned). The chemist obtains the
dataset below. In the column on the right, "kJ/mol" is the unit
measuring the amount of energy released. <br/>
You would like to use linear regression (<img src="/lm_course/LinearRegression/tex/f490e01ff81c1c7e0df0d309c2f6a0d9.svg?invert_in_darkmode&sanitize=true" align=middle width=120.67521674999999pt height=24.65753399999998pt/>) to estimate the amount of energy released (<img src="/lm_course/LinearRegression/tex/a3bd584dc0ef15b1884333c4d22133cf.svg?invert_in_darkmode&sanitize=true" align=middle width=8.649225749999989pt height=14.15524440000002pt/>) as a
function of the number of carbon atoms (<img src="/lm_course/LinearRegression/tex/e4fd027188c5ecbf6abde58e5b94bcd5.svg?invert_in_darkmode&sanitize=true" align=middle width=9.39498779999999pt height=14.15524440000002pt/>). Which of the following
do you think will be the values you obtain for <img src="/lm_course/LinearRegression/tex/2236187420fb2bfcf28d7dfd16ed31e1.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/> and
<img src="/lm_course/LinearRegression/tex/233284b1a493a6306b3660ec1885a6f2.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>? <br/>
You should be able to select the right answer without actually
implementing linear regression. <br/>
(D) <br/>
A. <img src="/lm_course/LinearRegression/tex/1efd9bc9ebe93a7759da5c3849994e9e.svg?invert_in_darkmode&sanitize=true" align=middle width=177.21461505pt height=22.831056599999986pt/> <br/>
B. <img src="/lm_course/LinearRegression/tex/d017183c2ff2812c716050c06a006a86.svg?invert_in_darkmode&sanitize=true" align=middle width=168.9954057pt height=22.831056599999986pt/> <br/>
C. <img src="/lm_course/LinearRegression/tex/6487546232b8ea3e33d319806b4795c3.svg?invert_in_darkmode&sanitize=true" align=middle width=190.0000476pt height=22.831056599999986pt/> <br/>
D. <img src="/lm_course/LinearRegression/tex/1fe60f9029d43d961b06fbb8be8675b0.svg?invert_in_darkmode&sanitize=true" align=middle width=181.78083825pt height=22.831056599999986pt/>

<div align=center><img src="figure/7.png" alt=" "/></div>

3. Suppose we set <img src="/lm_course/LinearRegression/tex/f9448acbb3a2f2ce879d11cebea77ba0.svg?invert_in_darkmode&sanitize=true" align=middle width=110.54770154999999pt height=22.831056599999986pt/> in the linear
regression hypothesis from Q1. What is <img src="/lm_course/LinearRegression/tex/9d78133d85e15f9c067a8ced192c769a.svg?invert_in_darkmode&sanitize=true" align=middle width=37.91292449999999pt height=24.65753399999998pt/>? <br/>
(11)

4. Let <img src="/lm_course/LinearRegression/tex/79986cadd9fb05185bb29bf10739134b.svg?invert_in_darkmode&sanitize=true" align=middle width=9.81741584999999pt height=22.831056599999986pt/> be some function so that <img src="/lm_course/LinearRegression/tex/7cb0502f5ecaac5bd60f01044f8db685.svg?invert_in_darkmode&sanitize=true" align=middle width=60.09143414999999pt height=24.65753399999998pt/> outputs
a number. For this problem, <img src="/lm_course/LinearRegression/tex/79986cadd9fb05185bb29bf10739134b.svg?invert_in_darkmode&sanitize=true" align=middle width=9.81741584999999pt height=22.831056599999986pt/> is some arbitrary/unknown smooth
function (not necessarily the cost function of linear regression, so
<img src="/lm_course/LinearRegression/tex/79986cadd9fb05185bb29bf10739134b.svg?invert_in_darkmode&sanitize=true" align=middle width=9.81741584999999pt height=22.831056599999986pt/> may have local optima). <br/>
Suppose we use gradient descent to try to minimize
<img src="/lm_course/LinearRegression/tex/7cb0502f5ecaac5bd60f01044f8db685.svg?invert_in_darkmode&sanitize=true" align=middle width=60.09143414999999pt height=24.65753399999998pt/> as a function of <img src="/lm_course/LinearRegression/tex/2236187420fb2bfcf28d7dfd16ed31e1.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/> and <img src="/lm_course/LinearRegression/tex/233284b1a493a6306b3660ec1885a6f2.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>.
Which of the following statements are true? (Check all that apply.) <br/>
(AD) <br/>
A. If the learning rate is too small, then gradient descent may take a
very long time to converge. <br/>
B. If <img src="/lm_course/LinearRegression/tex/2236187420fb2bfcf28d7dfd16ed31e1.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/> and <img src="/lm_course/LinearRegression/tex/233284b1a493a6306b3660ec1885a6f2.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/> are initialized so that
<img src="/lm_course/LinearRegression/tex/8803ce22d949dc9cb80a6ba012e61974.svg?invert_in_darkmode&sanitize=true" align=middle width=51.27842114999999pt height=22.831056599999986pt/>, then by symmetry (because we do simultaneous
updates to the two parameters), after one iteration of gradient descent,
we will still have <img src="/lm_course/LinearRegression/tex/8803ce22d949dc9cb80a6ba012e61974.svg?invert_in_darkmode&sanitize=true" align=middle width=51.27842114999999pt height=22.831056599999986pt/>. <br/>
C. Even if the learning rate <img src="/lm_course/LinearRegression/tex/ebb66f0e96fcb4a8d842166969b28831.svg?invert_in_darkmode&sanitize=true" align=middle width=10.57650494999999pt height=14.15524440000002pt/> is very large, every iteration of
gradient descent will decrease the value of <img src="/lm_course/LinearRegression/tex/7cb0502f5ecaac5bd60f01044f8db685.svg?invert_in_darkmode&sanitize=true" align=middle width=60.09143414999999pt height=24.65753399999998pt/>. <br/>
D. If <img src="/lm_course/LinearRegression/tex/2236187420fb2bfcf28d7dfd16ed31e1.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/> and <img src="/lm_course/LinearRegression/tex/233284b1a493a6306b3660ec1885a6f2.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/> are initialized at a local minimum,
then one iteration will not change their values.

5. Suppose that for some linear regression problem (say, predicting
housing prices as in the lecture), we have some training set, and for
our training set we managed to find some <img src="/lm_course/LinearRegression/tex/2236187420fb2bfcf28d7dfd16ed31e1.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>, <img src="/lm_course/LinearRegression/tex/233284b1a493a6306b3660ec1885a6f2.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/> such
that <img src="/lm_course/LinearRegression/tex/d65706b0c2b23ae80bbd28b54d2ad6ef.svg?invert_in_darkmode&sanitize=true" align=middle width=91.10721179999999pt height=24.65753399999998pt/>. <br/>
Which of the statements below must then be true? (Check all that apply.) <br/>
(D) <br/>
A. For this to be true, we must have <img src="/lm_course/LinearRegression/tex/e2bfcb82ca3c43e51f67b25e8ef2c76d.svg?invert_in_darkmode&sanitize=true" align=middle width=45.22819289999998pt height=22.831056599999986pt/> and
<img src="/lm_course/LinearRegression/tex/6abdd5dfb79819fa50ccbdabc9c065b9.svg?invert_in_darkmode&sanitize=true" align=middle width=45.22819289999998pt height=22.831056599999986pt/>, so that <img src="/lm_course/LinearRegression/tex/509b732a5847eca7c3f9088fbdf48db2.svg?invert_in_darkmode&sanitize=true" align=middle width=69.22554374999999pt height=24.65753399999998pt/>. <br/>
B. Gradient descent is likely to get stuck at a local minimum and fail
to find the global minimum. <br/>
C. For this to be true, we must have <img src="/lm_course/LinearRegression/tex/499d6af654bef2b57024cad71dacd3aa.svg?invert_in_darkmode&sanitize=true" align=middle width=54.532866299999995pt height=29.190975000000005pt/> for every value of
<img src="/lm_course/LinearRegression/tex/bb59f5a1494e2d65f0800ff2d5aba6c3.svg?invert_in_darkmode&sanitize=true" align=middle width=105.0273345pt height=21.68300969999999pt/>. <br/>
D. Our training set can be fit perfectly by a straight line, i.e., all
of our training examples lie perfectly on some straight line.

6. Suppose <img src="/lm_course/LinearRegression/tex/20f63355b5530f35928590c69beae88a.svg?invert_in_darkmode&sanitize=true" align=middle width=44.56994024999999pt height=21.18721440000001pt/> students have taken some class, and the class had a
midterm exam and a final exam. You have collected a dataset of their
scores on the two exams, which is as follows. <br/>
You'd like to use polynomial regression to predict a student's final
exam score from their midterm exam score. Concretely, suppose you want
to fit a model of the form
<img src="/lm_course/LinearRegression/tex/d3c647562d2261be75017ae936ebbc9e.svg?invert_in_darkmode&sanitize=true" align=middle width=179.17975514999998pt height=24.65753399999998pt/>,
where <img src="/lm_course/LinearRegression/tex/6bd71d4c07531ce53dc5d08d0d7e1524.svg?invert_in_darkmode&sanitize=true" align=middle width=15.94753544999999pt height=14.15524440000002pt/> is the midterm score and <img src="/lm_course/LinearRegression/tex/aa0968eba9d0dd34149c2ae25c317f26.svg?invert_in_darkmode&sanitize=true" align=middle width=15.94753544999999pt height=14.15524440000002pt/> is (midterm score)^2.
Further, you plan to use both feature scaling (dividing by the
"max-min", or range, of a feature) and mean normalization. <br/>
What is the normalized feature x_1^{(1)}? (Please round off your answer
to two decimal places). <br/>
(-0.32)

<div align=center><img width="600" src="figure/8.png" alt=" "/></div>

7. You run gradient descent for 15 iterations with <img src="/lm_course/LinearRegression/tex/42fc5e9c1d9d12cecde3ea447dbd61f2.svg?invert_in_darkmode&sanitize=true" align=middle width=53.49877169999999pt height=21.18721440000001pt/> and
compute <img src="/lm_course/LinearRegression/tex/da87e8d6186f7c20976773c00d9edbef.svg?invert_in_darkmode&sanitize=true" align=middle width=31.655311049999987pt height=24.65753399999998pt/> after each iteration. You find that the value of
<img src="/lm_course/LinearRegression/tex/da87e8d6186f7c20976773c00d9edbef.svg?invert_in_darkmode&sanitize=true" align=middle width=31.655311049999987pt height=24.65753399999998pt/> decreases quickly then levels off. Based on this, which of
the following conclusions seems most plausible? <br/>
(B) <br/>
A. Rather than use the current value of <img src="/lm_course/LinearRegression/tex/ebb66f0e96fcb4a8d842166969b28831.svg?invert_in_darkmode&sanitize=true" align=middle width=10.57650494999999pt height=14.15524440000002pt/>, it'd be more
promising to try a smaller value of <img src="/lm_course/LinearRegression/tex/ebb66f0e96fcb4a8d842166969b28831.svg?invert_in_darkmode&sanitize=true" align=middle width=10.57650494999999pt height=14.15524440000002pt/> (say <img src="/lm_course/LinearRegression/tex/d87748c51ececf03145ce8b069615c5b.svg?invert_in_darkmode&sanitize=true" align=middle width=53.49877169999999pt height=21.18721440000001pt/>). <br/>
B. <img src="/lm_course/LinearRegression/tex/0269883810d93e33db190eb6532d9ab2.svg?invert_in_darkmode&sanitize=true" align=middle width=53.49877169999999pt height=21.18721440000001pt/> is an effective choice of learning rate. <br/>
C. Rather than use the current value of <img src="/lm_course/LinearRegression/tex/ebb66f0e96fcb4a8d842166969b28831.svg?invert_in_darkmode&sanitize=true" align=middle width=10.57650494999999pt height=14.15524440000002pt/>, it'd be more
promising to try a larger value of <img src="/lm_course/LinearRegression/tex/ebb66f0e96fcb4a8d842166969b28831.svg?invert_in_darkmode&sanitize=true" align=middle width=10.57650494999999pt height=14.15524440000002pt/> (say <img src="/lm_course/LinearRegression/tex/1240c3a779f22c634b158ca1f22f7f31.svg?invert_in_darkmode&sanitize=true" align=middle width=53.49877169999999pt height=21.18721440000001pt/>).

8. Suppose you have <img src="/lm_course/LinearRegression/tex/c2dd86acd048b6c7aafb9bf63fe0b162.svg?invert_in_darkmode&sanitize=true" align=middle width=52.789149599999995pt height=21.18721440000001pt/> training examples with <img src="/lm_course/LinearRegression/tex/2f3dcf27c85416c8521667d801620034.svg?invert_in_darkmode&sanitize=true" align=middle width=40.00371704999999pt height=21.18721440000001pt/> features
(excluding the additional all-ones feature for the intercept term, which
you should add). The normal equation is
<img src="/lm_course/LinearRegression/tex/2ccc4fa3697e1abfc7c62fad863a49e5.svg?invert_in_darkmode&sanitize=true" align=middle width=134.3524182pt height=27.6567522pt/>.
For the given values of <img src="/lm_course/LinearRegression/tex/7371e4a1b4ff766095a123b7f0023f5c.svg?invert_in_darkmode&sanitize=true" align=middle width=14.433101099999991pt height=14.15524440000002pt/> and <img src="/lm_course/LinearRegression/tex/1921941e267a38d161d9fcc7b3df9a61.svg?invert_in_darkmode&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/>, what are the dimensions of
<img src="/lm_course/LinearRegression/tex/6dc297c35dfa9049f077582466f9b777.svg?invert_in_darkmode&sanitize=true" align=middle width=8.17352744999999pt height=22.831056599999986pt/>, <img src="/lm_course/LinearRegression/tex/3de8619ca2ce4f12bb7c0459b17120c6.svg?invert_in_darkmode&sanitize=true" align=middle width=14.29216634999999pt height=22.55708729999998pt/>, and <img src="/lm_course/LinearRegression/tex/967155ddb61931e80889fb3f380279f5.svg?invert_in_darkmode&sanitize=true" align=middle width=10.239687149999991pt height=14.611878600000017pt/> in this equation? <br/>
(D) <br/>
A. <img src="/lm_course/LinearRegression/tex/3de8619ca2ce4f12bb7c0459b17120c6.svg?invert_in_darkmode&sanitize=true" align=middle width=14.29216634999999pt height=22.55708729999998pt/> is <img src="/lm_course/LinearRegression/tex/650972038a67ae0b43460b804ea7ba4a.svg?invert_in_darkmode&sanitize=true" align=middle width=44.748820049999985pt height=21.18721440000001pt/>, <img src="/lm_course/LinearRegression/tex/967155ddb61931e80889fb3f380279f5.svg?invert_in_darkmode&sanitize=true" align=middle width=10.239687149999991pt height=14.611878600000017pt/> is <img src="/lm_course/LinearRegression/tex/ceef8262bbf56d3d104ba9ff4a176bb5.svg?invert_in_darkmode&sanitize=true" align=middle width=44.748820049999985pt height=21.18721440000001pt/>,
<img src="/lm_course/LinearRegression/tex/6dc297c35dfa9049f077582466f9b777.svg?invert_in_darkmode&sanitize=true" align=middle width=8.17352744999999pt height=22.831056599999986pt/> is <img src="/lm_course/LinearRegression/tex/562075b7f61cb15bfbb7913f663b7c18.svg?invert_in_darkmode&sanitize=true" align=middle width=36.52961069999999pt height=21.18721440000001pt/>. <br/>
B. <img src="/lm_course/LinearRegression/tex/3de8619ca2ce4f12bb7c0459b17120c6.svg?invert_in_darkmode&sanitize=true" align=middle width=14.29216634999999pt height=22.55708729999998pt/> is <img src="/lm_course/LinearRegression/tex/65d3230bb845bab182c5ce85c580fee7.svg?invert_in_darkmode&sanitize=true" align=middle width=44.748820049999985pt height=21.18721440000001pt/>, <img src="/lm_course/LinearRegression/tex/967155ddb61931e80889fb3f380279f5.svg?invert_in_darkmode&sanitize=true" align=middle width=10.239687149999991pt height=14.611878600000017pt/> is <img src="/lm_course/LinearRegression/tex/65d3230bb845bab182c5ce85c580fee7.svg?invert_in_darkmode&sanitize=true" align=middle width=44.748820049999985pt height=21.18721440000001pt/>,
<img src="/lm_course/LinearRegression/tex/6dc297c35dfa9049f077582466f9b777.svg?invert_in_darkmode&sanitize=true" align=middle width=8.17352744999999pt height=22.831056599999986pt/> is <img src="/lm_course/LinearRegression/tex/e7e35f7c0c89e7b2b28ee0c666b4206b.svg?invert_in_darkmode&sanitize=true" align=middle width=36.52961069999999pt height=21.18721440000001pt/>. <br/>
C. <img src="/lm_course/LinearRegression/tex/3de8619ca2ce4f12bb7c0459b17120c6.svg?invert_in_darkmode&sanitize=true" align=middle width=14.29216634999999pt height=22.55708729999998pt/> is <img src="/lm_course/LinearRegression/tex/650972038a67ae0b43460b804ea7ba4a.svg?invert_in_darkmode&sanitize=true" align=middle width=44.748820049999985pt height=21.18721440000001pt/>, <img src="/lm_course/LinearRegression/tex/967155ddb61931e80889fb3f380279f5.svg?invert_in_darkmode&sanitize=true" align=middle width=10.239687149999991pt height=14.611878600000017pt/> is <img src="/lm_course/LinearRegression/tex/ceef8262bbf56d3d104ba9ff4a176bb5.svg?invert_in_darkmode&sanitize=true" align=middle width=44.748820049999985pt height=21.18721440000001pt/>,
<img src="/lm_course/LinearRegression/tex/6dc297c35dfa9049f077582466f9b777.svg?invert_in_darkmode&sanitize=true" align=middle width=8.17352744999999pt height=22.831056599999986pt/> is <img src="/lm_course/LinearRegression/tex/b9fe143e10b5f304bd52efdba6363ee8.svg?invert_in_darkmode&sanitize=true" align=middle width=36.52961069999999pt height=21.18721440000001pt/>. <br/>
D. <img src="/lm_course/LinearRegression/tex/3de8619ca2ce4f12bb7c0459b17120c6.svg?invert_in_darkmode&sanitize=true" align=middle width=14.29216634999999pt height=22.55708729999998pt/> is <img src="/lm_course/LinearRegression/tex/65d3230bb845bab182c5ce85c580fee7.svg?invert_in_darkmode&sanitize=true" align=middle width=44.748820049999985pt height=21.18721440000001pt/>, <img src="/lm_course/LinearRegression/tex/967155ddb61931e80889fb3f380279f5.svg?invert_in_darkmode&sanitize=true" align=middle width=10.239687149999991pt height=14.611878600000017pt/> is <img src="/lm_course/LinearRegression/tex/ceef8262bbf56d3d104ba9ff4a176bb5.svg?invert_in_darkmode&sanitize=true" align=middle width=44.748820049999985pt height=21.18721440000001pt/>,
<img src="/lm_course/LinearRegression/tex/6dc297c35dfa9049f077582466f9b777.svg?invert_in_darkmode&sanitize=true" align=middle width=8.17352744999999pt height=22.831056599999986pt/> is <img src="/lm_course/LinearRegression/tex/3c0c035f2dfe78d0b34ffbd0c53900aa.svg?invert_in_darkmode&sanitize=true" align=middle width=36.52961069999999pt height=21.18721440000001pt/>.

9. Suppose you have a dataset with <img src="/lm_course/LinearRegression/tex/8b181d3ba71967dc4065a5bf96c37ef0.svg?invert_in_darkmode&sanitize=true" align=middle width=52.789149599999995pt height=21.18721440000001pt/> examples and
<img src="/lm_course/LinearRegression/tex/f017d6848491ee5892643356f5921695.svg?invert_in_darkmode&sanitize=true" align=middle width=81.09976379999999pt height=21.18721440000001pt/> features for each example. You want to use multivariate
linear regression to fit the parameters <img src="/lm_course/LinearRegression/tex/6dc297c35dfa9049f077582466f9b777.svg?invert_in_darkmode&sanitize=true" align=middle width=8.17352744999999pt height=22.831056599999986pt/> to our data. Should
you prefer gradient descent or the normal equation? <br/>
(D) <br/>
A. The normal equation, since it provides an efficient way to directly
find the solution. <br/>
B. The normal equation, since gradient descent might be unable to find
the optimal <img src="/lm_course/LinearRegression/tex/6dc297c35dfa9049f077582466f9b777.svg?invert_in_darkmode&sanitize=true" align=middle width=8.17352744999999pt height=22.831056599999986pt/>. <br/>
C. Gradient descent, since it will always converge to the optimal
<img src="/lm_course/LinearRegression/tex/6dc297c35dfa9049f077582466f9b777.svg?invert_in_darkmode&sanitize=true" align=middle width=8.17352744999999pt height=22.831056599999986pt/>. <br/>
D. Gradient descent, since <img src="/lm_course/LinearRegression/tex/c4251b2a98a8ad72a96f0aa5495c9697.svg?invert_in_darkmode&sanitize=true" align=middle width=68.55192464999999pt height=27.6567522pt/> will be very
slow to compute in the normal equation.

10. Which of the following are reasons for using feature scaling? <br/>
(B) <br/>
A. It speeds up gradient descent by making each iteration of gradient
descent less expensive to compute. <br/>
B. It speeds up gradient descent by making it require fewer iterations
to get to a good solution. <br/>
C. It is necessary to prevent the normal equation from getting stuck
in local optima. <br/>
D. It prevents the matrix <img src="/lm_course/LinearRegression/tex/c4251b2a98a8ad72a96f0aa5495c9697.svg?invert_in_darkmode&sanitize=true" align=middle width=68.55192464999999pt height=27.6567522pt/> (used in the
normal equation) from being non-invertable (singular/degenerate).

## Exercise1
根据城市的人口来预测利润, 代码见[exercise1.py](exercise1.py).

[data1.txt](data1.txt)包含不同城市的数据, 第一列为城市的人口, 第二列为利润.
如下图.

<div align=center><img width="400" src="figure/ex1.png" alt=" "/></div>

采用梯度下降得到最优参数为: <img src="/lm_course/LinearRegression/tex/ddfad4d971eeabdf6c15ee44673604c3.svg?invert_in_darkmode&sanitize=true" align=middle width=167.07788294999997pt height=24.65753399999998pt/>.
利用该参数可以预测得到人口为35000时, 利润为40819.05.

将最优参数代入训练集进行拟合, 得到下图:

<div align=center><img width="400" src="figure/ex2.png" alt=" "/></div>

绘制代价函数随着参数<img src="/lm_course/LinearRegression/tex/2236187420fb2bfcf28d7dfd16ed31e1.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>和<img src="/lm_course/LinearRegression/tex/233284b1a493a6306b3660ec1885a6f2.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>变化的surface图和contour图如下.

<div align=center><img width="400" src="figure/ex3.png" alt=" "/></div>

<div align=center><img width="400" src="figure/ex4.png" alt=" "/></div>

## Exercise2
预测房屋售价, 代码见[exercise2.py](exercise2.py).

[data2.txt](data2.txt)包含不同房屋的售价, 第一列为房子的大小(平方米),
第二列为卧室的数量, 第三列为房屋的售价.

由于存在多个特征, 需要先对特征进行归一化. 注意需要保存归一化的均值和标准差参数,
在预测时也要使用相同的参数对特征进行归一化.

不同学习率代价函数曲线如下. 可以看出, 学习率较小时, 收敛速度较慢.

<div align=center><img width="400" src="figure/ex5.png" alt=" "/></div>

梯度下降得到的最优参数为: [340410.91897 109162.68848 -6293.24735].
房屋尺寸为1650, 卧室数量为3时, 梯度下降预测得到的房价: 293142.43.

采用Normal Equation得到的最优参数为: [89597.90954 139.21067 -8738.01911].
房屋尺寸为1650, 卧室数量为3时, 梯度下降预测得到的房价: 293081.46.

可以看出, 虽然梯度下降得到的参数与Normal Equation相差较大, 但是预测值非常接近.
