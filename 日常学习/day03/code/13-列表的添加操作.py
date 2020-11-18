my_list = [1, 2, 3]
print(my_list)  # [1, 2, 3]
# 列表.append(数据)  向列表的尾部添加数据, 直接修改原列表,返回的是 None
# print(my_list.append(4))   # None
my_list.append(4)
print(my_list)  # [1, 2, 3, 4]

# 列表.insert(下标, 数据)  在指定下标位置添加数据, 直接修改原列表,返回的是 None
# 注意点: 书写的下标必须存在,将数据添加到最后的位置
my_list.insert(1, 'hello')  # 在下标为1的位置,添加数据 hello, 本来的数据后移
print(my_list)  # [1, 'hello', 2, 3, 4]
my_list.insert(10, 'python')
print(my_list)   # [1, 'hello', 2, 3, 4, 'python']

# 列表.extend(可迭代序列)  将可迭代序列中的每一个元素逐个添加到列表的尾部, 直接修改原列表,返回的是 None
my_list.extend('abc')
print(my_list)  # [1, 'hello', 2, 3, 4, 'python', 'a', 'b', 'c']
my_list.extend(['python', 'cpp'])
print(my_list)  # [1, 'hello', 2, 3, 4, 'python', 'a', 'b', 'c', 'python', 'cpp']

