#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project:MyPythonLearn
# Product:PyCharm
# User:Gei
# Author: Gesiz
# Createtime: 2020/9/22 10:36

# 函数的动态参数


# def func(a, b, *args):  # 元组 在形参位置的 聚合为元组 接收多余位置参数
#     print(args)
#
#
# func(1, 2, 3)

# def func(a, b, c, d, **kwargs):  # 字典 接收多余的关键字参数
#     print(kwargs)
#
#
# func(a=1, b=2, c=3, d=4, e=5)
# def func(a, b, *args, c=1, **kwargs):
#     print(*args)
#
#
# func(1, 2, 3, 4, c=3)
# *args **kwargs 不建议修改

# 名称空间
# 内置空间 存放python 自带的内容
# 全局空间 函数中的空间
# 局部空间 函数体中的空间

# a = 10
#
#
# def func():
#     global a
#     a = a + 1
#     print(a)


# 加载顺序 内置>全局>局部
# 取值顺序 局部>全局>内置


# 函数的嵌套
# 函数的第一类对象及使用
# 函数名可以当做值被赋值
# a = func
# 2 函数名可作为两个函数的返回值
# def foo():
#     def func():
#         print(1)
#
#     return func()
#
#
# a = foo()
# a()


# 3函数名可以作为另一个函数的参数

# 4函数名可以当做值存放到容器中
# def func():
#     print(1)


# lst = [func, func, func]
# for i in lst:
#     i()
#
# # 函数的嵌套分为两种
# # 1 交叉嵌套
# # 2 嵌套
#
# def foo():
#     print(1)
#
# def func():
#     foo()
#
# func()
#

# def foo():
#     print(1111)
#     foo()
# foo()
# a = 10
#
#
# def func(b):
#     b = 5
#
#     def foo():
#         print(b)
#
#     foo()
#
#
# func(a)
# print(a)
#
# print(globals())
#
#
# # def foo():
# #     print(1)
# #     foo()
# # foo()
#
# # global 只修改全局变量
# # global 未声明时 可创建全局变量
# # global() locals()
# def func():
#     global a
#     a = 10
#
#
# func()
# print(a)

# global
# nonlocal 在局部内 修改离nonlocal 最近得一层 如果上一层没有就继续向上查找

a = 10


def func():
    a = 8

    def foo():
        a = 6

        def f1():
            a = 4

            def f2():
                a = 3

                def f3():
                    nonlocal a
                    a += 4

                    print(a)

                f3()

            print(a)
            f2()
            f2()

        print(a)
        f1()

    print(a)
    foo()


print(a)
func()
