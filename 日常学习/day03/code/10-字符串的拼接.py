# str.join(可迭代序列)  将str字符串插入到可迭代序列中每两个元素之间
# 可迭代序列是的内容必须是字符串类型
# 返回值: 得到一个新的字符串
my_str = "_".join('hello')
my_str1 = "_*_".join('hello')
print(my_str)  # h_e_l_l_o
print(my_str1)  # h_*_e_*_l_*_l_*_o

my_list = ['my', 'name', 'is', 'isaac']
my_str2 = ' '.join(my_list)
print(my_str2)

