#6个红球 ， [1,33]
# 1个蓝球  [1,16]

import random
red = random.sample(range(1,34),6)
blue = random.randint(1,16)

red.sort()
print("v1 红色球：",red," 蓝色球：",blue)


red1=[]
blue1=[]

for i in range(6):
    red1.append(random.randint(1,33))
red1.sort()
blue1.append(random.randint(1,16))
print("V2 红色球：",red1," 蓝色球：",blue1)

