import re

# .	匹配任意1个字符（除了\n）
# ret = re.match("t.o", "tqo")
# # 获取匹配的结果
# info = ret.group()
# print(info)


# [ ]	匹配[ ]中列举的字符
# try:
#     ret = re.match("t[abcde]o", "tao")
#     # 获取匹配的结果
#     info = ret.group()
# except Exception as e:
#     print("匹配失败")
# else:
#     print(info)

# \d	匹配数字，即0-9
# try:
#     ret = re.match("t\do", "t1o")
#     # 获取匹配的结果
#     info = ret.group()
# except Exception as e:
#     print("匹配失败")
# else:
#     print(info)

# \D	匹配非数字，即不是数字
# try:
#     ret = re.match("t\Do", "t1o")
#     # 获取匹配的结果
#     info = ret.group()
# except Exception as e:
#     print("匹配失败")
# else:
#     print(info)

# \s	匹配空白，即 空格，tab键
# try:
#     ret = re.match("t\so", "t o")
#     # 获取匹配的结果
#     info = ret.group()
# except Exception as e:
#     print("匹配失败")
# else:
#     print(info)

# \S	匹配非空白
# try:
#     ret = re.match("t\So", "t$o")
#     # 获取匹配的结果
#     info = ret.group()
# except Exception as e:
#     print("匹配失败")
# else:
#     print(info)

# \w	匹配非特殊字符，即a-z、A-Z、0-9、_、汉字
# try:
#     ret = re.match("t\wo", "t@o")
#     # 获取匹配的结果
#     info = ret.group()
# except Exception as e:
#     print("匹配失败")
# else:
#     print(info)

# \W	匹配特殊字符，即非字母、非数字、非汉字
try:
    ret = re.match("t\Wo", "t@o")
    # 获取匹配的结果
    info = ret.group()
except Exception as e:
    print("匹配失败")
else:
    print(info)
