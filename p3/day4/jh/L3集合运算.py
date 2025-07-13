# 1. in not in

set1 = {"java", "python", "php", "node", "java"}
b1 = "c" not in set1
print(b1)  # True

print("===== not in")

b2 = "java" in set1
print(b2)  # True

set2 = {3, 5, 6, 7, 8, 9}
set3 = {5, 6, 7, 8, 9, 10, 12}
print("===== 交集")

set_j = set2 & set3
set_j2 = set2.intersection(set3)

print(set_j)
print(set_j2)

print("===== 并集")

set_b = set2 | set3
set_b2 = set2.union(set3)

print(set_b)
print(set_b2)


print("===== 差集")

set_c = set2 - set3
set_c2 = set2.difference(set3)

print(set_c)
print(set_c2)


print("===== 对称差")

set_dc = set2 ^ set3
set_dc2 = set2.symmetric_difference(set3)

print(set_dc)
print(set_dc2)