#MATPLOTLIB绘图
import matplotlib.pyplot as plt
import numpy as np

#%matplotlib inline

x=np.linspace(0,10,100)
#print(x)
y=np.sin(x)
#plt.plot(x,y)
plt.plot(x,y,'--')
plt.plot(x,np.sin(x),'o',color="black",label="sin(x)",markersize=4,linewidth=10)
plt.plot(x,np.cos(x),'o',label="cos(x)")
#loc是location的简写，控制label的位置显示
plt.legend(loc=1)
#展示页面
plt.show()
# plt.plot
#fig=plt.figure()
#fig.savefig('c:/Users/lenovo/Desktop/11.png')