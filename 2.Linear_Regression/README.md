# [目录](../README.md)

# Linear Regression

## Definition
对于回归问题, 假设有一堆训练集, 记:
* <img src="/2.Linear_Regression/tex/0e51a2dede42189d77627c4d742822c3.svg?invert_in_darkmode&sanitize=true" align=middle width=14.433101099999991pt height=14.15524440000002pt/> - 训练集的样本数量
* <img src="/2.Linear_Regression/tex/eb498af51d4103488bf6cb749bdce12e.svg?invert_in_darkmode&sanitize=true" align=middle width=15.599359049999991pt height=14.15524440000002pt/> - 输入变量/特征
* <img src="/2.Linear_Regression/tex/dd7f27a66a7dfa15c57c2fc06b8d49c4.svg?invert_in_darkmode&sanitize=true" align=middle width=14.26380119999999pt height=14.15524440000002pt/> - 输出变量/目标变量
* <img src="/2.Linear_Regression/tex/81277d3368f07d957253e7c28a3e5774.svg?invert_in_darkmode&sanitize=true" align=middle width=38.135511149999985pt height=24.65753399999998pt/> - 一个样本对
* <img src="/2.Linear_Regression/tex/9a9ed1968ddefaa8d6f1635e03f6c72b.svg?invert_in_darkmode&sanitize=true" align=middle width=69.62915025pt height=29.190975000000005pt/> - 第<img src="/2.Linear_Regression/tex/77a3b857d53fb44e33b53e4c8b68351a.svg?invert_in_darkmode&sanitize=true" align=middle width=5.663225699999989pt height=21.68300969999999pt/>个样本对

## Model Representation
学习算法通过对训练数据的学习来获取模型<img src="/2.Linear_Regression/tex/f79ff4ffc0429ece3cfe30e85017e634.svg?invert_in_darkmode&sanitize=true" align=middle width=76.84518929999999pt height=22.831056599999986pt/>, 也称作hypothesis.
在预测阶段, 将<img src="/2.Linear_Regression/tex/332cc365a4987aacce0ead01b8bdcc0b.svg?invert_in_darkmode&sanitize=true" align=middle width=9.39498779999999pt height=14.15524440000002pt/>输入模型<img src="/2.Linear_Regression/tex/2ad9d098b937e46f9f58968551adac57.svg?invert_in_darkmode&sanitize=true" align=middle width=9.47111549999999pt height=22.831056599999986pt/>得到预测的<img src="/2.Linear_Regression/tex/deceeaf6940a8c7a5a02373728002b0f.svg?invert_in_darkmode&sanitize=true" align=middle width=8.649225749999989pt height=14.15524440000002pt/>.
<div align=center><img width="250" src="1.png" alt=" "/></div>

## Cost Function
我们可以采用代价函数来评估模型的准确性.

假设模型为:
<p align="center"><img src="/2.Linear_Regression/tex/e33503194166872d1917d512b6a503ed.svg?invert_in_darkmode&sanitize=true" align=middle width=120.67521674999999pt height=16.438356pt/></p>

其中, <img src="/2.Linear_Regression/tex/1a3151e36f9f52b61f5bf76c08bdae2b.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>和<img src="/2.Linear_Regression/tex/edcbf8dd6dd9743cceeee21183bbc3b6.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>是待定参数, 不同的参数得到的模型也不同.

目标是选取最好的<img src="/2.Linear_Regression/tex/1a3151e36f9f52b61f5bf76c08bdae2b.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>和<img src="/2.Linear_Regression/tex/edcbf8dd6dd9743cceeee21183bbc3b6.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>, 使得模型对训练集的拟合程度较好,
即<img src="/2.Linear_Regression/tex/b687e9cb7f5356da0e24f1b1cac73585.svg?invert_in_darkmode&sanitize=true" align=middle width=39.088702949999984pt height=24.65753399999998pt/>尽可能与<img src="/2.Linear_Regression/tex/deceeaf6940a8c7a5a02373728002b0f.svg?invert_in_darkmode&sanitize=true" align=middle width=8.649225749999989pt height=14.15524440000002pt/>接近, 那么可以将代价函数写成:
<p align="center"><img src="/2.Linear_Regression/tex/12ef58af70bc9706323e22259bae3ab3.svg?invert_in_darkmode&sanitize=true" align=middle width=254.63021925pt height=44.89738935pt/></p>

