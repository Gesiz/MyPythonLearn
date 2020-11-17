#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project:MyPythonLearn
# Product:PyCharm
# User:Gei
# Author: Gesiz
# Createtime: 2020/9/4 0:27

import random


def randomList(n):  # 声明一个用来返回随机列表的函数
    iList = [random.randint(1, 1001) for i in range(n)]  # 声明一个空列表用来存放一会产生的随机数据
    return iList  # 将处理好的列表返回到需要的地方


if __name__ == "__main__":
    iList = randomList(10)
    print(iList)

# def randomList(n):  # 执行help(文件.函数)可查询该函数帮助内容
#     """返回一个长度为n的整数列表,数据范围[0,1000]"""
#     iList = []
#     for i in range(n):
#         iList.append(random.randrange(0, 1000))
#     return iList
#
#
# if __name__ == "__main__":
#     iList = randomList(10)
#     print(iList)
