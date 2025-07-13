# find找不到返回-1 ，index找不到会报错 找到了则返回索引值

s = "语文:110,数学:100,英语:115"

r1 = s.find("100")
print(r1)

r2 = s.index("115")
print(r2)