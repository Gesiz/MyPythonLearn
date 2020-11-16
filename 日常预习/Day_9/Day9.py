#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project:MyPythonLearn
# Product:PyCharm
# User:Gei
# Author: Gesiz
# Createtime: 2020/9/23 23:45

# 闭包函数嵌套
# 闭包的作用 就是能够保护数据的安全性及干净性jjjjjjjjjjjjj
# 闭包就是使用非全局变量 且不是本层对象
def foo():
    lst = []  # 变量提升为自由变量

    def func(money):
        lst.append(money)
        print(sum(lst) / len(lst))

    return func


func = foo()

func(20000)
func(30000)


def foo():
    a = []

    def func(num):
        a.append(num)

    return func


#  推导式 编写一些有规律的
lst = []
for i in range(1, 11):
    lst.append(i)
print(lst)
# 普通循环模式
lst = [i for i in range(1, 11, 2)]
print(lst)

# 筛选模式
lst = [i for i in range(1, 11) if i > 5]
print(lst)

lst = [i if i > 3 else "jaja" for i in range(1, 11) if i > 2]
print(lst)

for i in range(3):
    print(i)
    for em in range(2):
        lst.append(em)

lst = [em for i in range(3) for em in range(2)]

# 集合推导式
se = {i for i in range(5)}
se = {i if i > 1 else "rau" for i in range(5) if i > 2}

# 字典推导式
dic = {i: i for i in range(10)}
print(dic)
#  生成器表达式
g = (i for i in range(5))
print(next(g))
print(next(g))
print(next(g))

# 迭代器 可迭代对象
# 1 能被for循环 循环的就是可迭代对象 具有iter方法就是可迭代对象
lst = [1, 2, 3, 4]
new_lst = lst.__iter__()  # 迭代器缺点 使用不灵活 一次性的
print(new_lst.__next__())  # 迭代器优点 节省空间 惰性进制

s = "alex"
s1 = s.__iter__()
while True:
    try:
        print(s1.__next__())
    except StopIteration:  # 异常捕获
        break

f = open("info", "a+", encoding="utf-8")

lst = [1, 2, 3]
new_lst = iter(lst)
print(next(new_lst))


# 生成器 生成器的本质就是迭代器
# 迭代器和生成器的区别
# 迭代器是python内置好的
# 生成器是人为定义的

# 生成器 节省空间 保留执行位置


# 函数
def func():
    return 1


def func():
    print(123)
    yield 1  # yield 是将值返回 并记录执行位置
    print(234)
    yield 2


g = func()  # 产生一个生成器

print(g.__next__())  # 触发生成器执行
print(g.__next__())  # 继续向下执行


# next和yield 数量要一一对应


def func():
    lst = []
    lst.append(1)
    yield lst


g = func()  # 产生一个生成器
print(g.__next__())


def func():
    lst = [i for i in range(2)]
    for i in lst:
        yield i


g = func()
print(g.__next__())
print(g.__next__())


# 当数据量大是建议使用生成器
# 当数据量较大时建议使用

def func():
    lst = [1, 2, 3, 45]
    for i in lst:
        yield i


g = func()
for em in g:
    print(em)


def func():
    lst = [1,2,3,4]
    yield from lst  # 将可迭代对象整个返回


g = func()
for em in g:
    print(em)

# 生成器本身是迭代器
# 生成是人为定义的
# 迭代器是python内置的
# 通过对象内存地址
# 通过send方法进行判断 只有生成器有send guobaoyuan.gitee.io