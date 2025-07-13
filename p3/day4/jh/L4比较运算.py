set1 = {2,4,6}
set2 = {2,4,6,10,12}
set3 = {100,200,300}

# > >= < <=

b1 = set2 > set1
b2 = set2 >= set1

print(b1)
print(b2)


# ==

b3 = set1 == set2

print(b3)

# 超集合和子集合

b4 = set1.issubset(set2)

b5 = set2.issuperset(set1)

print(b4)
print(b5)