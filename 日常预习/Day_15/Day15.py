#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project:MyPythonLearn
# Product:PyCharm
# User:Gei
# Author: Gesiz
# Createtime: 2020/10/17 22:36

# 继承 子承父业
#
#
#
# class Person():
#
#     def __init__(self, name, age, sex, hobby):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.hobby = hobby
#
#     def eat(self):
#         print("能吃")
#
#     def sleep(self):
#         print("能睡")
#
#     def speak(self):
#         print("能说话")
#
#     def walk(self):
#         print("能走")
#
#
# class cat():
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def eat(self):
#         print("能吃")
#
#     def sleep(self):
#         print("能睡")
#
#     def speak(self):
#         print("能叫")
#
#     def walk(self):
#         print("能走")
#
# class dog():
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def eat(self):
#         print("能吃")
#
#     def sleep(self):
#         print("能睡")
#
#     def speak(self):
#         print("能叫")
#
#     def walk(self):
#         print("能走")

# 会大量重复代码
#
# class Zoo():  # 父类 基类 超类
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def eat(self):
#         print("能吃")
#
#     def sleep(self):
#         print("能睡")
#
#     def speak(self):
#         print("能叫")
#
#     def walk(self):
#         print("能走")
#
#
# class Person(Zoo):  # 子类 派生类
#
#     def __init__(self, name, age, sex, hobby):
#         Zoo.__init__(self, name, age, sex)  # 既执行子类中的初始化方法又执行父类的初始化方法  方式一
#         self.hobby = hobby
#
#     def speak(self):
#         print("能说话")
#
#
# class cat(Zoo):  # 子类
#     def __init__(self, name, age, sex, coat_color):
#         self.coat_color = coat_color
#         super().__init__(name, age, sex)  # super 是严格按照类的继承顺序进行执行
#
#     def jump(self):
#         print("跳楼")
#
#
# class dog(Zoo):  # 子类
#     pass
#
#
# p = Person("alex", 89, "不详", "lol")
# # 继承的优点就是减少重复代码
# #
# print(p.name)
#
# c1 = cat("布偶", 6, "公", "不详")
# print(c1.coat_color)

# class A():
#     name = "alex"
#     __age = 18
#
#     def func(self):
#         print("is func")
#
#     def __foo(self):
#         print("is foo")
#
#     @classmethod
#     def f1(cls):
#         print("is clas")
#
#     @staticmethod
#     def f2():
#         print("is f2")
#
#     def f3(self):
#         print("is f2")
#
#
# class B(A):
#     pass
#
#
# b = B()
# print(b.name)
# b.func()
# b.f1()


# 多继承
# python2
#   经典类 不继承object
#   新式类 继承object
# python3
#   新式类 继不继承object都是新式类

# 经典类的继承 深度优先 (一条路走到头) 类似于树
# 新式类 mro 广度优先仅供参考
# 类名.mro()


# 继承总结
# 继承
# 单继承
# 既要执行子类的初始化方法,又要执行父类的初始化放啊
# 推荐使用super().__init__()
# 父类中私有是不能进行继承的
# 多继承
# 经典类的继承方式 深度优先
# 新式类的继承方式 类名.mro
# 推荐使用super().__init__()
# 父类中私有是不能进行继承的

# 面向对象三大特征
# 1 封装 将属性封装在对象空间中
#   将功能封装到类中
# 2 继承
#   单继承 多继承 (经典 深度) (新式 mro)
# 3 多态
#   python 天生支持多态
#

# lst = [1, 2, 3, 4, 5, 6, 7, 8]
#
#
# def func(x):
#     return x > 4
#
#
# filter(lambda x: x > 4, lst)
# print(list(filter(func, lst)))
#
# print(list(filter(lambda x: x < 3, lst)))
#

# 类的约束
# 支付公司
# 1 微信
# 2 支付宝
# 3 QQ

from abc import ABCMeta, abstractmethod


class Pay(metaclass=ABCMeta):

    @abstractmethod  # 只要继承我的子类 先检查一遍 出错直接暂停
    def pay(self):
        pass
        # raise Exception("你没有定义pay函数")  # 主动报错


class WechatPay(Pay):

    def pay(self):
        """微信支付"""
        print("这是微信支付")

    def pay2(self):
        print(222)


class AliPay(Pay):

    def pay(self):
        print("这是支付宝支付")


class QQpay(Pay):

    def pay(self):
        print("这是QQ支付")


a = WechatPay()
b = AliPay()
c = QQpay()


def pay(obj):  # 统一接口
    obj.pay()


pay(a)
pay(b)
pay(c)


# super(当前类名，当前类的对象 )