因此, 目标就转化为最小化代价函数:
<p align="center"><img src="/2.Linear_Regression/tex/c64a73c550872589c715e7dcfa181e52.svg?invert_in_darkmode&sanitize=true" align=middle width=93.67323404999999pt height=25.2967704pt/></p>

可以将代价函数对<img src="/2.Linear_Regression/tex/1a3151e36f9f52b61f5bf76c08bdae2b.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>和<img src="/2.Linear_Regression/tex/edcbf8dd6dd9743cceeee21183bbc3b6.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>求偏导并等于0, 从而得到最优的参数.

## Gradient Descent
给定不同的参数<img src="/2.Linear_Regression/tex/1a3151e36f9f52b61f5bf76c08bdae2b.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>和<img src="/2.Linear_Regression/tex/edcbf8dd6dd9743cceeee21183bbc3b6.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>, 得到的代价函数值也不一样,
可以将代价函数随着参数变化的曲面绘制出来. 代价函数最小的点, 也就是曲线上最低的点,
此时的参数就是最优模型. 给定初始的参数<img src="/2.Linear_Regression/tex/1a3151e36f9f52b61f5bf76c08bdae2b.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>和<img src="/2.Linear_Regression/tex/edcbf8dd6dd9743cceeee21183bbc3b6.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>,
采用梯度下降算法对参数不断更新, 在曲面上不断"下山", 直到最低点得到最优的参数.

<div align=center><img width="400" src="2.png" alt=" "/></div>

梯度下降算法:
<p align="center"><img src="/2.Linear_Regression/tex/06aadd9fa723f94f19e6606049467ef5.svg?invert_in_darkmode&sanitize=true" align=middle width=241.79507715pt height=38.5152603pt/></p>

上式中, <img src="/2.Linear_Regression/tex/c745b9b57c145ec5577b82542b2df546.svg?invert_in_darkmode&sanitize=true" align=middle width=10.57650494999999pt height=14.15524440000002pt/>称作学习率. 如果学习率较大, 梯度下降就会采用较大的步长下降;
如果学习率较小, 梯度下降就会采用较小的步长下降.

## Learning Rate
学习率太小, 梯度下降速度可能会很慢.

学习率太大, 梯度下降可能错误局部最优点, 可能不会收敛, 甚至发散.

<div align=center><img width="250" src="3.png" alt=" "/></div>

如果达到最优点, 此时梯度下降算法再更新, 参数就不会再发生变化.

<div align=center><img width="300" src="4.png" alt=" "/></div>

由于梯度下降过程中, 梯度项会不断减小, 因此, 即时学习率固定, 也可以收敛到局部最优.

## Gradient Descent For Linear Regression
将线性回归的模型代入梯度下降的公式, 偏导项变为:
<p align="center"><img src="/2.Linear_Regression/tex/d30868dbef07d533e81f25daf74bfb06.svg?invert_in_darkmode&sanitize=true" align=middle width=576.1502075999999pt height=44.89738935pt/></p>

可以求出<img src="/2.Linear_Regression/tex/2d72a911a19b952b476268360c3d83be.svg?invert_in_darkmode&sanitize=true" align=middle width=37.84725779999999pt height=21.68300969999999pt/>和<img src="/2.Linear_Regression/tex/808d7610d22dae56fe8166a58e9f8c92.svg?invert_in_darkmode&sanitize=true" align=middle width=37.84725779999999pt height=21.68300969999999pt/>时的偏导项为:
<p align="center"><img src="/2.Linear_Regression/tex/d54a38ace526553d735e68db97a3b04d.svg?invert_in_darkmode&sanitize=true" align=middle width=559.48138455pt height=80.0153376pt/></p>

## Quiz
