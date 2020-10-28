#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project:MyPythonLearn
# Product:PyCharm
# User:Gei
# Author: Gesiz
# Createtime: 2020/10/21 13:11


# 依赖关系

# class Elephant:
#     def __init__(self, name):
#         self.name = name
#
#     def open(self, obj):
#         obj.open_door()
#
#     def close(self, obj):
#         obj.close_door()
#
#
# class Medi:
#     def open_door(self):
#         print("冰箱门被打开")
#
#     def close_door(self):
#         print("冰箱门被关闭")
#
#
# class Haier:
#     def open_door(self):
#         print("冰箱门被打开")
#
#     def close_door(self):
#         print("冰箱门被关闭")
# 78
#
# m = Medi()
# f = Elephant("小飞象")
# f.open(m)

# class inst():
#     def knief(self):
#         raise Exception("没有该函数 有问题")
#
#
# class Person(inst):
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp
#
#     def knief(self, obj):
#         print(f"{self.name}划了{obj.name}一刀{obj.name}掉了10滴血")
#
#
# class Police(Person):
#     call = "警察"
#
#     def __init__(self, name, hp, job):
#         super().__init__(name, hp)
#         self.job = job
#
#
# class Bandit(Person):
#     call = "土匪"
#
#     def __init__(self, name, hp, job):
#         super().__init__(name, hp)
#         self.job = job
#
#
# class AK():
#     def __init__(self):
#         self.ak = 90
#
#     def fire(self, obj, obj1):
#         print(f"{obj.name}打{obj1.name}打掉了{obj1.name}90滴血")
#
#
# p1 = Police("海豹", 100, "警察")
# b1 = Bandit("座山雕", 100, "土匪")
# a1 = AK()
# a1.fire(p1, b1)
# p1.knief(b1)

# class inst():  # 这部分是演示依赖
#     def knief(self):
#         raise Exception("没有该函数 有问题")
#
#
# class Person(inst):
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp
#
#     def knief(self, obj):
#         print(f"{self.name}划了{obj.name}一刀{obj.name}掉了10滴血")
#
#     def fire(self, ak1, obj):
#         self.ak1 = ak1
#         self.obj = obj
#         ak1.fire(self, obj)
#
#
# class Police(Person):
#     call = "警察"
#
#     def __init__(self, name, hp, job):
#         super().__init__(name, hp)
#         self.job = job
#
#
# class Bandit(Person):
#     call = "土匪"
#
#     def __init__(self, name, hp, job):
#         super().__init__(name, hp)
#         self.job = job
#
#
# class AK():
#     def __init__(self):
#         self.ak = 90
#
#     def fire(self, obj, obj1):
#         print(f"{obj.name}打{obj1.name}打掉了{obj1.name}90滴血")
#
#
# # p1 = Police("海豹", 100, "警察")  #
# # a1 = AK()
# # b1 = Bandit("座山雕", 100, "土匪")
# # p1.fire(a1, b1)

# class inst():  # 这部分是演示组合
#     def knief(self):
#         raise Exception("没有该函数 有问题")
#
#
# class Person(inst):
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp
#
#     def knief(self, obj):
#         print(f"{self.name}划了{obj.name}一刀{obj.name}掉了10滴血")
#
#
# class Police(Person):
#     call = "警察"
#
#     def __init__(self, name, hp, job, ak1):  # 这一波叫做组合
#         super().__init__(name, hp)
#         self.job = job
#         self.ak1 = ak1
#
#     def fire(self, obj):
#         self.ak1.fire(self, obj)
#
#
# class Bandit(Person):
#     call = "土匪"
#
#     def __init__(self, name, hp, job):
#         super().__init__(name, hp)
#         self.job = job
#
#
# class AK():
#     def __init__(self):
#         self.ak = 90
#
#     def fire(self, obj, obj1):
#         print(f"{obj.name}打{obj1.name}打掉了{obj1.name}90滴血")
#
#
# # 实例化一个枪对象
# ak1 = AK()
# # 首先实例化一个警察对象
# p1 = Police("火凤凰", 100, "特种兵", ak1)
#
# b1 = Bandit("黑猫", 100, "雇佣兵")
# p1.fire(b1)

