import pandas as pd
import numpy as np
#pandas 表格处理工具
base_path = 'c:/Users/lenovo/Desktop/class.csv'
df=pd.read_csv(base_path)
print(df.head(3))
print(type(df))
print(df.index)
print(df.loc[0])

#筛选数学大于80
print(df.数学 > 80)
print(df[df.数学 <70])
sort_val=df.sort_values(['数学','语文']).head()
print(sort_val)



scores={
    '英语':[90,78,89],
    '数学':[76,88,90],
    '姓名':['lili','zhangsn','Jack']
}
ds=pd.DataFrame(scores)
print(ds)
dss=pd.DataFrame(scores,index=['one','two','three'])
print(dss)

print(df.values)
print(df.数学.values)
print(df.数学.value_counts)
def func(score):
    if score>=80:
        return "优秀"
    elif score>=70:
        return "良好"
    elif score >=60:
        return "及格"
    else:
        return "不及格"
#map函数运用非常广泛
df['数学分类']=df.数学.map(func)
print(df)
#lambda 匿名函数
df.apply(lambda x : str(x) + "--")
func1 =lambda number: number+10
print(df)

def func_getnum(x):
    return x +10

list =list(map(lambda x:x+100,range(10)))
print(list)


