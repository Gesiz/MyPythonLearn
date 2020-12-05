# TODO 导入单个模块起别名
# 语法
# import 模块名1 as 别名
# import module1 as m1
#
# print(m1.name)


# TODO 导入多个模块起别名
# 语法
# import 模块名1 as 别名1, 模块名2 as 别名2, 模块名n as 别名n
import module1 as m1,module2 as m2

print(m1.name)
print(m2.name)

# TODO 起别名有什么作用
# 1. 通过起别名简化调用资源的名字
# 2. 防止资源名字冲突（from里面体现）