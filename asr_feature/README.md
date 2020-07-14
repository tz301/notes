# [目录](../README.md)

# 语音特征

语音识别常用的特征包括FBank, MFCC, Pitch等, 常见的变换包括Delta变换和CMVN变换.

## FBank和MFCC

FBank和MFCC特征有很多相似之处, MFCC在FBank的基础上做了进一步处理.
FBank特征提取的更多是音频信号的本质, 而MFCC则受限于一些机器学习算法,
在语音识别中广泛使用.

Fbank特征的提取流程为:
1. 预加重.
2. 分帧.
3. 加窗.
4. 傅里叶变换.
5. 梅尔滤波.

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

倒谱加权的作用主要是增加高频成分. 例如MFCC为<img src="/asr_feature/tex/5e9c7a7d16b15ab5b947bedf5f56bd79.svg?invert_in_darkmode&sanitize=true" align=middle width=14.99998994999999pt height=22.465723500000017pt/>阶, 加权系数为<img src="/asr_feature/tex/6e75432f3e00dc52c8ba25566dcdf692.svg?invert_in_darkmode&sanitize=true" align=middle width=11.18724254999999pt height=22.465723500000017pt/>阶,
倒谱加权为:

<p align="center"><img src="/asr_feature/tex/f5765e5fb318777e71a76d274cb49e92.svg?invert_in_darkmode&sanitize=true" align=middle width=238.71684209999998pt height=33.62942055pt/></p>

## Pitch

Pitch特征提取就是计算声音基频F0的过程.

如果一个复杂信号和一个可变频率的正弦波在音调上听感一致,
那么正弦波的频率就是复杂信号的pitch.

Pitch特征的提取有多种方法, 例如:
1. Yin: Alain De Cheveign´e and Hideki Kawahara, “Yin, a fundamen- tal frequency estimator for speech and music,” The Journal of the Acoustical Society ofAmerica, vol. 111, pp. 1917, 2002.
2. Getf0: David Talkin, “A robust algorithm for pitch tracking (rapt),” Speech coding and synthesis, vol. 495, pp. 518, 1995.
3. SAcC: Daniel PWEllis and Byunk Suk Lee, “Noise robust pitch track- ing by subband autocorrelation classification,” in 13th Annual Conference of the International Speech Communication Asso- ciation, 2012.
4. Wu: M. Wu, D.L. Wang, and G.J. Brown, “A multipitch tracking algorithm for noisy speech,” IEEETransactions on Speech and Audio Processing, vol. 11, no. 3, pp. 229–241, 2003.
5. SWIPE: A. Camacho and J. G. Harris, “A sawtooth waveform inspired pitch estimator for speech and music,” Journal of the Acousti- cal Society ofAmerica, vol. 124, no. 3, pp. 1638–1652, 2008.
6. YAAPT: Kavita Kasi and Stephen A Zahorian, “Yet another algorithm for pitch tracking,” in Acoustics, Speech, and Signal Process- ing (ICASSP), 2002 IEEE International Conference on. IEEE, 2002, vol. 1, pp. I–361.

下面主要参考kaldi pitch: Ghahremani P, BabaAli B, Povey D, et al. A pitch extraction algorithm tuned for automatic speech recognition[C]//2014 IEEE international conference on acoustics, speech and signal processing (ICASSP). IEEE, 2014: 2494-2498.

kaldi pitch没有对每一帧是否为人声进行判断,
而是对每一帧都计算pitch, 使得pitch是一个连续的值, 更加符合语音识别任务.
主要提取流程如下:
1. 重采样.
2. 归一化.
3. NCCF(Normalized Cross Correlation Function)计算.
4. NCCF上采样.

### 重采样

