my_list = ['abc', 'adb', 'aaaa', 'badaf', 'bb', 'bcd']
# # 直接排序
# my_list.sort()
# print(my_list)
# 按照字符串的长度排序
istr = "asdasd"



print(istr[::-1])
# my_list.sort(key=lambda x: len(x) * 9999 if len(x) > (lambda a, y: y.index(a))(x, globals(my_list)) else len(x) * 999 + 1)
# my_list.sort(key=lambda x: len(x) * 999999 + (ord(x[0]) * 100) - (ord(x[1]) * 10000) )
# my_list.sort(key=lambda x: [i for i in my_list if len(i) == len(x)])

print(sorted([i for i in [i for i in my_list if len(i) == len('abc')]],reverse=True))
my_list.sort(key=lambda x: len(x))
print([i for i in [len(i) for i in my_list]].count(0))
# print(sorted(my_list, key=len))
print(my_list)

