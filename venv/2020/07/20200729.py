num_1, num_2, num_3, num_4 = 1, 2, 3, 4
print(num_4 > num_1 > num_2)
num_5=1
print((num_2 > num_1) and (num_1 < num_4))

print(num_4 < num_1 or num_1 > num_2)

print(num_1 is num_5) # True
print(id(num_2))
sock = '枕头';
soce = '枕头';

print(sock is soce) #True
print(id(soce) is id(sock)) #False