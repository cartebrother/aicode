# count统计出现的数量

# replace: 替换字符串

s = "语文:110,数学:100,英语:115"

r1 = s.count(":")
print(r1)

r2 = s.replace(",","|")
print(r2)

r3 = s.replace(",","|",1)
print(r3)