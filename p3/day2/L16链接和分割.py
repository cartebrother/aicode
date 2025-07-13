# split分割成列表

s = "深圳,广州,北京,杭州,衡阳"

list = s.split(",")

print( list)

print(type(list))

n = len(list)

print(s, "城市数量：",n,sep="\n")


# 拼接字符串

s2 = "|".join(list)

print(s2)