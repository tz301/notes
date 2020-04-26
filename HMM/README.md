# [目录](../README.md)

# Hidden Markov Models

## Markov Chains

马尔科夫链, 是状态空间中从一个状态到另一个状态转换的随机过程.
对于马尔科夫链, 如果要从一个序列进行预测, 当前状态起到决定的作用,
历史状态对于预测没有影响.

假设一个序列内的状态变量为<img src="/HMM/tex/e637b86bbdb2aacea366b27626449b0a.svg?invert_in_darkmode&sanitize=true" align=middle width=87.98971334999999pt height=14.611911599999981pt/>. 可以将马尔可夫假设表示为:

<img src="/HMM/tex/a71e51aa5270f06bd78929a1e2fa9c18.svg?invert_in_darkmode&sanitize=true" align=middle width=267.77565375pt height=24.65753399999998pt/>

