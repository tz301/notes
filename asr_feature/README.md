# [目录](../README.md)

# 语音特征

语音识别常用的特征包括FBank, MFCC等, 常见的变换包括Delta变换和CMVN变换.

## FBank和MFCC

FBank和MFCC特征有很多相似之处, MFCC在FBank的基础上做了进一步处理.
FBank特征提取的更多是音频信号的本质, 而MFCC则受限于一些机器学习算法,
在语音识别中广泛使用.

Fbank和MFCC均需要经过**预加重** - **分帧** - **加窗** - **傅里叶变化** - **梅尔滤波**这些流程.

### 预加重(Pre-Emphasis)

录制的语音信号通常会有频谱倾斜的现象, 即高频部分的幅度会比低频部分的小,
这通常与扬声器的频率响应有关.

预加重可以起到频谱平衡的作用, 增大高频的幅度. 预加重滤波器如下:

<p align="center"><img src="/asr_feature/tex/1f3bcd45e64153083e0c7c41636a32f5.svg?invert_in_darkmode&sanitize=true" align=middle width=168.4302741pt height=16.438356pt/></p>

对应的传递函数为:

<p align="center"><img src="/asr_feature/tex/50bcf551b16923cc2965deedd3354a74.svg?invert_in_darkmode&sanitize=true" align=middle width=122.1517374pt height=18.312383099999998pt/></p>

对于语音识别来说, <img src="/asr_feature/tex/ebb66f0e96fcb4a8d842166969b28831.svg?invert_in_darkmode&sanitize=true" align=middle width=10.57650494999999pt height=14.15524440000002pt/>通常取值0.97.

预加重可以起到频谱平衡的作用, 同时可以提升信噪比.
但是也会引入额外的边缘效应, 对于多通道而言, 可能由于边缘不一致导致串扰等问题.

### 分帧(Framing)

很多信号处理算法要求信号的平稳性, 而语音信号是非平稳的. 将信号分帧后,
可以近似认为一帧内的信号是平稳的. 为了避免信号突变, 分帧会存在一定重叠.

对于语音识别来说, 帧长和帧移的选取主要考虑音素的可区分性.
通常取帧长25ms, 帧移10ms, 即0 \~ 25ms为第一帧, 10 \~ 35ms为第二帧.

### 加窗(Window)

分帧后, 需要对每帧的信号进行加窗.

实际上, 分帧相当于加了矩形窗. 为了进行傅里叶变换, 需要经过周期延拓得到无限长信号,
完成傅里叶变换后通过低通滤波器获取指定频率区间的频谱图. 那么在对信号进行截断时,
频谱就发生了畸变. 原来集中在<img src="/asr_feature/tex/bd0eb9ccc03ec3af49c481bc4c369061.svg?invert_in_darkmode&sanitize=true" align=middle width=18.03662189999999pt height=22.831056599999986pt/>处的能量会分散到旁瓣, 也就是频谱泄漏.

因此需要好的窗函数, 来减少频谱泄漏. 例如常用的Hamming窗:

<p align="center"><img src="/asr_feature/tex/0f1f87f45fe91bc720fbb6678493e4b7.svg?invert_in_darkmode&sanitize=true" align=middle width=349.4069502pt height=39.452455349999994pt/></p>

<div align=center><img width="450" src="figure/1.png" alt=" "/></div>

### 傅里叶变换(Fourier Transform)

对每一帧进行短时傅里叶变换, 并对幅值求平方得到功率谱.

<p align="center"><img src="/asr_feature/tex/b8827d2a89167057d294dcd22040c703.svg?invert_in_darkmode&sanitize=true" align=middle width=118.48419329999999pt height=38.07696255pt/></p>

### 梅尔滤波(Mel Filter Banks)

人耳的听觉在频域上是非线性的, 更容易区分低频的声音, 而对高频声音的区分度更低,
不同频率的声音听感也不一样. 参考如下的等响曲线.

<div align=center><img width="450" src="figure/2.png" alt=" "/></div>

梅尔刻度的目的就是模拟人耳听觉的非线性关系. 梅尔刻度<img src="/asr_feature/tex/7371e4a1b4ff766095a123b7f0023f5c.svg?invert_in_darkmode&sanitize=true" align=middle width=14.433101099999991pt height=14.15524440000002pt/>和频率<img src="/asr_feature/tex/79986cadd9fb05185bb29bf10739134b.svg?invert_in_darkmode&sanitize=true" align=middle width=9.81741584999999pt height=22.831056599999986pt/>的关系如下:

<p align="center"><img src="/asr_feature/tex/49513de4292e916763af0dee11d7046e.svg?invert_in_darkmode&sanitize=true" align=middle width=188.0454378pt height=39.452455349999994pt/></p>

<p align="center"><img src="/asr_feature/tex/e699b5bec139c89e89eb2bef096018bb.svg?invert_in_darkmode&sanitize=true" align=middle width=168.9480012pt height=29.58934275pt/></p>

梅尔滤波器组如下, 每个滤波器在中心频率处幅值为1, 呈三角滤波的形式. 具体如下:

<p align="center"><img src="/asr_feature/tex/427c10a537b12a073a6605e49bae080d.svg?invert_in_darkmode&sanitize=true" align=middle width=386.83524825pt height=159.86165909999997pt/></p>

<div align=center><img width="450" src="figure/3.png" alt=" "/></div>

### FBank

将上述获取的功率谱通过梅尔滤波器组进行滤波, 就得到了FBank特征.

### MFCC

MFCC的流程通常为: FBank - 取log - DCT - 倒谱加权.

由于FBank特征系数之间是高度相关的, 采用DCT对FBank去相关化, 同时也可以实现压缩.

DCT拥有多种形式, 常用的DCT-II如下:

<p align="center"><img src="/asr_feature/tex/29356b8339fc408fc95f1d377d706325.svg?invert_in_darkmode&sanitize=true" align=middle width=221.3268915pt height=47.60747145pt/></p>

倒谱加权的作用主要是增加高频成分, 如下:

<p align="center"><img src="/asr_feature/tex/90422291412e8c04037d1c1b952730c8.svg?invert_in_darkmode&sanitize=true" align=middle width=227.39063984999999pt height=33.81208709999999pt/></p>
