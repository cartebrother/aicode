import random

s = [[100,88,60],[90,80,70],[80,70,60]]

print("s",s)
print("s[1]",s[1])
print("s[2][2]",s[2][2])


s3 = [[random.randint(60,100) for i in range(3)] for j in range(5)]
print("s3",s3)


s2 = []
for i in range(5):
    tmp = []
    for j in range(3):
        input_int = int(input(f"请输入第{i}个学生的第{j}门课成绩："))
        tmp.append(input_int)
    s2.append(tmp)
print("s2",s2)

