# lambda表达式
# 三元运算符
def do_serach(c):
    return lambda x: True if x in c else False
res = do_serach((1,2,3,4))

print(res(1))