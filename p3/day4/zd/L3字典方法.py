dict1 = dict(name="carter",age=37,bmi=36,height=180,address=dict(city="上海",country="中国"))
print("dict1 : ",dict1)
print("get name : ",dict1.get("name"))

# 不存在的key 返回None
print("get xxx : ",dict1.get("xxx"))




print("keys: ",dict1.keys())

print("values: ",dict1.values())

print("items: ",dict1.items())

print("遍历items")

for k,v in dict1.items():
    print(k," = ",v)


#字典合并
dict2 = dict(sex="male",country="中国",name="carter.li")
print("dict2 : ",dict2)


dict3 = dict1.update(dict2)

print("update dict1 dict2 return : ",dict3)
print("dict1 : ",dict1)
print("dict2 : ",dict2)

dict4 = dict(name="carter.li",sex="male",country="中国")
dict5 = dict(name="gemini",sex="female",country="中国",age=18)

dict5 |= dict4

print("dict5 : ",dict5)
print("dict4 : ",dict4)


dict6 = dict(name="carter.li",sex="male",country="中国",hobby=["篮球","足球"])
print("dict6: ",dict6)
print("pop ：",dict6.pop("name") , " dict6:",dict6)

print("dict6 popItem  1 : ",dict6.popitem() , " dict6 : ",dict6)

print("dict6 popItem  2 : ",dict6.popitem() , " dict6 : ",dict6)
print("dict6 popItem  3 : ",dict6.popitem() , " dict6 : ",dict6)

#空字典 不能popitem 报错：KeyError: 'popitem(): dictionary is empty'
# print("dict6 popItem  4 : ",dict6.popitem() , " dict6 : ",dict6)


dict7 = dict(name="carter",sex="male",country="中国",hobby=["篮球","足球"])
print("dict7: ",dict7)
dict7.clear()
print(" after clear dict7: ",dict7)

dict8 = dict(name="carter",sex="male",country="中国",hobby=["篮球","足球"])
print("dict8: ",dict8)
del dict8["hobby"]
print(" after del hobby  dict8: ",dict8)