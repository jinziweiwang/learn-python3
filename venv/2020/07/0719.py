import random
import string

all_row_code = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

my_code = []
for i in range(4):
    gen_code = all_row_code[random.randint(0, len(all_row_code) - 1)]
    print(gen_code)
    my_code.append(gen_code)
print('我的验证码%s' % (','.join(my_code)))


code = ''.join(random.sample((string.digits + string.ascii_lowercase),4))
print(code)

print(string.digits[0:5])

def myinfo():
    name,age='yangyijin',29
    return name,age

print(myinfo())

