t1 = (1, 2, 3)
t2 = (4, 5, 6 ,"中国", "美国")

print("t1: ",t1)
print("t1的类型： ",type(t1))

print("t2",t2)
print("t2 的长度：",len(t2))

print("索引运算： t2[1] = " ,t2[1] , " t2[-1] = " , t2[-1])

print("切片：  t2[1:3] = " , t2[1:3])

print("=====遍历t2")

for t in t2:
    print(t)

print("成员运算： 5 in  t2 = ",(5 in t2))
print("成员运算： 7 not in t2 = ",(7 not in t2))

print("拼接t1，t2 = ",(t1 + t2))

print("比较运算： t1= t2  expect : false  real:",(t1 == t2))
print("比较运算： t1 >= t2  expect : false  real:",(t1 >= t2))
print("比较运算： t1 <= t2  expect : true  real:",(t1 <= t2))

print("一元组： (1,)）",type(1,))
print("一元组 (\"hello,\")",("hello",)  ," 字符串  (\"hello\")）",("hello"))
y1 = ()
print("空元组： () : ",y1 , "  y1的类型： ",type(y1))