假设采样后信号<img src="/asr_feature/tex/1e1cd67f38bd36937fd1b33d0685bf3b.svg?invert_in_darkmode&sanitize=true" align=middle width=26.42701049999999pt height=24.65753399999998pt/>, 第<img src="/asr_feature/tex/1921941e267a38d161d9fcc7b3df9a61.svg?invert_in_darkmode&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/>个采样点<img src="/asr_feature/tex/168fb4eddcc5ed7b56677c5f09164b7f.svg?invert_in_darkmode&sanitize=true" align=middle width=17.521011749999992pt height=14.15524440000002pt/>可以看作<img src="/asr_feature/tex/fae4aefa3cdb3111d870132c7fc739ef.svg?invert_in_darkmode&sanitize=true" align=middle width=29.11348769999999pt height=24.65753399999998pt/>时刻的 <img src="/asr_feature/tex/f4a02e5afd3c51c34036863474c11e94.svg?invert_in_darkmode&sanitize=true" align=middle width=7.928075099999989pt height=22.831056599999986pt/>函数,
<img src="/asr_feature/tex/dee3f05776ccbc001bd3e363130afa0a.svg?invert_in_darkmode&sanitize=true" align=middle width=11.027402099999989pt height=22.465723500000017pt/>为采样频率.

定义滤波函数<img src="/asr_feature/tex/ae25d802dc4a8c6ca74eb002dd324c33.svg?invert_in_darkmode&sanitize=true" align=middle width=50.841565499999994pt height=24.65753399999998pt/>, 参数<img src="/asr_feature/tex/899152ab9dec1c3edd956dafb93febfb.svg?invert_in_darkmode&sanitize=true" align=middle width=61.39482524999998pt height=24.65753399999998pt/>表示截止频率, 窗宽<img src="/asr_feature/tex/8d6a6623dff6c3c697210c8a29078c5c.svg?invert_in_darkmode&sanitize=true" align=middle width=42.347685599999984pt height=21.18721440000001pt/>.

选取Hanning窗函数<img src="/asr_feature/tex/337713b725c1d8b85dd4180055cd53c3.svg?invert_in_darkmode&sanitize=true" align=middle width=30.93237674999999pt height=24.65753399999998pt/>, 定义滤波函数为:

<p align="center"><img src="/asr_feature/tex/37a6200bd5daba15804b306fc55cdaea.svg?invert_in_darkmode&sanitize=true" align=middle width=312.55079789999996pt height=39.452455349999994pt/></p>

其中, <img src="/asr_feature/tex/4c92b0bf040bc45da3c7ba431e843372.svg?invert_in_darkmode&sanitize=true" align=middle width=30.34938719999999pt height=21.68300969999999pt/>为归一化的sinc函数.

对于任意时刻<img src="/asr_feature/tex/99d32c17b0344b01c18cce1e210642dc.svg?invert_in_darkmode&sanitize=true" align=middle width=5.936097749999991pt height=20.221802699999984pt/>, 计算窗内所有输入信号加窗后的数值之和, 得到重采样后的信号:

<p align="center"><img src="/asr_feature/tex/ef9f32570d3577feaa94bdd3a6fa4f72.svg?invert_in_darkmode&sanitize=true" align=middle width=199.80226365pt height=42.353648699999994pt/></p>

### 归一化.

将重采样后的信号除以均方值进行归一化.

### NCCF计算.

互相关(Cross Correlation Function, CCF)一般用来度量两个量之间的相似度,
它是一个向量相对于另一个向量的偏移的函数, 也叫滑动内积.
而自相关(Auto Correlation Function, ACF)就是信号自身与自身的互相关.

自相关函数在波形重合处会出现峰值, 因此可以用来计算序列中的重复模式, 即基频.
通过计算不同偏移处的自相关, 找到峰值处的偏移值.

对于ACF和CCF, 偏移越大, 计算的序列就越短, 那么不同偏移处的数值是无法比较的.
而NCCF通过归一化使得不同偏移处的数值可以比较.

为了寻找能够最大化NCCF的偏移, 先定义计算偏移的区间.

定义<img src="/asr_feature/tex/a63a4877971e55b6902dddb7f39039fb.svg?invert_in_darkmode&sanitize=true" align=middle width=273.87131145pt height=24.65753399999998pt/>为计算NCCF的lag区间,
采用非线性的方式获取偏移值:

