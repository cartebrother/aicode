# 打包操作

a = 2, 5, 8

print("a : ",a , " type a : " , type(a))

# 解包操作

x, y, z = a

print(f"""解包3个元素： x= {x} , y= {y} ,z = {z}""")

i, *j = a
print(f"""解包带* i= {i} , *j= {j}""")

*b , c = a
print(f"""解包带* b= {b} , c= {c}""")

# 解包语法 适用列表 ，元组 （range， 字符串）