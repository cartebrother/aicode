import random
import string

random_num = random.randint(1000,9999)

print("随机数字：",random_num)

print("===========随机选择")

source = string.digits + string.ascii_lowercase+string.ascii_uppercase
s=""


for i in range(6):
    s += random.choice(source)


print("随机字母：",s)