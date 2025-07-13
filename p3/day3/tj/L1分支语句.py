age = input("请输入年龄：")
if age.isdigit():
    age = int(age)
else:
    print("请输入数字")
    exit()

if age >= 18:
    print(f"{age} 可以投票")
else:
    print(f"{age} 不可以投票")


print("感谢选举国家主席！")