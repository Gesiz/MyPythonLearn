#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project:MyPythonLearn
# Product:PyCharm
# User:Gei
# Author: Gesiz
# Createtime: 2020/9/22 18:28

# 匿名函数 一句话函数 能够实现一些比较的事情
# 定义结构
# lambda:
# 只能返回一种元素或者元组 可以穿*args 或者**kwargs

x = 10
y = 20


def func(x, y):
    return x + y


f = lambda x, y: x + y

print(f(3, 6))
print(f.__name__)

# 使用lambda实现，传入两个传输 将数值大的返回
(lambda x, y: x if x > y else y)(1, 3)

# 使用lambda实现传入一个流标 将列表中后三个元素返回
print((lambda x: x[-3:])([1, 3, 4, 5]))

# 内置函数 拿来主义
# all() 判断元素里边的元素是否都为真 返回的bool值
print(all([1, 2, 3, 4, 5]))

# any() 里面有一个真即为真
any([1, 0, False, "", [], {}, (), set(), None])

print(bytes("abc", encoding="utf-8"))


# callable() 判断是否可调用
def func():
    return 1


f = lambda x: x

print(callable(f))

print(chr(20320))  # 查找内容
print(ord("你"))  # 通过内容查找码位

print(complex(20))  # 复数

print(divmod(5, 2))  # 商余

# eval() exec() 禁止使用
# print(eval("3+2*2/2"))
#
# msg = """
# print(input('>>>'))
# """
# eval(msg)  #
msg = """
def func():
    print("aaa")
func()
"""
exec(msg)

frozenset()  # 冻结集合
help(list.append)  # 帮助

# locals()查看当前空间
print(oct(20))  # 十进制转换为八进制

print(pow(4, 2))  # 幂计算

print(repr("123"))  # 原形毕露
print(repr(123))

print(round(4.5))  # 五舍六入 保留两位小数
print(round(4.213123, 3))  # 五舍六入

# 常用内置函数
# abs() 绝对值
print(abs(-20))

s = 10
print(format(s, "08b"))  # 将十进制转换为二进制
print(format(s, "08o"))  # 将十进制转换为八进制
print(format(s, "08x"))  # 将十进制转换为十六进制

print(format(2.123, ".2f"))  # 保留小数位
print(format("你好", "<20"))  # 右对齐
print(format("你好", ">20"))  # 左对齐
print(format("你好", "^20"))  # 居中

# enumerate() 枚举 默认起始值为0 可以自己指定起始值
lst = ["wenzhou", "taibai", "meet", "alex"]
for i in range(len(lst)):
    print(i, lst[i])

for i, c in enumerate(lst, 0):
    print(i, c)

# 求和 sum()
print(sum([12, 3, 4, 12], start=10))  # 从10开始加

# zip()  # 拉链
lst1 = [1, 2, 3, 4, 5]
lst2 = [1, 1, 1, 1, 1]
lst3 = [1, 1, 1, 1, 1]
lst4 = [1, 1, 1, 1, 1]
print(list(zip(lst1, lst2, lst3, lst4)))  # 对象转换
# 面试题
print(dict(zip(lst1, lst2)))  # 创建字典
d = dict(a=1, b=2, c=3)  # 创建字典
print(d)

# dir()  # 查看当前内容具体有什么方法
print(dir(str))

print(1, "你好", sep="++")
seq = "分割"
end = "结尾"

# reversed()反转
print(list(reversed("你好啊")))

lst = [1, 2, 3, 4]
lst1 = list(reversed(lst))  # 开辟新的空间
lst.sort()  # 在原地进行修改

# 高阶函数 filter() 过滤
# filter(函数过滤条件,可迭代对象) 高阶函数帮我们进行了一次for循环

lst = [1, 2, 3, 4, 5, 6, 7, 8]


def func(x):
    return x > 4


filter(lambda x: x > 4, lst)
print(list(filter(func, lst)))

print(list(filter(lambda x: x < 3, lst)))

lst = ["三国演义", "水浒传", "红楼梦", "西游记", "白蛇传", "还珠格格", "聊斋"]
print(list(filter(lambda x: len(x) > 3, lst)))
#
# lst = [{'id': 1, 'name': 'alex', 'age': 17},
#        {'id': 1, 'name': 'alex', 'age': 16},
#        {'id': 1, 'name': 'alex', 'age': 15}]
# print(list(filter(lambda x: x['age'] > 15, lst)))
#
# # map()  # 映射
# # map(函数,可迭代对象)
# lst = [1, 2, 3]
# lst2 = [1, 2, 3]
# lst3 = [1, 2, 3]
#
#
# def foo(x):
#     return str(x)
#
#
# print(list(map(lambda x, y, z: (str(x), str(y), str(z)), lst, lst2, lst3)))  # 批量处理
# lst = [1, 2, 3, 4, 5]
# print(list(map(str, lst)))
#
# # sorted(可迭代对象,key=排序规则)  # 排序
# # list.sort
# lst = [1, 2, 3, 4, 5, 6, 7, -8]
# lst.sort(reverse=True)
# print(lst)
# print(sorted(lst, reverse=True, key=(lambda x: abs(x))))
# print(sorted(lst, reverse=True, key=abs))
# lst = ["三国演义义义义", "水浒传传传", "红楼梦梦", "西游记记", "白蛇传", "还珠格格", "聊斋"]
# print(sorted(lst, key=len))
# dic = {1: 'a', 2: 'cd'}
# print(sorted(dic.values(), key=len, reverse=True))
#
# # max() 求最大值 min() 求最小值
# print(max([1, 2, 3, 4], key=abs))
#
lst = [1, 2, 3, 4, 5]
from functools import reduce


def func(x, y):
    return x * y


print(reduce(func, lst))
