import re

# ^	匹配字符串开头
# $	匹配字符串结尾

data = "0laowa@itcast.cJ"

try:
    ret = re.match("^\d[a-zA-Z0-9]{2,29}@itcast\.c[a-zA-Z]$", data)
    # 获取匹配的结果
    info = ret.group()
except Exception as e:
    print("匹配失败")
else:
    print(info)