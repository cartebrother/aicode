set1 = frozenset([1, 2, 3, 4, 5])
set2 = frozenset([5, 7, 8, 9, 10])
print(set1)

# 遍历

for i in set1:
    print(i)

# 大小
print(len(set1))

# in not in
print(1 in set1)
print(100 not in set1)

# 比较
print(set1 == set2)
print(set1 > set2)


# 是否可以增加和删除 不能
# set2.add(100)
# set2.remove(5)