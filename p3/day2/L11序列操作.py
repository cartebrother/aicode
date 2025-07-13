s="I love AI,this is the develop future of IT industry! "

print(s)

# 索引操作 正索引从0开  负索引从-1结束

print("s index 2 is :",s[2])

print("s last index 3 is : ",s[-3])


# 切片 索引开始位置：索引结束位置 ,缺省是 0,-1 怎么方便怎么来

sa = s[2:6]
print("s  2：6 切片是：",sa) # love

sb = s[6:]
print("s 6：-1 切片是：",sb)

sc = s[:6]
print("s 0：6 切片是：",sc)

# 步长参数

sd = s[0:6:1]

print("s 0：6 1 步长切片是：",sd)


se = s[:]
print("s 0：-1 全切是：",se)

sf = s[::-1]
print("s 0：-1 反转是：",sf)