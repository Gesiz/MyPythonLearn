#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project:MyPythonLearn
# Product:PyCharm
# User:Gei
# Author: Gesiz
# Createtime: 2020/10/16 22:09

# 函数可以节省代码 提高实用性
# 函数 vs 面向对象

# 类 对一类相似的的事物的统称
# 对象 对某事物的具体描述

# 有点
# 能够给相似功能进行分类管理
# 上帝的视角 万物皆可造

# class :
# 累的结构

# def 函数名 遵循变量命名规则 下划线

# def func():
# 函数体
# class 类名 遵循变量命名规则 驼峰

# class UserInfo():
#     # 类变量 -- 变量 --静态字段 -- 静态属性  自动执行
#     # 类方法 -- 函数 --动态字段 -- 动态属性
#     name = "alex"
#
#     def func(self):
#         print(111)

# class Person():
#     name = "子惠"  # 子惠的特征
#     age = 18
#     sex = "男"
#     print(sex)
#     def worf(self):  # 形参
#         print("都能工作")
#
#     def eat(self):
#         print("都能吃")
#
#     def sleep(self):
#         print("都能睡")
#
#     def speak(self):
#         print("都能说话")
#
# p = Person()  # 实例化对象
# # p.name = "asdasd"
# # print(Person.name)
# # Person.name = "jhhh"
# # del Person.name
#
# # 可以通过类名操作类 但是不建议使用类名操作类 (除非有特殊的类方法 才能用类名操作类)
#
# # 查找顺序 先从对象空间中进行查找 如果对象空间中没有再去 类空间中查找
#
# # 写类的技巧是 将多个对象共同的特点和方法进行提升就是类
#
# # 不推荐类名操作 对象操作类方法时 会将对象本身当做参数隐形传参
# Person.worf(1)
# p.worf()  # 对象

# class Person():
#
#     name = "子惠"
#
#     def work(self):
#         print(id(self))
#         print("all work")
#
# p = Person()
# print(id(p))
# p.work()
# p1 = Person()
# p1.work()
#

# self 就是对象背身
# class Person():
#
#     def __init__(self, **kwargs):  # 魔法方法
#         # 初始化函数
#         # 给对象空间封装属性的函数
#         self.name = kwargs["name"]
#         self.sex = kwargs["sex"]
#         # print(name)
#         # print(11)
#         # print(id(self))
#
#
# p = Person(name="alex", sex="男")  # 类名加()触发__init__函数
# # print(id(p))
# #
# # p.name = "alex"
#
# print(p.name, p.sex)
#
#
#
# class Person():
#     # 公有
#     nationality = "中国"  # 公有类变量
#     __nationality = 10  # 私有类变量
#     def __init__(self, name, sex, age, money):
#         print(Person.__nationality)  # 只能在类中通过 类名访问 私有类变量
#         self.name = name
#         self.sex = sex
#         self.age = age
#         self.money = money  # 私有
#
#     def func(self):
#         print("我是公有方法")
#         self.__foo()  # 私有方法一般在公有方法内调用
#
#     def __foo(self):
#         print("我是私有方法")
#
#
# p1 = Person("alex", "不详", 99, 10)
# p2 = Person("meet", "不详", 8, 100)
# print(p1.name)
# print(p2.name)
# print(p1.nationality)
# print(p2.nationality)
#
#
# p1.func()
#
#
#
# class LOL():
#     def __init__(self, name, ak, hp, obj=None):
#         self.name = name
#         self.ak = ak
#         self.hp = hp
#
#     def q(self, obj):
#         obj.hp = obj.hp - self.ak * 0.2
#         print(f"{self.name}使用了Q技能攻击{obj.name},{obj.name}掉了{self.ak * 0.2}血 {obj.name} 剩余血量 {obj.hp}")
#
#
#     def w(self, obj):
#         print("w技能")
#
#     def e(self, obj):
#         print("e技能")
#
#     def r(self, obj):
#         print("r技能")
#
#
# ccl = LOL("盖伦", 100, 1000)
# ys = LOL("亚索", 200, 500)
# ccl.q(ys)
#
# msg = """
# 1.盖伦
# 2.亚索
# """
# # 依赖关系 将一个对象当作参数传递到类中使用就是依赖关系


# 实例方法
# class A():
#     pass
#
#     @classmethod  # 类方法
#     def func(cls):
#         print(11)
#
#     @staticmethod  # 静态方法
#     def foo():
#         print(222)
#
#
#
# a = A()
# a.func()  # 对象方法
#
# # 类方法
# A.func()
#
# # self cls *args **kwargs 都是可以随意修改的
# # 静态方法
#
# A.foo()
# a = A()
# a.foo()


class Bmi():
    name = "a"  # 属性

    def __init__(self, name, height, weight):
        self.height = height
        self.weight = weight
        self.name = name

    # 目的是吧bmi这个方法伪装成一个属性

    @property  #把方法伪装成一个属性
    def bmi(self):
        return self.weight / (self.weight ** 2)

    @bmi.setter
    def bmi(self, value):
        self.weight = value
        print(f"修改时执行我{value}")

    @bmi.deleter
    def bmi(self):
        print("删除时执行我")

p = Bmi("徐乐", 1.78, 89)

print(p.bmi)
p.bmi = 20
print(p.bmi)
del p.bmi