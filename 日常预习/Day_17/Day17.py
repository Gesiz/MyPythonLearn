#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project:MyPythonLearn
# Product:PyCharm
# User:Gei
# Author: Gesiz
# Createtime: 2020/10/24 15:18

# 反射

# class A():
#     def __init__(self, name):
#         self.name = name
#
#     def func(self):
#         print("hello")
#
#     # def __getattr__(self, item):  # 当对象空间中 有属性时不执行这个方法
#     #     return "没有当前值"
#
#     def __setattr__(self, key, value):
#         print("设置值时走此")
#         self.__dict__[key] = value
#
#     def __delattr__(self, item):
#         print("删除的时候执行我")
#         self.__dict__.pop(item)
#
#
# a = A("alex")


# print(a.age)
# b = input("请输入你想运行的函数")
# if getattr(a, b) == "没有当前值":
#     print("没有该函数")
# else:
#     getattr(a, b)()

# if hasattr(a, b):  # 判断属性是否存在 返回的是布尔值  推荐
#     getattr(a, b)()
# else:
#     print("没有该函数")
# print(getattr(a,b,"没有该函数"))

# if getattr(a,b,None):
#     getattr(a,b)
# else:
#     print("没有该函数")
# for i in range(3):
#     msg = input("请输入您要封装的属性及值格式如下[age|10]:")
#     k, v = msg.split("|")
#     setattr(a, k, v)
#     print(a.__dict__)

# delattr(a, "name")

# hasattr(对象名,"字符串属性名")  # 判断属性在对象是否存在
# hasattr(a,"name")
# getattr(对象名,"要获取的属性名","找不到时返货的提示语句")
# getattr(a,"name","没有")

# setattr(对象名,"要设置的属性名",要设置的值)
# setattr(a,"name","alex")

# delattr(对象名,"要删除的属性名")
# delattr(a,"name")


# class User:
#     def login(self):
#         print("登录")
#
#     def register(self):
#         print("注册")
#
#     def save(self):
#         print("存储")
#
#
# user = User()
#
# msg = """
# login
# register
# save
# """
# choose = input(msg)
# if hasattr(user, choose):
#     getattr(user, choose)()
# else:
#     print("输入有误")
#


# def func():
#     print("is func")
#
#
# name = "meet"
#
#
# def foo():
#     print("is func")
#
#
# msg = input("请输入您要执行的函数")
#
# # print(globals())
#
# # if msg in globals():
# #     globals()[msg]()
# # else:
# #     print("没有")
#
# import sys
#
# obj = sys.modules[__name__]
# if hasattr(obj, msg):
#     getattr(obj, msg)()
# import time
#
# obj = time
# if hasattr(obj, "time"):
#     print(getattr(obj, "time")())
# else:
#     print("nothing")
# s = "alex"
# if hasattr(s, "upper"):
#     print(getattr(s, "upper")())
# else:
#     print("nothing")
#
# lst = [1, 2, 33, 4, 25, 6, 17, 8, 9]
# if hasattr(lst, "sort"):
#     getattr(lst, "sort")()
#     print(lst)

# 异常处理

# 异常 错误导致程序中断 不能正常运行
# 异常分为两种
# 语法错误 print( if  无法捕获 只能避免
# 逻辑错误 int("") 可以捕获

# 异常处理 发现错误 及时制止使 程序能够继续运行
# if 3>2

# if 3 > 2:
#     try:
#         print(int("q"))
#     except Exception as e:
#         print(e)
#
# print(123)
#
# # 异常的分类
# try:
#     int("q")
# except KeyError:
#     print(1)
# except IndexError:
#     print(2)
# except ValueError:
#     print(3)
# else:
#     print(666)

try:
    # print(int("q"))
    raise TypeError("有错误")  # 主动异常
except KeyError:
    print(1)
except IndexError:
    print(2)
except ValueError:
    print(3)
except Exception:
    print(5)
else:
    print(666)
finally:
    print(7)  # 进行清理工作


class MeetException(BaseException):
    def __init__(self, msg):
        self.msg = msg

    # def __str__(self):
    #     return "啦啦啦"


try:
    raise MeetException("这是一个异常")
except MeetException as e:
    print(e)
# if 1 == 2:
#     print()
# assert 1 == 2  # 断言 抛出不等于错误 比if硬

try:
    assert 1 == 1
except AssertionError:
    print("条件不成立")
else:
    print("条件成立")

a = 10
b = 20
try:
    assert a == b
except AssertionError:
    print("条件不成立")

