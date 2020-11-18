# 列表 list 列表中可以存放任意多个数据,每个数据之间使用 逗号隔开

# 列表的定义方式一   变量 = list(可迭代序列)
my_list1 = list()
my_list2 = list('hello')  # 会将字符串中的每一个字符作为列表中的一个数据
my_list3 = list(range(3))  # 0 1 2
print(my_list1, type(my_list1))  # [] <class 'list'>
print(my_list2, type(my_list2))  # ['h', 'e', 'l', 'l', 'o'] <class 'list'>
print(my_list3, type(my_list3))  # [0, 1, 2] <class 'list'>

# 列表的定义方式二 使用字面量的方式 [数据, 数据, 数据, 数据]

my_list4 = [2, 3.14, 'isaac', False]
my_list5 = []
print(my_list4, type(my_list4))  # [2, 3.14, 'isaac', False] <class 'list'>
print(my_list5, type(my_list5))  # [] <class 'list'>

# 列表支持下标和切片操作
# 3.14
print(my_list4[1])  # 使用下标访问列表中的数据

# 不同点: 可以使用下标修改列表中的数据
my_list4[1] = 3.1415926
print(my_list4)  # [2, 3.1415926, 'isaac', False]

