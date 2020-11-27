#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project:MyPythonLearn
# Product:PyCharm
# User:Gei
# Author: Gesiz
# Createtime: 2020/9/4 0:21

from randomList import randomList
import timeit

iList = randomList(20)


def bubbleSort(iList):
    if len(iList) <= 1:
        return iList
    for i in range(1, len(iList)):
        for j in range(0, len(iList) - i):
            if iList[j] <= iList[j + 1]:
                iList[j], iList[j + 1] = iList[j + 1], iList[j]
    return iList

# def bubbleSort(iList):
#     for i in range(1,len(iList)-1):
#         for j in range(0,len(iList)-i):
#             if iList[j] > iList[j+1]:
#                 iList[j],iList[j+1] = iList[j+1],iList[j]
#     return iList


#
# def bubbleSort(iList):
#     for i in range(1, len(iList) - 1):
#         for j in range(0, len(iList) - i):
#             if iList[j] <= iList[j + 1]:
#                 iList[j], iList[j + 1] = iList[j + 1], iList[j]
#     return iList


if __name__ == "__main__":
    print(bubbleSort(iList))

    # def bubbleSort(iList):
#     if len(iList) <= 1:
#         return iList
#     for i in range(1, len(iList)):
#         for j in range(0, len(iList) - i):
#             if iList[j] <= iList[j + 1]:
#                 iList[j], iList[j + 1] = iList[j + 1], iList[j]
#     return iList
#
#
# if __name__ == "__main__":
#     print(bubbleSort(iList))

# def bubbleSort(iList):
#     if len(iList) <= 1:
#         print("不满足")
#
#     for i in range(1, len(iList)):
#         for j in range(0, len(iList) - i):
#             if iList[j] <= iList[j + 1]:
#                 iList[j], iList[j + 1] = iList[j + 1], iList[j]
#     return iList
#
#
# if __name__ == "__main__":
#     print(bubbleSort(iList))
# iList = randomList(20)
#
#
# def bubbleSort(iList):
#     if len(iList) <= 1:
#         print("长度不够 重新输入")
#
#     for i in range(1, len(iList)):
#         for j in range(0, len(iList) - i):
#             if iList[j] <= iList[j + 1]:
#                 iList[j], iList[j + 1] = iList[j + 1], iList[j]
#     return iList
#
# if __name__ == "__main__":
#     print(bubbleSort(iList))


# def bubbleSort(iList):
#     if len(iList) <= 1:
#         print("长度不够")
#
#     for i in range(1, len(iList)):
#         for j in range(0, len(iList) - i):
#             if iList[j] >= iList[j + 1]:
#                 iList[j], iList[j + 1] = iList[j + 1], iList[j]
#     return iList
#
#
# if __name__ == "__main__":
#     print(bubbleSort(iList))

#
# iList = randomList(20)
#
#
# def bubbleSort(iList):  # 声明一个冒泡函数的函数名 等待主函数调用
#     """冒泡排序"""
#     if len(iList) <= 1:  # 程序健壮性考虑 对不可靠数据进行过滤
#         return print("列表内数据不足请重新输入")
#
#         for i in range(1, len(iList)):
#             for j in range(0, len(iList)-i):
#                 if iList[j] >= iList[j]:
#                     iList[j], iList[j+1] = iList[j+1], iList[j]
#     return iList
#
#
# if __name__ == "__main__":
#     print(iList)
#     print(bubbleSort(iList))

# iList = randomList(20)
#
# def bubbleSort(iList):
#     """冒泡排序"""
#     if len(iList) <= 1:
#         return iList
#     for i in range(1, len(iList)):
#         for j in range(0, len(iList)-i):
#             if iList[j] >= iList[j+1]:
#                 iList[j], iList[j+1] = iList[j+1], iList[j]
#
#     return iList
#
#
# if __name__ == "__main__":
#     print(iList)
#     print(bubbleSort(iList))
#     print(timeit.timeit("bubbleSort(iList)", "from __main__ import bubbleSort,iList", number=100))