<p align="center"><img src="/asr_feature/tex/127e93e3dbd59b2fa1407d64d3a3e1c5.svg?invert_in_darkmode&sanitize=true" align=middle width=312.73628925pt height=20.582203949999997pt/></p>

定义滤波宽度<img src="/asr_feature/tex/e0d75638341aaa771a47999137d21473.svg?invert_in_darkmode&sanitize=true" align=middle width=12.210846449999991pt height=14.15524440000002pt/>, 那么输出的lag区间为:
<p align="center"><img src="/asr_feature/tex/3b9fdc96e9b62529563a849e2511a7a5.svg?invert_in_darkmode&sanitize=true" align=middle width=417.4539567pt height=17.031940199999998pt/></p>

这样可以在更大的偏移区间内计算NCCF.

对于帧索引<img src="/asr_feature/tex/99d32c17b0344b01c18cce1e210642dc.svg?invert_in_darkmode&sanitize=true" align=middle width=5.936097749999991pt height=20.221802699999984pt/>, 需要处理的信号从<img src="/asr_feature/tex/09367ca11f67c9fe997c850dad2307f7.svg?invert_in_darkmode&sanitize=true" align=middle width=105.05850299999999pt height=22.831056599999986pt/>开始,
长度为<img src="/asr_feature/tex/8307c4010326377822c07bf42b470f4a.svg?invert_in_darkmode&sanitize=true" align=middle width=194.75435594999996pt height=22.831056599999986pt/>.
定义<img src="/asr_feature/tex/99d32c17b0344b01c18cce1e210642dc.svg?invert_in_darkmode&sanitize=true" align=middle width=5.936097749999991pt height=20.221802699999984pt/>帧的信号为<img src="/asr_feature/tex/0e3b38cebcddb24629c054e3f7bab79f.svg?invert_in_darkmode&sanitize=true" align=middle width=146.69875605pt height=24.65753399999998pt/>,
<img src="/asr_feature/tex/7630609e2cb723f1b61986af92b8ffff.svg?invert_in_darkmode&sanitize=true" align=middle width=23.49794039999999pt height=14.611878600000017pt/>为<img src="/asr_feature/tex/f5cb86ce54122626240d4bd0d88caf96.svg?invert_in_darkmode&sanitize=true" align=middle width=18.61868744999999pt height=14.611878600000017pt/>内从<img src="/asr_feature/tex/8fceb32bd3f6803b77bbe1b1758a60b6.svg?invert_in_darkmode&sanitize=true" align=middle width=5.663225699999989pt height=21.68300969999999pt/>开始, 长度为<img src="/asr_feature/tex/2c3e207f73aa48f312f612513b1c0e8d.svg?invert_in_darkmode&sanitize=true" align=middle width=90.00856589999998pt height=22.831056599999986pt/>
的子序列.

那么可以得到第<img src="/asr_feature/tex/99d32c17b0344b01c18cce1e210642dc.svg?invert_in_darkmode&sanitize=true" align=middle width=5.936097749999991pt height=20.221802699999984pt/>帧, 第<img src="/asr_feature/tex/6361dd721b68dd339b33b2652c0abd4b.svg?invert_in_darkmode&sanitize=true" align=middle width=5.2283516999999895pt height=22.831056599999986pt/>个偏移处的NCCF为:

<p align="center"><img src="/asr_feature/tex/91b4c33b10389e0b3cf207f7848f2396.svg?invert_in_darkmode&sanitize=true" align=middle width=273.643392pt height=45.132167849999995pt/></p>

其中, <img src="/asr_feature/tex/1921941e267a38d161d9fcc7b3df9a61.svg?invert_in_darkmode&sanitize=true" align=middle width=9.86687624999999pt height=14.15524440000002pt/>为窗内的样本数, 降低ballest有利于非人声区域pitch计算的连续性.

### NCCF上采样
