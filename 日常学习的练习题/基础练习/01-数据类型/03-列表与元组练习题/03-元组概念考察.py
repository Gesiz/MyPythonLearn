# (1,2)*2 (1,2,1,2)
# (1,)*2 (1,1)
# (1)*2 2
# 合并列表
lst = [1, 2, 3]
lst2 = [4, 5, 6]
lst.extend(lst2)
print(lst)
# 合并字符串
str1 = "1,2,3"
str2 = "4,5,6"
# lst = [str1, str2]
# string = ' '.join(lst)
# print(string)
print(str1 + str2)

