#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project:MyPythonLearn
# Product:PyCharm
# User:Gei
# Author: Gesiz
# Createtime: 2020/9/27 22:05


# 装饰器 器: 工具  在不修改源代码及其调用方式的前提下 额外增加新的功能
# 开发封闭原则
# 对源代码及其调用方式是封闭的

# import time
#
# start_time = time.time()
#
#
# def func():
#     print("this is a write code")
#
#
# def foo():
#     print("this is b write code")
#
#
# def f1():
#     print("this is c write code")
#
#
# def run_time(f):
#     def inner():
#         start_time = time.time()
#         f()
#         time.sleep(2)
#         stop_time = time.time()
#         print(f"运行时间为{stop_time - start_time}")
#
#     return inner
#
#
# func = run_time(func)
# func()


# 标准版 装饰器
# def wrapper(func):
#     def inner(*args, **kwargs):
#         """执行装饰器前"""
#         func(*args, **kwargs)
#         print(args, kwargs)
#         """执行装饰器后"""
#
#     return inner
#
#
# def func(*args, **kwargs):
#     print(111)
#
#
# func = wrapper(func)
# func(20, 1, a=1, b=2)

#
# def wrapper(func):
#     def inner(*args, **kwargs):
#         ret = func(*args, **kwargs)
#         return ret
#
#     return inner
#
#
# @wrapper  # 语法糖
# def tb(money):
#     print("花钱了")
#     return money
#
#
# # tb = wrapper(tb)
# a = tb(100)
# print(a)


# 模拟打游戏 王者

# def gua(func):
#     def inner(*args, **kwargs):
#         print("kai")
#         ret = func(*args, **kwargs)
#         print("guan")
#         return ret
#     return inner
#
#
# @gua
# def game(rou):
#     print("打开游戏")
#     print(f"选资额{rou}")
#     return True
#
#
# ret = game("you")
#
# if ret == True:
#     print("go on")
# else:
#     print("stop")

# 有参装饰器
# def wrapper(func):  # func 接收到的是被装饰的函数
#     def inner(*args, **kwargs):  # 被装饰函数需要的参数
#         ret = func(*args, **kwargs)
#         return ret
#
#     return inner
#
# def auth(arg):
#     def wrapper(func):
#         def inner(*args, **kwargs):  # func 接收的是被装饰的函数
#             if arg:
#                 print("开始装饰")
#                 ret = func(*args, **kwargs)  # *args **args被装饰函数需要的参数
#                 print("停止装饰")
#             else:
#                 ret = func(*args, **kwargs)  # *args **args被装饰函数需要的参数
#             return ret  # ret是被装饰的函数的返回值
#
#         return inner
#
#     return wrapper
#
#
# @auth(False)  # func = auth(func)(10)
# def func(a):
#     print(a)
#
#
# func(10)


# 递归5
# 1 不断地调用自己本身
# 2 有明确的终止条件从

# 递归的最大深度 官方测试1000

# num = 0
#
# def func():
#     global num
#     print(num)
#     num = num + 1
#     func()
#
#
# func()

def func(n):
    if n == 3:
        return
    return func(n + 1)


func(1)

meet = ["1", "2", ["3", "4", ["5", "6"]]]


def func(m):
    for i in m:
        if type(m) == list:
            func(i)
        else:
            print(i)


func(meet)
