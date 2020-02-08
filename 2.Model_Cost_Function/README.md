# [目录](../README.md)

# Model and Cost Function

## Definition
对于回归问题, 假设有一堆训练集, 记: <br/>
<img src="/2.Model_Cost_Function/tex/0e51a2dede42189d77627c4d742822c3.svg?invert_in_darkmode&sanitize=true" align=middle width=14.433101099999991pt height=14.15524440000002pt/> - 训练集的样本数量 <br/>
<img src="/2.Model_Cost_Function/tex/eb498af51d4103488bf6cb749bdce12e.svg?invert_in_darkmode&sanitize=true" align=middle width=15.599359049999991pt height=14.15524440000002pt/> - 输入变量/特征 <br/>
<img src="/2.Model_Cost_Function/tex/dd7f27a66a7dfa15c57c2fc06b8d49c4.svg?invert_in_darkmode&sanitize=true" align=middle width=14.26380119999999pt height=14.15524440000002pt/> - 输出变量/目标变量 <br/>
<img src="/2.Model_Cost_Function/tex/81277d3368f07d957253e7c28a3e5774.svg?invert_in_darkmode&sanitize=true" align=middle width=38.135511149999985pt height=24.65753399999998pt/> - 一个样本对 <br/>
<img src="/2.Model_Cost_Function/tex/9a9ed1968ddefaa8d6f1635e03f6c72b.svg?invert_in_darkmode&sanitize=true" align=middle width=69.62915025pt height=29.190975000000005pt/> - 第<img src="/2.Model_Cost_Function/tex/77a3b857d53fb44e33b53e4c8b68351a.svg?invert_in_darkmode&sanitize=true" align=middle width=5.663225699999989pt height=21.68300969999999pt/>个样本对 <br/>

## Model Representation
学习算法通过对训练数据的学习来获取模型<img src="/2.Model_Cost_Function/tex/f79ff4ffc0429ece3cfe30e85017e634.svg?invert_in_darkmode&sanitize=true" align=middle width=76.84518929999999pt height=22.831056599999986pt/>, 也称作hypothesis.
在预测阶段, 将<img src="/2.Model_Cost_Function/tex/332cc365a4987aacce0ead01b8bdcc0b.svg?invert_in_darkmode&sanitize=true" align=middle width=9.39498779999999pt height=14.15524440000002pt/>输入模型<img src="/2.Model_Cost_Function/tex/2ad9d098b937e46f9f58968551adac57.svg?invert_in_darkmode&sanitize=true" align=middle width=9.47111549999999pt height=22.831056599999986pt/>得到预测的<img src="/2.Model_Cost_Function/tex/deceeaf6940a8c7a5a02373728002b0f.svg?invert_in_darkmode&sanitize=true" align=middle width=8.649225749999989pt height=14.15524440000002pt/>. <br/>
<div align=center><img width="150" height="150" src="1.png"/></div>

## Cost Function
代价函数指导了模型拟合的方向. <br/>
假设模型为: <br/>
<div align=center><p align="center"><img src="/2.Model_Cost_Function/tex/ab3fbf9c981f774b779b68f7d1a26f87.svg?invert_in_darkmode&sanitize=true" align=middle width=120.67521674999999pt height=16.438356pt/></p></div> <br/>
<img src="/2.Model_Cost_Function/tex/1a3151e36f9f52b61f5bf76c08bdae2b.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>和<img src="/2.Model_Cost_Function/tex/edcbf8dd6dd9743cceeee21183bbc3b6.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/> <br/><br/>

其中, <img src="/2.Model_Cost_Function/tex/1a3151e36f9f52b61f5bf76c08bdae2b.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>和<img src="/2.Model_Cost_Function/tex/edcbf8dd6dd9743cceeee21183bbc3b6.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>是待定参数, 不同的参数得到的模型也不同. <br/><br/>
目标是选取最好的<img src="/2.Model_Cost_Function/tex/1a3151e36f9f52b61f5bf76c08bdae2b.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>和<img src="/2.Model_Cost_Function/tex/edcbf8dd6dd9743cceeee21183bbc3b6.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>, 使得模型对训练集的拟合程度较好, 即
<img src="/2.Model_Cost_Function/tex/b687e9cb7f5356da0e24f1b1cac73585.svg?invert_in_darkmode&sanitize=true" align=middle width=39.088702949999984pt height=24.65753399999998pt/>尽可能与<img src="/2.Model_Cost_Function/tex/deceeaf6940a8c7a5a02373728002b0f.svg?invert_in_darkmode&sanitize=true" align=middle width=8.649225749999989pt height=14.15524440000002pt/>接近, 那么可以将代价函数写成: <br/>
<div align=center><p align="center"><img src="/2.Model_Cost_Function/tex/de24dc32227abc0f328a46919746502f.svg?invert_in_darkmode&sanitize=true" align=middle width=254.63021925pt height=44.89738935pt/></p></div> <br/>
目标就是最小化代价函数
<div align=center><p align="center"><img src="/2.Model_Cost_Function/tex/8b139a91423a7b4f189ad0f17ab28c3d.svg?invert_in_darkmode&sanitize=true" align=middle width=135.45454064999998pt height=25.2967704pt/></p></div> <br/><br/>
可以将代价函数对<img src="/2.Model_Cost_Function/tex/1a3151e36f9f52b61f5bf76c08bdae2b.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>和<img src="/2.Model_Cost_Function/tex/edcbf8dd6dd9743cceeee21183bbc3b6.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>求偏导并等于0, 从而得到最优的参数.<br/>

可以将代价函数对<img src="/2.Model_Cost_Function/tex/1a3151e36f9f52b61f5bf76c08bdae2b.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>和<img src="/2.Model_Cost_Function/tex/edcbf8dd6dd9743cceeee21183bbc3b6.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>求偏导并等于0, 从而得到最优的参数.<br/>
<img src="/2.Model_Cost_Function/tex/1a3151e36f9f52b61f5bf76c08bdae2b.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/> and <img src="/2.Model_Cost_Function/tex/edcbf8dd6dd9743cceeee21183bbc3b6.svg?invert_in_darkmode&sanitize=true" align=middle width=14.269439249999989pt height=22.831056599999986pt/>

## Quiz
