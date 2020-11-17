# 集合练习题
# 集合间的运算
lst1 = [1, 2, 3, 5, 6, 3, 2]
lst2 = [2, 5, 7, 9]

set1 = set(lst1)
set2 = set(lst2)

# 哪些整数即在lst1 也在lst2中
print(set1.intersection(set2))
print(set1 & set2)
# 哪些整数在lst1中 不在lst2中
print(set1.difference(set2))
print(set1 - set2)
# 两个列表一共有哪些整数
print(set1.union(set2))
print(set1 | set2)
