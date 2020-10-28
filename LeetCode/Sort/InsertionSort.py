#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project:MyPythonLearn
# Product:PyCharm
# User:Gei
# Author: Gesiz
# Createtime: 2020/9/23 23:47

from randomList import randomList
import timeit

iList = randomList(4)


def insertionSort(iList):
    if len(iList) <= 1:
        return iList
    count = 0
    for right in range(1, len(iList)):
        target = iList[right]
        for left in range(0, right):
            if target <= iList[left]:
                print(f"当 target {target}<= iList[left] 时 {iList[left + 1:right + 1]}++++{iList[left:right]} 前 {iList}")
                iList[left + 1:right + 1] = iList[left:right]
                print(f"当 target {target}<= iList[left] 时 {iList[left + 1:right + 1]}++++{iList[left:right]} 中 {iList}")
                iList[left] = target
                print(f"当 target {target}<= iList[left] 时 {iList[left + 1:right + 1]}++++{iList[left:right]} 后 {iList}")
                break
        print(f"这是第{count}次循环 Left列表为{iList[:right]} Right列表为{iList[right:]}")
        print(iList)
        count += 1
    return iList


if __name__ == "__main__":
    print(iList)
    print(insertionSort([431, 321, 213, 123]))
    # print(timeit.timeit("insertionSort(iList)", "from __main__ import insertionSort,iList", number=100))
