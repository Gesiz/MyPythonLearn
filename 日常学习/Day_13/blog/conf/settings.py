#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project:MyPythonLearn
# Product:PyCharm
# User:Gei
# Author: Gesiz
# Createtime: 2020/10/16 21:38

import sys, os

print(__file__)
print(os.getcwd())  # 获取当前工作路径
print(os.path.dirname(os.path.dirname(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
print(os.path.join(BASE_DIR,'db','userinfo'))
print(os.path.join(BASE_DIR,'log','blog.log'))


# 任意地点创建文件