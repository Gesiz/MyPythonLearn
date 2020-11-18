# str.replace(old_str, new_str, count)   字符串的替换
# old_str 原来的本来的字符串
# new_str 新的字符串,替换之后的字符串
# count  替换的次数, 默认是全部替换
# 返回值: 一个替换之后的新的字符串,不会修改原来的字符串

my_str = 'hello world itcast and itcastcpp'

my_str1 = my_str.replace('itcast', 'itheima')
my_str2 = my_str.replace('itcast', 'itheima', 1)
print('my_str :', my_str)
print('my_str1:', my_str1)
print('my_str2:', my_str2)




