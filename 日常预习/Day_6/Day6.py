#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project:MyPythonLearn
# Product:PyCharm
# User:Gei
# Author: Gesiz
# Createtime: 2020/9/18 12:50

# 函数的作用
# 1 减少重复代码
# 2 提高重用性

# 计算字符的长度 不能使用len方法
s = "alex"
count = 1
for i in s:
    count += 1
print(count)

lst = [1, 2, 3, 4, 5]
count = 0
for i in lst:
    count += 1
print(count)

# 计算字典的长度
dic = {}
count = 0
for i in dic:
    count += 1
print(count)

# 函数的定义
# def -- 关键字
# def 函数名()
#       函数体

s = "alex"


def my_len():
    count = 0
    for i in s:
        count += 1
    print(count)


# 只有函数被调用的时候函数体中的代码才会执行
# 写函数实现功能 其实就是给功能加一个外壳

# 调用函数 :
# 函数名+()

s = [1, 22, 3, 4, 5, 6]
my_len()

print("函数已经走过了")
my_len()


def func():
    with open("info", "r", encoding="utf-8") as f:
        for i in range(3):
            f.seek(0)
            user = input("请输入账号")
            pwd = input("请输入密码")
            for i2 in f:
                file_user, file_pwd = i2.strip().split(":")
                if user == file_user and pwd == file_pwd:
                    return True
                else:
                    return False


# return 不写的时候默认返回None
# return 能够终止函数
# return 能返回python中 所有的对象 python 中一切的对象
# return 同时返回多个数据 以元组的形式

# 函数的参数
def car(app, addr, carfu):  # 形参
    return f"{app},{addr}，{carfu}"


ret = car("1", "2", "3")  # 实参


# 参数
# 形参 在函数定义
# 实参 在函数调用
# 位置参数 必须一一对应
# 混合参数 位置和关键字一起使用

def func(a, b=10):  # 默认参数
    return a if a > b else b

# 形参 在函数的定义部分
# 实参 在函数的调用部分

# 位置参数
# def func(a,b)
# 默认参数
# def fun(a=1,b=2)
# 混合参数



