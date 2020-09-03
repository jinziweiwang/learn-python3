condition =""
if condition:
    print("null --")
else:
    print("ok --")

ver ={}

if ver:
    print("ok --")
else:
    print("no--")

a=True
b=False

print("a and b is {}".format(a and b))

m =1
n=2
print(m and n)

age =19
#assert  age ==18,"他竟然不是18岁" #测试的时候出现 类似于断言异常

costs=[213,3,12,54]
for i in costs:
    print('消费{}元'.format(str(i)).center(30))
import random
random_arr=[]
while(9 not in random_arr):
    random_arr.append(random.randint(1,10))
print(random_arr,len(random_arr))

a1=[1,2,3]
b1=1
c=(b1 in a1) #不是元组
print(c) #打印true 或者false

import time
number=0
#无限循环演示
#while True:
#    time.sleep(1)
#    number +=1
 #   print('hello world. {}'.format(number,end='\r'))

x=[1]
y=(1)  #y=(1,)元组写法
print(type(x),type(y),y)