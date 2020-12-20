import re

# *	匹配前一个字符出现0次或者无限次，即可有可无
# data = "agc"
#
# try:
#     ret = re.match("a[abcd]*c", data)
#     # 获取匹配的结果
#     info = ret.group()
# except Exception as e:
#     print("匹配失败")
# else:
#     print(info)

# +	匹配前一个字符出现1次或者无限次，即至少有1次
# data = "ac"
#
# try:
#     ret = re.match("aa+c", data)
#     # 获取匹配的结果
#     info = ret.group()
# except Exception as e:
#     print("匹配失败")
# else:
#     print(info)


# ?	匹配前一个字符出现1次或者0次，即要么有1次，要么没有
# data = "ac"
#
# try:
#     ret = re.match("aa?c", data)
#     # 获取匹配的结果
#     info = ret.group()
# except Exception as e:
#     print("匹配失败")
# else:
#     print(info)

# {m}	匹配前一个字符出现m次
# 1 邮箱必须是itcas.cn
# 2 用户名必须是字母和数字组成的
# 3 用户名长度范围是 3~30
data = "laowa@itcast.cn"

try:
    ret = re.match("[a-zA-Z0-9]{3,30}@itcast\.cn", data)
    # 获取匹配的结果
    info = ret.group()
except Exception as e:
    print("匹配失败")
else:
    print(info)
# {m,n}	匹配前一个字符出现从m到n次
