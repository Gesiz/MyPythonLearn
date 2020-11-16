# 变量的数据类型 值得是变量所代表的内存中数据的数据类型
# 变量的数据类型有变量中的数据决定的
# 可以使用type(变量/数据) 函数来获取对应的数据类型

# 1 int 整数
# 定义变量num 数据为10
num = 10
# 先计算等号右边的内容 即获取变量的数据类型 再将获取的结果赋给 result
result = type(num)
print(result)

# 2 float 浮点数 小数
pi = 3.14
print(type(3.14))

# 3 bool 布尔类型 (只有两个值 True False)
result = True
print(result)
print(type(result))

# 4 str 字符串
name = '123'
print(type(name))