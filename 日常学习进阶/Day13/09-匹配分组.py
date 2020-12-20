import re

# |	匹配左右任意一个表达式
# data = "laowang@qq.cn"
#
# try:
#     ret = re.match("[a-zA-Z0-9]{3,30}@(163|itcast)\.cn", data)
#     # 获取匹配的结果
#     info = ret.group()
# except Exception as e:
#     print("匹配失败")
# else:
#     print(info)

# (ab)	将括号中字符作为一个分组
# data = "laowang@163.cn"
#
# try:
#     ret = re.match("([a-zA-Z0-9]{3,30})@(163|itcast)\.cn", data)
#     # 获取匹配的结果
#     info = ret.group()
# except Exception as e:
#     print("匹配失败")
# else:
#     # ret.group(): 把所有的匹配数据都获取到
#     # ret.group(1): 获取第一个组中的数据
#     # ret.group(2): 获取第二个组中的数据
#     print(ret.group(1))
#     print(ret.group(2))


# \num	引用分组num匹配到的字符串
# data = "<html>nihao</html>"
#
# try:
#     ret = re.match("<[a-zA-Z0-6]{1,30}>.*</[a-zA-Z0-6]{1,30}>", data)
#     # 获取匹配的结果
#     info = ret.group()
# except Exception as e:
#     print("匹配失败")
# else:
#     # ret.group(): 把所有的匹配数据都获取到
#     # ret.group(1): 获取第一个组中的数据
#     # ret.group(2): 获取第二个组中的数据
#     print(info)


# data = "<html><div>nihao</div></html>"
# try:
#     ret = re.match("<([a-zA-Z0-6]{1,30})><([a-zA-Z0-6]{1,30})>.*</\\2></\\1>", data)
#     # 获取匹配的结果
#     info = ret.group()
# except Exception as e:
#     print("匹配失败")
# else:
#     # ret.group(): 把所有的匹配数据都获取到
#     # ret.group(1): 获取第一个组中的数据
#     # ret.group(2): 获取第二个组中的数据
#     print(info)


# (?P<name>)	分组起别名
# (?P=name)	引用别名为name分组匹配到的字符串
data = "<html><div>nihao</div></html>"
try:
    ret = re.match("<(?P<name1>[a-zA-Z0-6]{1,30})><(?P<name2>[a-zA-Z0-6]{1,30})>.*</(?P=name2)></(?P=name1)>", data)
    # 获取匹配的结果
    info = ret.group()
except Exception as e:
    print("匹配失败")
else:
    # ret.group(): 把所有的匹配数据都获取到
    # ret.group(1): 获取第一个组中的数据
    # ret.group(2): 获取第二个组中的数据
    print(info)

