dict1 = dict(name="carter",age=37,bmi=36,height=180,address=dict(city="上海",country="中国"))

print("成员运算")
print("name" in dict1)
print("sex" not in dict1)


print("索引运算")
print(dict1["name"])

#如果没有对应的key 会报错
# print(dict1["sex"]) #KeyError: 'sex'

print("遍历")

for k in dict1:
    print(k," = ",dict1[k])