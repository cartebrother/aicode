s = input("请输入一个数字：")

if s.isnumeric():
    n = int(s)
    print(f"{n} 的绝对值是：{abs(n)}")
else:
    print("这是一个非数字")