#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project:MyPythonLearn
# Product:PyCharm
# User:Gei
# Author: Gesiz
# Createtime: 2020/9/17 12:56

s = "alex"
s1 = s.capitalize()
print(s1)

# int
num = 12
num.bit_length()  # 12 占用的有效位 0000 1001

# int + - * /
# float
n = 1.2
print(type(n))  # python javascrript 不可进行小数位精确计算
# list:
# 索引
# 方法
# + 合并
# print(lst + lst2)
# 面试题 资源共享 元组和他一样
lst = [1, 2, 3, []]
lst1 = lst * 2
print(lst1)
lst1[-1].append(10)
lst1[-2] = 10
print(lst1)

# 元组 (10,) () (10,20)
# 字典增删改查
dic = {1: 12, 2: 234}
dic1 = dic.fromkeys("abcd", [])  # 批量创建键值对
print(dic1)
dic1["a"].append(10)
print(dic1)
dic1["a"] = 11

# 字典的合并
dic1 = {1: 2}
dic2 = {2: 3}
dic1.update(dic2)
dic1.update(dic2)
print(dic2)

s = frozenset({"aaa", "bbb"})
dic = {s: '3'}
print(dic)

# coding:utf-8
# is -- 是
# is not -- 不是
# == 判断两边的值是否一致
a = 10
b = 10
print(a == b)  # 判断两边布尔值是否一致
print(a is b)  # 判断a和b的内存地址是否相同
print(id(a), id(b))
# 小数据池 cnblogs.com/guobaoyuan/p/ 数字-5~256 字符串 自己定义内容一致时

a = 257
b = 257
print(a is b)
# 此涉及到代码块 从ide当中为代码块 终端中执行的是 小数据池
# 驻留机制 节省内存开销 增加运行效率

# 赋值 多个变量名 执行同一个内存地址
a = 10
b = 10
c = 10

a1 = 10
b1 = a1
c1 = b1

# 浅拷贝 只拷贝第一层元素的内存地址
lst = [1, 2, 3, []]
lst1 = lst.copy()  # 浅拷贝
print(lst1, id(lst1))
print(lst, id(lst))
print(lst1[0], id(lst1[0]))
print(lst[0], id(lst[0]))
lst[-1].append(5)
print(lst)
print(lst1)

lst = [1, 2, 3, []]
lst1 = lst.copy()  # 浅拷贝
lst.append(5)
print(lst)
print(lst1)

lst = [1, 2, 3, [1, [], 3]]
lst1 = lst[:]
lst1[-1][-2].append(2)
lst1[1] = 10
lst[0] = 20
print(lst)
print(lst1)

import copy

lst = [1, 2, 3, [2, 3]]
lst1 = copy.deepcopy(lst)
# 深拷贝 不管嵌套多少层 不可变数据类型共用 可变数据开辟新空间
lst.append(5)
print(lst)
print(lst1)

lst = [1, 23, 4, [1, ]]
lst1 = copy.deepcopy(lst)
lst[-1] = 10
print(lst)
print(lst1)

# 赋值 多个变量指向同一个内存地址
# 潜拷贝 只拷贝第一层元素 不可变数据类型不会有影响 可变数据类型会有联动效果
# 深拷贝 不管嵌套多少层 不可变数据类型共用 可变数据类型开辟空间

# 二次编码
# 初始编码 ascii() 不支持中文 英文 占一个字节
# 国标 gbk           英文一个字节 中文两个字节
# unicode 万国码 英文中文 四个字节
# utf-8 英文一个 欧洲二个 亚洲三个


# 重点 编码 解码
# 文件存储 和网络传输 使用的都是字节


s = "你好"
s1 = s.encode("utf-8")
print(s1)  # b'\xe4\xbd\xa0\xe5\xa5\xbd'
print(type(s1))
s2 = s1.decode("utf-8")
print(s2)

s = "你好"
s1 = s.encode("gbk")
print(s1)  # b'\xe4\xbd\xa0\xe5\xa5\xbd'
print(type(s1))
s2 = s1.decode("gbk")
print(s2)

s = b"\xc4\xe3"  # bytes类型

s1 = s.decode("gbk")
print(s1)

s = "你好"
s1 = s.encode("utf-8")
print(len(s1))  # 6
print(s1)
s2 = s1.decode("gbk")
print(s2)

# window 默认编码 gbk
# 以什么解码就以什么编码
# bytes 类型
s = "abc,!"
s1 = b"abc,!"
print(s.encode("utf-8"))
# 只能为英文数字 不可为中文 bytes 类型
# bytes == str 类型

s1 = b"alex"
s2 = b"dsb"
print(s1 + s2)
print(s1 * 5)


# 作用
# 1 文件操作 指的用什么编码保存
# 2 网络编程 发送消息智能发送字节类型

