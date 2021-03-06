# 列表如下
lst = [2, 5, 6, 7, 8, 9, 2, 9, 9]
# """
# 1 找出列表里的最大值
print(max(lst))
# 2 找出列表里的最小值
print(min(lst))
# 3 找出列表里最大值的个数
print(lst.count(max(lst)))
# 4 计算列表里所有元素的和
print(sum(lst))
# 5 计算列表里元素的平均值
print(sum(lst) / float(len(lst)))
# 6 计算列表的长度
print(len(lst))
# 7 找出元素6在列表中的索引
print(lst.index(6))
# """
lst = [2, 5, 6, 7, 8, 9, 2, 9, 9]
# 1 在列表的末尾增加元素15
lst.append(15)
# 2 在列表的中间位置插入元素20
lst.insert(20, len(lst) // 2)
# 3 将列表[2,5,6]合并到lst中
lst.extend([2, 5, 6])
# 4 移除列表中索引为3的元素
lst.remove(lst[3])
# 5 翻转列表里所有的元素
lst[::-1]
# 6 对列表里的元素进行排序 从小到达一次 从大到小一次
lst.sort(reverse=True)

# 复杂列表练习
# 列表lst如下
lst = [1, 4, 5, [1, 3, 4, 5[8, 9, 10, 12]]]
# 不写任何代码 通过思考来回答问题
# 1 列表的长度是多少
# 2 列表lst中有几个元素
# 3 lst[1]的数据类型是什么
# 4 lst[3]的数据类型是什么
# 5 lst[3][4]的值是什么
# 6 如何才能访问到这九个值
# 7 执行lst[3][4].append([5,6] 列表lst的内容是什么) 手写出来
# 8 lst[-1][-1][-2]的值是什么
# 9 lst[-2]的值是什么
# 10 len(lst[-1])的值是什么
# 11 len(lst[-1][-1])的值是什么
# 12 lst[-1][1:3]的值是什么
# 13 lst[-1][-1][1:-2]的值是什么

