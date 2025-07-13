list1 = [1,2,3,4,5,6]

print("list1:",list1)

list1.append(7)
print("list1.append(7):",list1)

list1.insert(0,1000)
print("list1.insert(0,0):",list1)

list1.remove(1000)
print("list1.remove(1000):",list1)

p1 = list1.pop()
print("list1.pop() value:",p1," list1: ",list1)

list1.clear()
print("list1.clear():",list1)

list2 = [1,2,3,4,5,6,1,3,4]
list2.remove(1)
print("list2:",list2)
print("list2.remove(1):",list2)


del list2[0]
print("del list2[0]:",list2)


print("list2.index(6)",list2.index(6))

print("list2.count(3): ",list2.count(3))

list2.sort()
print("list2.sort():",list2)

list2.reverse()
print("list2.reverse():",list2)