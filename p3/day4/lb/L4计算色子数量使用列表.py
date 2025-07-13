import random

a = [0] * 6

print("a = ",a)

for i in range(1,6001):
    r = random.randint(1,6)
    a[r-1] = a[r-1] + 1

for i in range(len(a)):
    print(f"""骰子点数 {i+1} 出现了: {a[i]}次""")


sum = a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
print("sum = ",sum)