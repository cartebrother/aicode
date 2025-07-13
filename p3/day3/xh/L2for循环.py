# for 变量 in 序列:
#     循环体


a = [1,2,3,4,5,6,7]
for n in a:
    print("数字： ",n)


print("=字符串==================")

s = "hello world"
for c in s:
    print("字符： ",c)


print("==============字典====")

liebiao={100,200,300,400,500}
for x in liebiao:
    print("元素： ",x)


print("===========range构造数组=======")

for y in range(100,150):
    print("数字y： ",y)

print("===========range构造数组-带步长=======")

for z in range(1,10,2):
    print("数字z： ",z)