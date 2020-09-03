import matplotlib.pyplot as plt
import numpy as np
import this
plt.style.use('seaborn-whitegrid')
x=np.random.randn(100)
y=np.random.randn(100) #从标准正态分布中返回一个或多个样本值
colors=np.random.rand(100) #随机样本位于[0,1)中
sizes=1000 * np.random.rand(100)
plt.scatter(x,y,c=colors,s=sizes,alpha=0.4)
plt.colorbar()
plt.show()