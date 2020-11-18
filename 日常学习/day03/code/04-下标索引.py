# 下标索引: 是字符在字符串中的编号,通过下标可以找到对应的字符
# 变量[下标]  , 访问不存在的下标, 程序会报错

my_str = 'abcdef'
print(my_str)

# 访问 a字符
print(my_str[0])
print(my_str[-6])

# d 字符
print(my_str[3])
print(my_str[-3])

# f 字符
print(my_str[-1])
print(my_str[5])

# len(str)  求字符串的长度(字符串中元素字符的个数)
num = len(my_str)  #
print(num)
print(my_str[len(my_str) - 1])


