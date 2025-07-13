list1 = [1,2,3,4,5,6]
list2 = ["a","b","c","d","e","f"]

print("list1:",list1)
print("list2:",list2)

list3 = list1 + list2
print("list3:",list3)

list4 = list2 * 4
print("list4:",list4)

b1 = 100 not in list1
print("100 not in list1 : ",b1)

b2 = 2 in list1
print("2 in list1 : ",b2)

print("索引操作： list1[0]:",list1[0]," list1[-1]:",list1[-1])

print("切片操作： list2[0:3]",list2[0:3])

list2[0:3] = ["CarterA","CarterB","CarterC"]
print("切片操作修改信息：list2[0:3] ",list2)

print("列表长度：",len(list2))

list3 = list(range(1,100))
print("list3:",list3)
print("list1：",list1)

print("比较大小： list1 >= list3",list1 >= list3)
print("比较大小： list1 <= list3",list1 <= list3)
print("比较大小： list1 == list3",list1 == list3)

print("====遍历 直接")
for i in list2:
    print(i)

print("====遍历 通过索引")
for ix in range(len(list2)):
    print(ix," = ",list2[ix])

