#整型

x = 10

print(type(x)) # <class 'int'>

#浮点型

y = 3.14

print(type(y)) # <class 'float'>

#布尔类型 比较得到

z = (x > y)
print(z)

# 直接申明
a = True
b = False
print("a type is : ",type(a)) # <class 'bool'>
print("a= ",a)
print("b= ",b)


# 用在分支条件中
if a:
    print("a is True")
else:
    print("a is False")


#所有的数据都有布尔值 ,整型和浮点型的0都是False ,其它的都是 True


print("x bool value is :",bool(x))

print("0 bool value is :",bool(0))

print("0.0 bool value is : ",bool(0.0))


# 字符串  “” ，列表 [] ，字典 {} 都是False,其它的都是 True

print(" "" bool value is :",bool(""))

print(" [] bool value is :",bool([]))

print(" {} bool value is :",bool({}))