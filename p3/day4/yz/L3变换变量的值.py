x = 100
y = 200

print(f"""
x = {x}
y = {y}
""")

x,y = y,x

print(f"""
变换之后
x = {x}
y = {y}
""")

a = "hello"
b = "world"
c = "carter"
print(f"""
a = {a}
b = {b}
c = {c}
""")

a,b,c = c,a,b

print(f"""
变换之后
a = {a}
b = {b}
c = {c}
""")

# 超过三个需要通过解包操作实现

