s = "I am Chinese!"
ss = " I am Chinese! "

# 内置方法 ,转成大写
s1 = s.upper()
b1 = s.isupper()
print(s, "upper:", s1 ," s is upper :",b1)

# 内置方法 ,转成小写
s2= s.lower()
b2=s.islower()
print(s, "lower:", s2 ," s is lower :",b2)

#开始和结束
b33 = s.startswith("I")
b44 = s.endswith("!")
print("s startswith I:",b33," s endswith !:",b44)

#是不是数字
b5 = s.isdigit()
b6 = s.isalpha()
b7= s.isalnum()
b8 = s.isnumeric()
print("s isdigit:",b5," s isalpha:",b6," s isalnum:",b7," s isnumeric:",b8)


# 去掉两边的空格或者换行符

s9 = ss.strip()
print("ss strip: ",s9)

s3=s.capitalize()
print("s capitalize: ",s3)