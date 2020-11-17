# """
# 已知一个列表
lst = [1, 2, 3, 3, 4, 5]

# 1 求列表的长度
print(len(lst))
# 2 判断6是否在列表中
print(6 in lst)
# 3 lst + [6,7,8] 的结果是什么
print(lst + [6, 7, 8])
# 4 lst * 2 的结果是什么
print(lst * 2)
# 5 列表里元素的最大值是多少
print(max(lst))
# 6 列表里元素的最小值是多少
print(min(lst))
# 7 列表里所有元素的和是多少
print(sum(lst))
# 8 在索引1 的后面新增宇哥元素10
print(lst.insert(1, 10))
# 9 在列表的末尾新增一个元素20
print(lst.append(20))
# """
print(lst)
lst.remove(3)
# lst.pop(0)
print(lst)

# 修改列表
lst = [1, [4, 6], True]

# 请将列表里所有的数字修改成原来的两倍