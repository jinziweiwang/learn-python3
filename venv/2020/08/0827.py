# 函数装饰器
def deco(original_func):
    def wapper_func(*args, **kwargs):
        return original_func(*args, **kwargs)

    return wapper_func


@deco
def show_age():
    print("i`m 29")


deco(show_age())


def school_teacer(origin_func):
    def wrapper_func(msg):
        return origin_func(msg + "我是杨老师")

    return wrapper_func


@school_teacer
def stu1(name):
    print("我叫", name)


stu1("杨亿金")


def deco_teacher(teacher_name):
    def school_teacer(origin_func):
        def wrapper_func(msg):
            return origin_func(msg + teacher_name)

        return wrapper_func

    return school_teacer


@deco_teacher("，数学老师")
def stu2(name):
    print("我是", name)


stu2("老杨")

# 装饰器案例   程序计时器

import time


def timer(func):
    def wrapper_1():
        start: float = time.time()
        func()
        end = time.time()
        #print(end-start)
        return end - start
    return wrapper_1


@timer
def add_1():
    l_data = []
    for x in range(10000000): #一千万次 2.437476873397827s
        l_data.append(x)

print(add_1())

def aa():
    print("yyy")

#查看函数的名字
print(aa.__name__)
