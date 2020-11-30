"""
from 包名 import 模块
from 包名.包名 import 模块
from 包名.模块 import 模块资源
"""
# TODO from 包名 import 模块, 模块2, ...
# 1. from 包名 import 模块
# 2. from 包名 import 模块, 模块2, ...
# 3. from 包名 import 模块
#    from 包名 import 模块2
# from users import module1, module2
#
# print(module1.name1)
# print(module2.name2)

# TODO from 包名.包名 import 模块
# from users.usercenter import userinfo, setpassword
#
# print(userinfo.name)
# print(setpassword.name)

# 错误的示范
# from users import usercenter.userinfo

# TODO from 包名.模块 import 模块资源
# 正确的导入方式
# from users.module1 import name1
# print(name1)

# TODO 思考 不能导入
# from users import module1.name1
# print(module1.name1)

# TODO 小练习
# 要求直接导入userinfo模块里面的 name = 'userinfo'
from users.usercenter.userinfo import name

print(name)




