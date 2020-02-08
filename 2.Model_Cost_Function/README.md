# [目录](../README.md)

# Model and Cost Function

## 符号定义
对于回归问题, 假设有一堆训练集, 记: <br/>
<img src="/2.Model_Cost_Function/tex/0e51a2dede42189d77627c4d742822c3.svg?invert_in_darkmode&sanitize=true" align=middle width=14.433101099999991pt height=14.15524440000002pt/> - 训练集的样本数量 <br/>
<img src="/2.Model_Cost_Function/tex/eb498af51d4103488bf6cb749bdce12e.svg?invert_in_darkmode&sanitize=true" align=middle width=15.599359049999991pt height=14.15524440000002pt/> - 输入变量/特征 <br/>
<img src="/2.Model_Cost_Function/tex/dd7f27a66a7dfa15c57c2fc06b8d49c4.svg?invert_in_darkmode&sanitize=true" align=middle width=14.26380119999999pt height=14.15524440000002pt/> - 输出变量/目标变量 <br/>
<img src="/2.Model_Cost_Function/tex/81277d3368f07d957253e7c28a3e5774.svg?invert_in_darkmode&sanitize=true" align=middle width=38.135511149999985pt height=24.65753399999998pt/> - 一个样本对 <br/>
<img src="/2.Model_Cost_Function/tex/9a9ed1968ddefaa8d6f1635e03f6c72b.svg?invert_in_darkmode&sanitize=true" align=middle width=69.62915025pt height=29.190975000000005pt/> - 第i个样本对 <br/>

## Model Representation

学习算法通过对训练数据的学习来获取模型<img src="/2.Model_Cost_Function/tex/f79ff4ffc0429ece3cfe30e85017e634.svg?invert_in_darkmode&sanitize=true" align=middle width=76.84518929999999pt height=22.831056599999986pt/>, 也称作hypothesis. 在预测阶段, 将<img src="/2.Model_Cost_Function/tex/332cc365a4987aacce0ead01b8bdcc0b.svg?invert_in_darkmode&sanitize=true" align=middle width=9.39498779999999pt height=14.15524440000002pt/>输入模型<img src="/2.Model_Cost_Function/tex/2ad9d098b937e46f9f58968551adac57.svg?invert_in_darkmode&sanitize=true" align=middle width=9.47111549999999pt height=22.831056599999986pt/>得到预测的<img src="/2.Model_Cost_Function/tex/deceeaf6940a8c7a5a02373728002b0f.svg?invert_in_darkmode&sanitize=true" align=middle width=8.649225749999989pt height=14.15524440000002pt/>.
<div align=center><img width="150" height="150" src="1.png"/>

## Quiz

