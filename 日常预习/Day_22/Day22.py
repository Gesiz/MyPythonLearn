#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project:MyPythonLearn
# Product:PyCharm
# User:Gei
# Author: Gesiz
# Createtime: 2020/10/31 12:21


# udp 复习
# from socket import *
#
# s = socket(AF_INET, SOCK_DGRAM)
# s.bind(("", 8881))
#
# while True:
#     data = s.recvfrom(1024)
#     print(data[0].decode("gb2312"))
#     s.sendto(data[0], data[1])

a = 'I love PythonSomething!'
b = 'I love PythonSomething!'
c = [1, 2, 3]
d = [1, 2, 3]
a = 'I love PythonSomething!'
b = 'I love PythonSomething!'
c = [1, 2, 3]
d = [1, 2, 3]
print(a is b)
print(c is d)


