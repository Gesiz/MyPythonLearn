#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project:MyPythonLearn
# Product:PyCharm
# User:Gei
# Author: Gesiz
# Createtime: 2020/10/31 13:09

# 对于一个非空字符串,判断其是否可以有一个子字符串重复多次组成,字符串只包含小写字母且长度不超过10000
#  	示例1:
#
# 1.  输入"abab"
# 2.  输出True
# 3.  样例解释: 输入可由"ab"重复两次组成
#
# 示例2:
#
# 1.  输入"abcabcabc"
# 2.  输出True
# 3.  样例解释: 输入可由"abc"重复三次组成
#
# 示例3:
#
# 1.  输入"aba"
# 2.  输出False
while True:
    test_str = input('请输入（字符串只包含小写字母且长度不小于2且，不超过10000）：')
    str_len = len(test_str)
    r = False
    for i in range(0, str_len):
        p = test_str[0:i]
        if i:
            if not str_len % (i):
                res = p*int(str_len/(i))
                if res == test_str:
                    r = True
                    break
    print(r)