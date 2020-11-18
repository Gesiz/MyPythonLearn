my_list = [1, 'hello', 2, 3, 4, 'python', 'a', 'b', 'c', 'python', 'cpp']

# 1. 列表.index(value, start, end)  在列表中查找数据是否存在
# value 要查找的数据
# start 开始下标 默认0
# end 结束下标 默认 len()
# 返回值: 找到,返回下标, 没有找到,报错
# 注意: 在列表中没有 find 方法
num = my_list.index('python')
num1 = my_list.index('python', 6)
# num2 = my_list.index('python', 10)   # 程序代码报错
print(num)  # 5
print(num1)  # 9

# 2. 列表.count(value)  统计出现的次数的,
# 返回值: 出现的次数
num4 = my_list.count('python')
print(num4)  # 2 

# 3. in/ not in 存在/不存在 返回值是True/False
result = 'python' in my_list
print(result)  # True
if 'python' in my_list:
    pass

