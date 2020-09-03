#列表推导式
list_data =[ x for x in range(10)]
print(list_data)

#列表推导式扩展1
list_data1 =[ x for x in range(10) if x%2==0]
print(list_data1)

#列表推导式扩展2
list_data2=[x**2  for x in range(10) if x%2==0]
print(list_data2)
#列表扩展3

list_data3=[(x,y) for x in(1,2,3) for y in (4,5,6)]
print(list_data3)