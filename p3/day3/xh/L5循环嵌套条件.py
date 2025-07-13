sum = 0

for i in range(1,101):
    if i%2 ==0:
        sum += i

print("1到100的偶数相加的和是：",sum)


print("==================")
# 2 1-100 能整除13的数的和

sum2 = 0
for i in range(1,101):
    if i%13 == 0:
        print("当前数字：",i)
        sum2 += i

print("1到100能整除13的数的和是：",sum2)


# 3 无限循环嵌套分支
while True:
    s = """
    1 前进
    2 后退
    3 向左
    4 向右
    5 回城
    0 结束
    """
    print(s)
    c = input("请输入数字：")
    if c == "1":
        print("前进")
    elif c == "2":
        print("后退")
    elif c == "3":
        print("向左")
    elif c == "4":
        print("向右")
    elif c == "5":
        print("回城")
    elif c == "0":
        print("结束")
        break
    else:
        print("输入错误")