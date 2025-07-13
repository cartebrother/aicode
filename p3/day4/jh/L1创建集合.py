set1 = {"hello","world","ok","good","ok"}
print(set1) # 输出结果：{'hello', 'good', 'world', 'ok'}

print("======== 花括号语法创建")

set2 = {37,5,8,58,61,37}
print(set2) #输出结果： {37, 5, 8, 58, 61}

print("======== set语法创建 ")

set3 = set("hello")
print(set3) #输出结果：{'h', 'l', 'e', 'o'}

print("======== set语法创建 通过列表初始化")

set4 = set([1,2,3,4,5,6,7,8,9,100,5])
print(set4) #输出结果：{1, 2, 3, 4, 5, 6, 7, 8, 9, 100}
print("======== 花括号语法创建 带循环 ")

set5 = {n for n in range(1,11)}
print(set5) #输出结果：{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print("======== 花括号语法创建 带循环和条件 ")

set6 = {n for n in range(1,11) if n % 2 == 0}
print(set6) #输出结果：{2, 4, 6, 8, 10}