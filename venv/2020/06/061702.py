import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.rcParams['font.sans-serif']=['SimHei'] #黑体显示中文
matplotlib.rcParams['axes.unicode_minus']=False #正常显示负号
data=np.random.randn(10000)
'''
data:必选参数，绘图数据
bins:直方图的长条形数目，可选项，默认为10
normed:是否将得到的直方图向量归一化，可选项，默认为0，代表不归一化，显示频数。normed=1，表示归一化，显示频率。
facecolor:长条形的颜色
edgecolor:长条形边框的颜色
alpha:透明度
————————————————
版权声明：本文为CSDN博主「zxhohai」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/hohaizx/article/details/79101322
'''
plt.hist(data,bins=40,facecolor='blue',edgecolor='black',alpha=0.7)
#显示横轴标签
plt.xlabel("区间")
#显示纵轴标签
plt.ylabel("频数/频率")
#显示图标题
plt.title("频数/频率分布直方图")
plt.show()
