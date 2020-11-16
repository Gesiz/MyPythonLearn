#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project:MyPythonLearn
# Product:PyCharm
# User:Gei
# Author: Gesiz
# Createtime: 2020/9/6 10:06

# 昨日复习
# 列表 -- 储存大量数据 可变 有序 可以春村不同数据类型
# 增 append insert extend
# 删 pop del remove
# 改 list[索引] = "值"
# 查 索引 for
# 其他操作 sort 升序 reverse 反转 sort(reverse =True)

# 字典 -- 存储大量数据 可变 无序 查询速度快 键值对数据 可以让数据与数据间 产生关联 {}
# 增 字典[键位] = 值
# 删 字典.pop(键)
# 改 字典[键] = 值
# 查 字典[键] for循环 字典.get(键)
# 其他操作 获取所有的键位 字典.keys 获取所有的值 字典.values 获取所有的键值对 字典.item

# Python 有八个大数据类型

# 集合 --set --无序(不支持索引) --可变 {} set() 空集合
# 集合 -- 作用 -- 去重

# 集合中可变的数据类型 不能当做元素
# 集合中元素必须是不可变的

s = {"key", "key2", "key"}
print(type(s))
print(s)

# 增
s.add(123)
print(s)
s.update("alex")
print(s)

# 删
s.remove("key2")
s.pop()  # 随机删除

# 改 先删除 后修改 或者 数据类型转换 列表<-->集合
lst = list(s)
lst[-1] = "key3"
s1 = set(lst)
print(s1)

# 查 for循环

s = {"key", "key2", "key"}
for i in s:
    print(i)

# 其他操作
s1 = {1, 2, 3, 4, 5}
s2 = {5, 2, 12, 34, 12}
s3 = {51, 21, 12, 34, 12}
print(s1 & s2)  # 交集 查看出来方都有的数据
print(s2 - s1)  # 差 查看我有你没有的数据
print(s1 | s2 | s3)  # 并集 所有数据集合
print(s1 ^ s2)  # 补集 反交集
print(s2 > s1)  # bool 超集 完全包含

s1 = {1, 2, 3, 4}
s2 = {5, 6, 7}
s1 = s2
print(s1)

# 更多数据类型

# 深浅拷贝
# is not
# == 判断两边值是否相同
a = 10
b = 10
print(a == b)  # 判断两边的值是否一致
print(a is b)  # 判断a和b的内存地址是否相同

print(id(a), id(b))

# 小数据池
# 数字 -5~256
# 字符串 自己定义的内容一致
# https://cnblogs.com/guobaoyuan/p/9833517.html
dic = {"k": "alex", "b": "alex"}
for i in dic:
    print(i)
    print(dic[i])

a = 257
b = 257
print(a is b)

# z驻留机制 节省内存开销 提高效率
# 小数据池
# 终端执行的事小数据池
# pycharm 执行的是代码块

# 赋值 多个变量名执行同一个内存地址

a = 10
b = 10
c = 10

a1 = 10
b1 = a1
c1 = b1

# 浅拷贝 只拷贝第一层元素的内存地址
lst = [1, 2, 3, []]

a = [1, 2]
a[1] = a
print(a[1])

lst = [1, 2, 3, []]
lst1 = lst.copy()  # 浅拷贝

lst[-1].append(5)

print(lst, id(lst))
print(lst1, id(lst1))

s = {"key", "key2"}
print(type(s))
# 集合中可变数据类型不可当做元素 自动去重 无序 集合是可变的
# 增加
s.add(12)
print(s)
s.update("alex")  # 迭代添加
# 删除
s.remove("key2")
print(s)

s.pop()  # 随机删除 因为集合是无序的
print(s)

# 改 集合无法定位
# 集合先删 后改 数据类型转换

lst = list(s)
print(lst)
lst[-1] = "key3"
s1 = set(lst)
# 查
for i in s:
    print(i)  # 无序

# 其他操作
s1 = {1, 2, 3, 4, 5}
s2 = {5, 2, 12, 34, 12}

print(s1 & s2)  # 交集
print(s2 - s2)  # 差集
print(s1 | s2)  # 并集
print(s1 ^ s2)  # 补集合 看两方没有的
print(s2 > s1)  # 包含 bool   # 超集
print(s2 < s1)  # bool       # 子集

lst1 = [1, 2, 3, 4]
lst2 = [12, 312, 32, 4]
# 集合可以使用这些操作

