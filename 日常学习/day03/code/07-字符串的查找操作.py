my_str = 'hello world itcast and itcastcpp'

# str.find(sub_str, start, end)  在字符串中查找另外一个字符串
# sub_str 要查找的字符串
# start 开始的位置,从哪个位置进行查找, 默认是 0
# end  结束的位置,查找到哪里结束 默认是len()
# 返回值,就是方法执行的结果, ① 没有找到要查找的内容,返回-1, ② 找到要查找的内容,返回的是正数下标
# str.rfind(sub_str, start, end)  从右边开始查找,找到返回的依然是正数下标

num = my_str.find('itcast')
print(num)  # 12

num1 = my_str.find('itcast', 15)
print(num1)  # 23

num2 = my_str.find('itcast', 15, 28)
print(my_str[28])  # t
print(num2)  # -1

num3 = my_str.rfind('itcast')
print(num3)  # 23


# str.index(sub_str, start, end)  在字符串中查找另外一个字符串
# sub_str 要查找的字符串
# start 开始的位置,从哪个位置进行查找, 默认是 0
# end  结束的位置,查找到哪里结束 默认是len()
# 返回值,就是方法执行的结果, ① 没有找到要查找的内容,程序报错 ② 找到要查找的内容,返回的是正数下标
# str.rindex(sub_str, start, end)  从右边开始查找,找到返回的依然是正数下标

num4 = my_str.index('itcast')
print(num4)  # 12

num5 = my_str.index('itcast', 15)
print(num5)  # 23

num5 = my_str.rindex('itcast')
print(num5)  # 23

# num5 = my_str.index('itcast', 24)  # 程序会报错
# print(num5)  # 23

# str.count(sub_str, start, end)  统计字串出现的次数
# sub_str 要查找的字符串
# start 开始的位置,从哪个位置进行查找, 默认是 0
# end  结束的位置,查找到哪里结束 默认是len()
# 返回值, 字串出现的次数

num6 = my_str.count('itcast')
print(num6)  # 2

num6 = my_str.count('itcast', 15)
print(num6)  # 1

num6 = my_str.count('itcast', 26)
print(num6)  # 0