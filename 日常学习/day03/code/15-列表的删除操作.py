my_list = [1, 'hello', 2, 3, 4, 'python', 'a', 'b', 'c', 'python', 'cpp']
print(my_list)

# 1. 列表.remove(value)  根据数据值删除数据  直接修改原列表,返回值为None
# 注意点: 删除的数据如果不存在,会报错
# print(my_list.remove('hello'))  # None
my_list.remove('hello')
print(my_list)
if 'hello' in my_list:
    my_list.remove('hello')

# 2. 列表.pop(下标)  根据下标删除数据, 默认可以不写,删除最后一个元素, 是直接在原列表中的删除
# 返回值是删除的数据
result = my_list.pop()  # 删除最后一个数据 'cpp'
print('result:', result)
print(my_list)
result1 = my_list.pop(4)  # 删除下标为4的数据
print('result:', result1)
print(my_list)

# 3. del 列表[下标]  根据下标删除数据
del my_list[-1]
print(my_list)
# del my_list[10]  下标不存在,会报错

