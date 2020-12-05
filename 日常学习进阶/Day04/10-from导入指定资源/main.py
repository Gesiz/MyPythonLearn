# 直接使用模块下面的资源
# TODO 之前的方式
# import module1
#
# print(module1.name)
# module1.info()

# TODO 使用from之后
from module1 import name, info

print(name)
info()