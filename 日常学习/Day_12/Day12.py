#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project:MyPythonLearn
# Product:PyCharm
# User:Gei
# Author: Gesiz
# Createtime: 2020/10/14 16:32

# re : 正则表达式
# 正则的作用从字符串中获取内容
name = "aleexe"
print(name[name.find("e")])
import re

name = "asdad1AA23123**&&…………%%sasdasd2"
print(re.findall("e", name))  # 无内容则为空列表

print("".join(re.findall("\w", name)))  # \w 匹配中文 英文 数字
print("".join(re.findall("\W", name)))  # \W 匹配特殊符号

print("".join(re.findall("\s", name)))  # \s 匹配空白符
print("".join(re.findall("\S", name)))  # \S 匹配不是空白符

print("".join(re.findall("\d", name)))  # \d 匹配数字
print("".join(re.findall("\D", name)))  # \D 匹配不是数字

print("".join(re.findall("\Aa", name)))
print("".join(re.findall("^a", name)))  # \s 匹配以什么开头

print(re.findall("2\Z", name))
print(re.findall("2$", name))  # 匹配以什么结尾

print(re.findall(".", name))  # 匹配所有 除了换行符
print(re.findall(".", name, re.DOTALL))  # 匹配所有

print(re.findall("[0-9]", name))  # \d
name = "asdasdAS--DasD"
print(re.findall("[A-Z]", name))
print(re.findall("[a-z]", name))
print(re.findall("[A-Za-z0-9]", name))
print(re.findall("[-]", name))  # 减号只能放到前面
name = "asdasdASDasD1231&&^^**23AA"
print(re.findall("[^a-z0-9A-Z]", name))  # [^] 取反 不要az09AZ

print(re.findall("d*", name))  # 匹配零个或多个 e*0 或 e*n 贪婪匹配
print(re.findall(".*", name))

name = "asdaabc123123abcseeedASDasD1231&&^^**23AA"
print(re.findall("e+", name))  # 匹配e*1 或 e*n 贪婪匹配
print(re.findall("e?", name))  # 匹配0个或1个   非贪婪匹配

print(re.findall("e{3}", name))  # 精确匹配

print(re.findall("e{1,10}", name))  # 区间匹配

print(re.findall("e|a", name))  # 匹配a或者b

print(re.findall("abc(\d+)abc", name))  #

s = 'alex_sb ale123_sb wu12sir_sb wusir_sb ritian_sb'
print(re.findall("(\w+)_sb", s))
print(re.findall("(.+?)_sb", s))

s = '1-2*(60+(-40.35/5)-(-4*3))'
print(re.findall("\d+", s))
print(re.findall("-\d+", s))
print(re.findall("-\d+|\d+", s))
print(re.findall("-\d+\.\d+", s))
s = '这是我123121123@qq.comaasdasd'
print(re.findall("\d+@\w+\.com", s))
s = "15566529696"
print(re.findall("^1[3-9]\d{9}", s))
s = "10001 10002 10000"
print(re.findall("\d{5,11}", s))
s = '''
时间就是1995-04-27,2005-04-27
1999-04-27 老男孩教育创始人
老男孩老师 alex 1980-04-27:1980-04-28
2018-12-08
'''
print(re.findall("\d{4}-\d{2}-\d{2}", s))

# print(re.findall('href="(.*?)"', s))

# 重点
s = "alexabce"
# print(re.search("e", s).group())  # 获得对象 分组  # search 是从任意位置进行匹配 匹配到一个元素就停止匹配
# print(re.match("e", s).group())  # match 是从字符串的开头进行匹配 ^e 匹配不到时 返回None
s = "ale,xa.b c?e"
print(re.split("[,. ?]", s))
s = "barry"
print(re.sub("barry", "meet", s))
s = "asdasdasdasd123123"
obj = re.compile("\d+")  # 定义规则 直接使用即可
obj.findall(s)

g = re.finditer('href="(.*？)"', s)  # 返回一个迭代器

# def out(s):
#     def wrapper(h):
#         def inner(*args, **kwargs):
#             print("被修饰前")
#             ret = h(*args, **kwargs)
#             print("被修饰后")
#             return ret
#         return inner
#     return wrapper
#
#
# @out(False)
# def func():
#     print("被修饰内容")
#
# func()

# logging : 日志

# 1 记录程序执行的状态
# 2 记录一些重要信息
# 3 热推
# 4 人喜好分析
# 时间 级别 文件 错误信息

# 基础版本
# import logging
#
# logging.basicConfig(
#     level=10,  # 从十级别开始记录 debug 记录级别
#     format="%(asctime)s %(levelno)s %(filename)s 错误信息 %(message)s ",  # 记录格式 会覆盖
#     filename="test",
#     filemode="a",
#
#
# )
# logging.debug("is debug")  # 调试
# logging.info("is info")  # 信息
# logging.warning("is warning")  # 警报  默认从警报开始记录
# logging.error("is error")  # 错误
# logging.critical("is critical")  # 危险
# # 存储在文件中时 不能以utf-8形式储存
# # 储存在文件的同事在屏幕上打印

# 自定义日志
# import logging
#
# loger = logging.Logger("loger")  # 创建了一个空盒
# f = logging.FileHandler(filename="test1.log", mode="a+", encoding="utf-8")  # 创建一个文件句柄
# s = logging.StreamHandler()
# format = logging.Formatter("%(asctime)s %(levelno)s %(filename)s 错误信息 %(message)s")
# format2 = logging.Formatter("%(asctime)s %(levelno)s  错误信息 %(message)s")
# # 储存到文件和屏幕时使用的结构
# loger.setLevel(logging.ERROR)  # 从某个程度开始记录
# f.setFormatter(format)  # 给文件句柄绑定储存数据是使用的样式
# s.setFormatter(format2) # 给屏幕绑定显示数据的样式
# loger.addHandler(f)  # 把文件句柄与loger对象进行绑定
# loger.addHandler(s)  # 把屏幕句柄与loger对象进行绑定
# loger.info("你好")

from mylogger import loggin

try:
    int(input())
except Exception:
    loggin().error("类型转换错误")
