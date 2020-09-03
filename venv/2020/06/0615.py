import array
import numpy as np

list=np.array(range(10))
print(list)

a=np.zeros(10)
print(a,type(a))

b=np.zeros(10,dtype=int)
print(b)
#多维数组
c=np.zeros((4,4),dtype=int)#float
print(c)
d=np.full((3,3),3.14)
print(d)
e=np.zeros_like(d)
print(e)
f=np.random.random(10)
print(f)
g=np.random.randint(0,10,(5,5))
print(g)
h=np.random.randint(1,33,(6,1))
print(h)
i=np.linspace(0,3,10)
print(i)
#n维度的单位数组
j=np.eye(5)
print(j)
var=[[1,2,3],[4,5,6],[7,8,9]]
print(np.array(var))
#print(var[1,0],var[1][0])
#打印维度
print(a.ndim)
print(a.itemsize)
print(a.dtype) #float64
k=np.linspace(0,np.pi,10) #将数据的值拆成10份
print(k)
print(sum([1,2,3,4,5]))
l=np.full(10,2.3)
print(l)
#sum优化
print(np.sum(var))
print(np.sum(l))
timeit sum(var)
timeit np.sum(var)