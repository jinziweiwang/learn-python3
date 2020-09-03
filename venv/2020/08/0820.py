# 函数的三种写法
data = [1, 2, 3, 4, 5]
new_1 = []
new_2 = []
new_3 = []
new_4 = []
# 传统函数表达方式
for n in data:
    n += 1
    new_1.append(n)
print(new_1)

# map函数表达方式
def func_1(n):
    return n + 1
new_2 = map(func_1, data)
new_2 = list(new_2)
print(new_2)
# map +lambda方式
#人称一人君，不是浪得虚名
new_3 = list(map(lambda n: n + 1, data))
print(new_3)
#reduce函数  元素减少之意  一次减少一个元素直到用尽
#reduce(func,sequence) n =[4,3,2,1]

#sorted()函数
#sorted(iterable,key=None,reverse=False)
