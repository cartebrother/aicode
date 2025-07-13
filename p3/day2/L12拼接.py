# 字符串拼接使用 +

s1 = "hello"
s2 = "world"
s3 = s1 + "  " + s2

print(s3)

name = "李福春"
age = 20

s4= "我的名字："+name +"\n我的年龄是："+ str(age) + "**"*10
print(s4)


#计算字符串长度

len1 = len(s4)
print("len1 is : ",len1)

s5="my name is 李福春"
len2 = len(s5)
print("len2 is : ",len2)


# in 是否存在,连续的字符串

b1 = "李" in s5
print("b1 is : ",b1)