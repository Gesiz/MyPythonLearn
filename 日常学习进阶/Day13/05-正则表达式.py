import re

# 参数1 : 匹配规则
# 参数2 : 数据来源
ret = re.match("itcast", "itcast.cn")
# 获取匹配的结果
info = ret.group()
print(info)
