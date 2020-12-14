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
# while True:
#     test_str = input('请输入（字符串只包含小写字母且长度不小于2且，不超过10000）：')
#     str_len = len(test_str)
#     r = False
#     for i in range(0, str_len):
#         p = test_str[0:i]
#         if i:
#             if not str_len % (i):
#                 res = p*int(str_len/(i))
#                 if res == test_str:
#                     r = True
#                     break
#     print(r)

# 写代码：用户输入一个字符串, 打印 该字符串中字符的所有组合.
# def perm(s=''):
#     # 这里是递归函数的出口，为什么呢，因为这里表示：一个长度为1的字符串，它的排列组合就是它自己。
#     if len(s) <= 1:
#         return [s]
#     sl = []  # 保存字符串的所有可能排列组合
#     for i in range(len(s)):  # 这个循环，对应 解题思路1）确定字符串的第一个字母是谁，有n种可能（n为字符串s的长度
#         for j in perm(s[0:i] + s[i + 1:]):  # 这个循环，对应 解题思路2）进入递归，s[0:i]+s[i+1:]的意思就是把s中的s[i]给去掉
#             sl.append(s[i] + j)  # 对应 解题思路2）问题就从“返回字符串中的字母排列组合” **变成了** “返回 第一个字母+除去第一个字母外的字符串的排列组合”
#     return sl
#
#
# def main():
#     perm_nums = perm('abb')  # 有可能存在字母相同的情况
#     no_repeat_nums = list(set(perm_nums))  # 去重，挺牛的，这个代码
#     print('perm_nums', len(perm_nums), perm_nums)
#     print('no_repeat_nums', len(no_repeat_nums), no_repeat_nums)
#     pass
#
#
# if __name__ == '__main__':
#     main()


# def binarySearch(arr, l, r, x):
#     # 基本判断
#    if r >= l:
#         mid = (l + (r-1)) // 2
#         if arr[mid] == x:
#             return mid
#         elif arr[mid] > x:
#             return binarySearch(arr, l, mid - 1, x)
#
#         else:
#             return binarySearch(arr, mid + 1, r, x)
#    else:
#        return False
#
#
# # 测试数组
# arr = [2, 3, 4, 10, 40]
# x = 10
#
# # 函数调用
# result = binarySearch(arr, 0, len(arr) - 1, x)
#
# if result != -1:
#     print("元素在数组中的索引为 %d" % result)
# else:
#     print("元素不在数组中")