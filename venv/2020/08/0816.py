
def function_q(num1,num2):
    resutlt = num1 +num2
    return num1,num2,resutlt

print(function_q(1221,333))

#lamda作为匿名函数
result=lambda x:x**x
print(result(8))


#将lambda 作为参数传递 ，lamada
def income(a,b,c):
    return lambda x:x + a+b+c

res = income(1,2,3)
xx=res(500)
print(xx)