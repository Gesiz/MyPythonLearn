#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project:MyPythonLearn
# Product:PyCharm
# User:Gei
# Author: Gesiz
# Createtime: 2020/9/6 0:23

# 选择排序 由于python的特殊性可通过 min(iList[i:]) 获得最小值 因此在所有排序算法中选择排序最快

from randomList import randomList
import timeit

iList = randomList(20)


def selectionSort(iList):
    if len(iList) <= 1:
        return iList

    for i in range(0, len(iList) - 1):
        if iList[i] != min(iList[i:]):
            minIndex = iList.index(min(iList[i:]))
            iList[i], iList[minIndex] = iList[minIndex], iList[i]
    return iList


if __name__ == "__main__":
    print(selectionSort(iList))

# iList = randomList(20)
#
#
# def selectionSort(iList):
#     if len(iList) <= 1:
#         print("error")
#
#     for i in range(0, len(iList)-1):
#         if iList[i] != min(iList[i:]):
#             minIndex = iList.index(min(iList[i:]))
#             iList[i], iList[minIndex] = iList[minIndex], iList[i]
#     return iList
#
#
# if __name__ == "__main__":
#     print(selectionSort(iList))

# def selectionSort(iList):
#     if len(iList) <= 1:
#         print("不满足条件")
#     for i in range(0, len(iList) - 1):
#         if iList[i] != min(iList[i:]):
#             minIndex = iList.index(min(iList[i:]))
#             iList[i, iList[minIndex]] = iList[minIndex], iList[i]
#         return iList

# def selectionSort(iList):
#     if len(iList) <= 1:
#         return iList
#     for i in range(0, len(iList)-1):
#         if iList[i] != min(iList[i:]):
#             minIndex = iList.index(min(iList[i:]))
#             iList[i], iList[minIndex] = iList[minIndex], iList[i]
#     return iList
#
#
# if __name__ == "__main__":
#     print(iList)
#     print(selectionSort(iList))
#     print(timeit.timeit("selectionSort(iList)", "from __main__ import selectionSort, iList", number=100))
