random_numbers = [1,32,3,2,4,7]
'''
for num in random_numbers:
    if num % 2 ==0:
        print('{} is 偶数'.format(num))
    else:
        continue
'''

#for循环中，如果没有碰到break语句，就会执行else里的代码
for num in random_numbers:
    if num % 2 == 0:
        print('{} is 偶数'.format(num))
    else:
        continue
    print("没有结束")
else:
    print("结束")
#for循环可以构建推导式
#所谓推导式，就是一种从一个数据序列构建另一个数据序列的方法

random_numbers_new = [number*10 for number in random_numbers]

print(random_numbers_new)
#字典推导式

dict_numbers ={number:'A' for number in random_numbers}
print(dict_numbers)
#元组生成器
print(tuple(random_numbers))

variable ={
    'a':200,
    'b':300,
    'c':400
}
print(variable['a'])

print(variable.items())

print([key for key, value in variable.items() if value ==200])

def findV(para,v):
    return [key for key, value in para.items() if value ==v]

print(findV(variable,200))

def test(val):
    a=val.append(100)
    return a
var =[]
print(test(var))

#参数的收集
#写接口的时候将用户传递的值收集起来
#*args,代表任意参数 ； **kwargs参数收集
def clol(name,age,*args,**kwargs):
    print(name,age,*args,**kwargs)

#可以将一个函数名赋值给变量

#python语法糖，装饰器

def test(func):
    return func

def func():
    print('func run')
print(test(func))

f = test(func)
print(f.__name__)

import random

#@decorator
def ranm():
    return random.random()

print(ranm())
