#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project:MyPythonLearn
# Product:PyCharm
# User:Gei
# Author: Gesiz
# Createtime: 2020/9/17 20:03

data_list = []
data = {}
for i in range(10):
    data['user'] = i
    data_list.append(data)
print(data_list)

v1 = [1, 2, 3, 4, 5]
v2 = [v1, v1, v1]
v2[1][0] = 111
v2[2][0] = 222
print(v1)
print(v2)

v1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
v2 = {}
for item in v1:
    if item < 6:
        continue
    if 'k1' in v2:
        v2['k1'].append(item)
    else:
        v2['k1'] = [item]
print(v2)

import copy

v1 = "alex"
v2 = copy.copy(v1)
v3 = copy.deepcopy(v1)
print(id(v1), id(v2), id(v3))

v1 = [1, 2, 3]
v2 = copy.deepcopy(v1)
print(v1 is v2)
# 文件操作的作用 持久化储存
#
# 文件操作 读写
# file = "文件的位置"
# mode = 操作这个文件的模式
# r = read 的缩写
# encoding = “文件存储时使用的编码”
# f为一个变量名 但是被称为文件句柄
f = open(file="File", mode="r", encoding="utf-8")
# c = f.read()  # 全部读取
# print(c)

# d = f.read(6)  # 读取六个字符
# print(d)

e = f.readline()  # 读取一行
print(e)

# 路径文件位置
# 相对路径 相对于某个内容进行查找
# 绝对路径 从磁盘的根本开始查找 C,B,D E:\


# 读字节
# f = open("1.jpg","rb")
# c = f.read()
# 路径转义


# 03 文件操作
# 写 w 清空写 先清空 在追加内容
# a 追加写
# w 和 a模式 的文件存在时不会创建 不存在时会创建文件
f = open("第一次", "w", encoding="utf-8")
f.write("123")  # 必须为字符串
f.close()

f = open("第二次", "a", encoding="utf-8")
f.write("\n今天是星期4")
f.write("\n今天是星期5")
f.close()

f = open("第二次", "r", encoding="utf-8")
print(f.read())

# + 操作及其他操作
# a+ 追加 读写
# w+ 写 读
# r+ 读 加写

f = open("第二次", "r+", encoding="utf-8")
print(f.read())
f.write("啦啦啦")
f.close()

# 写读
f = open("第二次", "r+", encoding="utf-8")
print(f.read())
f.close()

# a+ 自动创建文件 读 写
# 登录 注册
#
# user = input("username: ")
# pwd = input("password: ")
# f = open("userinfo", "a+", encoding="utf-8")
# f.seek(0)
# for i in f:
#     file_user, file_pwd = i.split(":")
#     if user == file_user:
#         print("用户名存在")
#         break
# else:
#     f.write(f"{user}:{pwd}\n")
#     print("可以注册")

# 光标操作 移动光标 查看光标
# 移动光标 seek
# 一个参数 seek(0) 移动到头部 1 移动到当前 2 移动到末尾
# 两个参数 seek(0,0) seek(0,1) seek(0,2)
# 一个参数 seek(3) 按照字节移动

# 产看光标 tell
f = open("第二次", "r", encoding="utf-8")
print(f.read(3))
print(f.tell())

# 文件的另一种打开方式

# 打开文件 操作文件 关闭文件
# with open
with open("第二次", "r", encoding="utf-8") as f, \
        open("第一次", "r", encoding="utf-8") as f1:
    c = f.read()
    print(c)

# with 面向对象 上下文管理
# 文件的修改
# 1 打开文件
# 2 找到修改的内容 进行替换
# 3 写回文件 第二次文件中

import os

with open("第二次", "r", encoding="utf-8") as f, \
        open("第一次", "w", encoding="utf-8") as f1:
    for i in f:
        i = i.replace("alex", "dabai")
        f1.write(i)

os.rename("第二次", "第二次.bak")
os.rename("第一次", "第二次")


