# 数据类型转换 在转换之前明白两件事
# 数据本来是什么类型
# 你想要将这个数据转换为什么类型
# 新的变量 = 要转换的类型(原来的数据) 数据类型的转换 不会改变原来的数据的类型会生成一个新的数据
# int() 将其他类型转换为 int 类型
# 1.1 将float 类型 转换为 int 类型
num1 = int(3.6)
print(num1, type(num1))

# 1.2 将证书类型的字符串转换为 int 类型 "18" '3'
num2 = int('16')
print(num2, type(num2))

# 2 float() 将其他类型转换为 float 类型
# 2.1 将int 类型转换为 float 类型
num3 = float(15)
print(num3, type(num3))
# 2.2 将数字类型的字符串转换为float类型
num4 = float('3.15')
print(num4, type(num4))
num5 = float('18')
print(num5, type(num5))

# 3. str 将任意类型转换为 字符串类型
# 4. eval()去除引号
# 去除数字类型字符串的引号
# eval() 函数用来执行一个字符串表达式，并返回表达式的值。
num6 = eval('18')
num6 = eval('15.6')
print(num6, type(num6))

# num7 = eval('aa')  # aa去除引号之后 成为变量 变量不存在就会报错
num7 = eval('num6')  # 'num6' 去掉单引号是存在的变量名称 就进行正常的赋值操作

