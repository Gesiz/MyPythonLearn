import re
import socket

socket.socket(socket.AF_INET)

data = input("请输入ip地址")
# data = "192.168.0."
# data = "1922.168.0.1"
# (
# \d [0-9]
# [1-9]\d 10-99
# 1\d{2} 100-199
# 2[0-4]\d 200-249
# 25[0-5] 250-255
# .
# )
# {3}
try:
    ret = re.match(
        "("
        "("
        "\d|"
        "[1-9]\d|"
        "1\d{2}|"
        "2[0-4]\d|"
        "25[0-5]"
        ")"
        "\."
        "){3}"
        "(\d|"
        "[1-9]\d|"
        "1\d{2}|"
        "2[0-4]\d|"
        "25[0-5])",
        data)
    # 获取匹配的结果
    info = ret.group()
except Exception as e:
    print("匹配失败 不符合IPV4规则")
else:
    print(info, "匹配成功")
