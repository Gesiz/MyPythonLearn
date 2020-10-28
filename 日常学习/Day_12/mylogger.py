#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project:MyPythonLearn
# Product:PyCharm
# User:Gei
# Author: Gesiz
# Createtime: 2020/10/16 19:56

import logging

def loggin():
    loger = logging.Logger("loger")  # 创建了一个空盒
    f = logging.FileHandler(filename="test1.log", mode="a+", encoding="utf-8")  # 创建一个文件句柄
    s = logging.StreamHandler()
    format = logging.Formatter("%(asctime)s %(levelno)s %(filename)s 错误信息 %(message)s")
    format2 = logging.Formatter("%(asctime)s %(levelno)s  错误信息 %(message)s")
    # 储存到文件和屏幕时使用的结构
    loger.setLevel(logging.INFO)  # 从某个程度开始记录
    f.setFormatter(format)  # 给文件句柄绑定储存数据是使用的样式
    s.setFormatter(format2)  # 给屏幕绑定显示数据的样式
    loger.addHandler(f)  # 把文件句柄与loger对象进行绑定
    loger.addHandler(s)  # 把屏幕句柄与loger对象进行绑定
    # loger.info("你好")
    return loger