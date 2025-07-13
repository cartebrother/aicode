name = '李福春'
age = 20
hobby="编程"

s1 = '''
我的名字叫 %s
我的年龄是 %d
我喜欢 %s
'''

# 方式1 占位符
print(s1 % (name,age,hobby))

print("====\n")

# 方式2 名称占位符
print(f'''
我的名字叫 {name}
我的年龄是 {age}
我喜欢 {hobby}
''')

