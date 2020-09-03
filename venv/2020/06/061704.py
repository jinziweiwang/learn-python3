import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
df=pd.DataFrame(np.random.rand(1000,2).cumsum(0),columns=['a','b'])
#bar 条形图
#df.plot.bar()
#box绘图
#df.plot.box()
#Hexagonal Bin Plot

#df['b'] = df['b'] + np.arange(1000)
#df.plot.hexbin(x='a', y='b', gridsize=25)
#3D图形


#histogram
df4 = pd.DataFrame({'a': np.random.randn(1000) + 1, 'b': np.random.randn(1000),'c': np.random.randn(1000) - 1}, columns=['a', 'b', 'c'])
df4.plot.hist(alpha=0.5)

#ares绘图
df5 = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
df5.plot.area()

#密度图
df.plot.kde()

plt.show()


