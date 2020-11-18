# 切片: 从字符串中截取一部分内容,不会改变原来的字符串,会新创建一个字符串
# 变量[start:end:step]  从下标为start开始,到下标end结束(不包含end), 步长是step(下标之间的间隔)
my_str = 'abcdef'

# 'bcd'
my_str1 = my_str[1:4:1]
print(my_str1)  # bcd
# 步长如果是1, 可以不写
my_str2 = my_str[1:4]
print(my_str2)  # bcd

# 步长为正数, 开始位置不写,默认是0, 但是冒号不能省
my_str3 = my_str[:4]  # [0:4]
print(my_str3)  # abcd

# 步长为正数, 结束位置不写,相当于是长度 len()
my_str4 = my_str[:]  # [0:len()]
print(my_str4)  # abcdef

my_str5 = my_str[::2]  # [0:6:2] 0 2 4
print(my_str5)  # ace

my_str6 = my_str[4:1]  # [4:1:1] 步长是正数,代表从左到右(开始位置要在结束位置的左边), 取不到数据
print("my_str6: ", my_str6)

# 步长可以是负数, 代表从右向左(开始位置要在结束位置的右边)
my_str7 = my_str[4:1:-1]
print(my_str7)  # edc

# 字符串的逆置
my_str8 = my_str[::-1]
print(my_str8)  # fedcba

