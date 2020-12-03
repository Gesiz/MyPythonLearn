#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project:MyPythonLearn
# Product:PyCharm
# User:Gei
# Author: Gesiz
# Createtime: 2020/10/29 11:55

# 信号量semaphore 类似于 互斥锁 线程池

# import threading, time
#
# s1 = threading.Semaphore(200)  # 控制每次线程的上限
#
#
# def func():
#     s1.acquire()
#     print(time.ctime())
#     time.sleep(1)
#     print("给Alex搓背")
#     s1.release()
#
#
# for i in range(100):
#     t1 = threading.Thread(target=func)
#     t1.start()


# from multiprocessing import Process  # 复习
# import threading
#
# import time
#
#
# def func():
#     t = threading.Thread(target=func1)
#     t.start()
#     t.join()
#
#
# def func2():
#     print("345")
#
#
# def func1():
#     t1 = threading.Thread(target=func2)
#     t1.start()
#     t1.join()
#
#
# if __name__ == "__main__":
#     p = Process(target=func)
#     p.start()
#     p.join()

# 新状态 可运行状态 运行状态 等待 阻塞 睡眠状态 死亡态

# 强耦合
# 高内聚 低耦合

# def func():
#     print("func1")
#
#
# def func2():
#     print("func2")
#
#
# dit = {
#     "1": func,
#     "2": func2
# }
# msg ="""
# 1 fu
# 2 fu2
# """
# while True:
#     choose = input(msg)
#     if choose in msg:
#         dit[choose]()
#
# 进程之间如果直接做通信会垂涎按两个问题
# 1 耦合性太强
# 2 速率可能不太匹配
# 解决方式 找一个缓冲区来中转数据


# 同步和异步

# 异步
# import threading, time
#
# num = 10
#
#
# def func():
#     global num
#     while True:
#         if lock.acquire(False):
#             time.sleep(3)
#             for i in range(1000000):
#                 num += 1
#             lock.release()
#             break
#         else:
#             print("这里可以做一些IO操作")
#
#     print(num)
#
#
# def func1():
#     global num
#     while True:
#         if lock.acquire(False):
#             time.sleep(3)
#             for i in range(1000000):
#                 num += 1
#             lock.release()
#             break
#         else:
#             print("这里可以做一些IO操作")
#     print(num)
#
#
# lock = threading.Lock()
#
# t = threading.Thread(target=func)
# t1 = threading.Thread(target=func1)
#
# t.start()
# t1.start()

import multiprocessing


#
#
def func1():
    for i in range(10):
        print(123)
    return "运行结束"


def func2(tool):
    print(tool)


if __name__ == "__main__":
    po = multiprocessing.Pool()
    po.apply_async(func=func1, callback=func2)
    po.close()
    po.join()

# 协程 比线程更小的执行单元
# 一个线程作为一个容器里面可以放置多个协程

# import greenlet
# import time
#
#
# def func1():
#     for i in range(10):
#         print("123")
#         g2.switch()
#     time.sleep(1)
#
#
# def func2():
#     for i in range(10):
#         print("234")
#         g1.switch()
#     time.sleep(1)
#
#
# g1 = greenlet.greenlet(func1)
# g2 = greenlet.greenlet(func2)
# g1.switch()

# import gevent
#
#
# def func1():
#     while True:
#         print("111")
#         gevent.sleep(2)
#
#
# def func2():
#     while True:
#         print("222")
#         gevent.sleep(2)
#
#
# a1 = gevent.spawn(func1)
# a2 = gevent.spawn(func2)
#
# a1.join()
# a2.join()
