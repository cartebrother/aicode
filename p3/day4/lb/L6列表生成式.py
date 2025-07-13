print("===== 把列表[1,99]中所有数字3或5的倍数，放入列表中：")
r1 = []
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        r1.append(i)
print("循环方式生成：",r1)

# 用列表生成式实现
r2 = [i for i in range(1, 100) if i % 3 == 0 or i % 5 == 0]
print("生成式生成：  ",r2)


print("===== 把列表3个数字平方后，放入列表中：")

r3 = range(1, 11)
r33 = []

for i in r3:
    r33.append(i * i)
print("循环方式得到：",r33)

r4 = [i * i for i in range(1, 11)]
print("生成式得到：  ",r4)

print("===== 把列表中所有数字>100的数字，放入列表中：")

r4 = [200, 300, 400, 500, 600, 700, 800, 900, 1000,1,11]
r44 = []

for i in r4:
    if i > 100:
        r44.append(i)
print("循环方式得到：",r44)

r5 = [i for i in r4 if i > 100]
print("生成式得到：  ",r5)