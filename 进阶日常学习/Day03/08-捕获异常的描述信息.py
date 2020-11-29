# 捕获异常的描述信息

try:
    raise Exception("我是你祖宗")
except Exception as e:
    print(e)

"""
try:
    可能出现的异常代码
except 异常类型 as 变量(异常类的实例):
    捕获到的业务
    print(变量)  # 异常的描述性信息
"""

try:
    print(name)  # name 'name' is not defined
except NameError as e:
    print(e)

