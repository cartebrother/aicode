import random

n = int(input("请输入注数："))

for i in range(1,n+1):
    red = random.sample(range(1,34),6)
    red.sort()
    blue = random.randint(1,16)

    print(f"第{i}注号码为：红色：{red}，蓝色：{blue}")