# class inst():  # 这部分是演示组合演示
#     def knief(self):
#         raise Exception("没有该函数 有问题")
#
#
# class Person(inst):
#     def __init__(self, name, hp, job, ak1):
#         self.name = name
#         self.hp = hp
#         self.ak1 = ak1
#         self.job = job
#
#     # def knief(self, obj):
#     #     print(f"{self.name}划了{obj.name}一刀{obj.name}掉了10滴血")
#
#     def fire(self, obj):
#         self.ak1.fire(self, obj)
#
#
# class Police(Person):
#     pass
#
#
# class Bandit(Person):
#     pass
#
#
# class AK():
#     def __init__(self):
#         self.ak = 90
#
#     def fire(self, obj, obj1):
#         print(f"{obj.name}打{obj1.name}打掉了{obj1.name}90滴血")
#
#
# # 实例化一个枪对象
# ak1 = AK()
# # 首先实例化一个警察对象
# p1 = Police("火凤凰", 100, "特种兵", ak1)
#
# b1 = Bandit("黑猫", 100, "雇佣兵", ak1)
# p1.fire(b1)
# b1.fire(p1)


# 双下方法 魔法方法

# def __init()__  实例化时 触发

# class A():
#
#     def __init__(self, name):
#         self.name = name
#
#     def __len__(self):
#         return len(self.name)
#
#
# a = A("Alex")
# print(len(a))

# class A(object):
#
#     def __hash__(self):
#         return 10101011
#
#
# a = A()
# print(hash(a))

# class A(object):
#
#     def __str__(self):
#         return "格式化的时候执行我"
#
#
# a = A()
# print("%s" % a)

# class A(object):
#
#     # def __str__(self):  # 级别更高
#     #     return "格式化的时候执行我"
#
#     def __repr__(self):
#         return "执行的我"
#
#
# a = A()
# print(a)

#
# class A():  # 对象加()
#
#     def func(self):
#         print("啦啦啦")
#
#     def __call__(self, *args, **kwargs):
#         print("执行到我")
#         self.func()
#
#
# a = A()
# a()

#
# class A():
#     def __init__(self, a):
#         self.a = a
#
#     def __add__(self, other):  # 进行+的时候操作
#         return self.a + other.a
#
#
# a = A(10)
# b = A(20)
# print(a + b)

# class A():
#
#     def __init__(self, name):
#         self.name = name
#
#     def __del__(self):
#         print("删除时执行我")
#
#
# a = A("alex")
# del a.name


# 单列模式
# class A():
#     __instance = None
#
#     def __init__(self, name):
#         print("我是init")
#         self.name = name
#
#     def __new__(cls, *args, **kwargs):  # 开辟空间
#         print("我是new")
#         if not cls.__instance:
#             cls.__instance = super().__new__(cls)  # 让父类开空间
#             print(cls.__instance)
#         return cls.__instance
#
#     def show(self):
#         print(self.name)
#
#
# a = A("alex")
# a1 = A("asdasd")
# print(a.name)

# class A():  #item 系列
#
#     def __init__(self, name):
#         self.name = name
#
#     def __getitem__(self, item):   # a["name"]
#         return self.__dict__[item]
#
#     def __setitem__(self, key, value):  # a["name"] = "alex"
#         self.__dict__[key] = value
#
#
#     def __delitem__(self, key):  # del a["name"]
#         self.__dict__.pop(key)
#
#
# a = A("alex")
# print(a["name"])
# a["name"] = "hel"
# print(a.name)

# class A():
#
#     def __init__(self, name):
#         self.name = name
#
#     def __getitem__(self, item):
#         print("这是查看对象空间的变量")
#         return self.__dict__.get(item)  # self.__dict__[item]
#
#     def __setitem__(self, key, value):
#         """
#         :param key:
#         :param value:
#         :return:
#         """
#         print("这是给对象空间进行变量的设置")
#         self.__dict__[key] = value
#
#     def __delitem__(self, key):
#         print("这是删除对象空间中的变量")
#         self.__dict__.pop(key)
#
#
# a = A("alex")
# # 用法与字典一模一样
# # a[""] -- 对象名[键名]
#
# print(a["name"])
#
# a["age"] = 10  # 对象名["键"] = "值"
# print(a.age)
# print(a["age"])
#
# del a["age"]


# 上下文管理

# class A():
#
#     def __init__(self, filename, mode="r", encoding="utf-8"):
#         self.filename = filename
#         self.mode = mode
#         self.encoding = encoding
#
#     def read(self):
#         return self.f.readline()
#
#     def __enter__(self):
#         self.f = open(self.filename, self.mode, encoding=self.encoding)
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.f.close()
#
#
# with A("userinfo") as f:
#     print(f.read())

# class A():
#
#     def __init__(self, name):
#         self.name = name
#
#     def __enter__(self):
#         self.name = "alex"
#         return self
#
#     def func(self):
#         print("is func")
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         del self.name
#
# with A("meet") as f:
#     f.func()
#     print(f.name)


# class A():
#     def __init__(self):
#         pass
#
#     def fun(self):
#         pass
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         del self
#
# with A() as f:
#     pass
#
# # 让func()函数执行

#