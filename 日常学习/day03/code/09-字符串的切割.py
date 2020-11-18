# str.split(sep, maxsplit)   字符串切割
# sep 按照什么字符进行切割,不写,默认按照空白字符进行切割(空格  tab\t 换行\n)
# maxsplit 切割多少次, 默认是全部切割
# 返回值是 列表
my_str = ' hello world itcast and\titcast\ncpp'
my_str = my_str.strip()
result1 = my_str.split()
result2 = my_str.split(' ')
result3 = my_str.split('itcast')
result4 = my_str.split('itcast', 1)
print(result1)
print(result2)
print(result3)
print(result4)



