print("通过花括号创建字典")

dict1 = {"name":"carter","age":37 , "bmi":36}

print(dict1)

print("通过花括号循环创建字典")
dict11 = {x: x*x for x in range(1,101)}

print(dict11)


print("通过dict关键字创建字典")

dict2 = dict(name="carter",age=37,bmi=36,height=180)
print(dict2)

print("通过zip关键字创建字典")

dict3 = dict(zip("hello","world"))
print(dict3)


print("通过zip关键字创建字典")

dict4 = dict(zip("hello",range(1,101)))
print(dict4)