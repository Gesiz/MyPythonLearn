# 集合 set 表示方式 :{数据,数据,数据}
# 1. 集合时无序的，数据的添加顺序和输出顺序不一致
# 2. 集合中的数据时没有重复的 天然去冲 可以对列表元组 去重
# 3. 集合是可变类型
# 4. 集合中的数据必须是不可变类型
set1 = set()
print(set1, type(set1))
set2 = {1, 3, 4, 5, 3, 2}
print(set2)  # {1，2，3，4，5} 没有重复数据 数据的顺序和添加的顺序不一致

# set3 = {[1, 2]}  # 报错
# set4 = {(1, 2)}  # 可以
# set4 = {(1, 2, [1, 2])}  # 报错 没有重复的数据 数据的顺序和添加的顺序不一致

# 类型转换
import random

my_list = [random.randint(10, 30) for i in range(20)]
print(my_list, len(my_list))

my_list1 = list(set(my_list))
print(my_list1, len(my_list1))

# 可变类型
set2.remove(5)
print(set2)
num = set2.pop()
print(num)
print(set2)
set3 = {0, 22, 3, 41, 4, 51, 1, 34, 15, 15, 13}
num = set3.pop()
print(num)
print(set3)
# 需求 将11 修改为20
# 方法一 先转类型 修改 转回来
list3 = list(set3)
# list3[list3.index(11)] = 20
set3 - set3
print(set3)
# 方法二先删除后添加
# set3.remove()
# set3.add(11)

print("asdasd asdasd".capitalize())