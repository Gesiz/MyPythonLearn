#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project:MyPythonLearn
# Product:PyCharm
# User:Gei
# Author: Gesiz
# Createtime: 2020/10/28 15:08

# 线程 是操作系统能够进行调度的最小单位
# 他包括在进程当中
# 是进程中的实际运行单位
# 进程是线程的容器

# import threading
#
#
# # t1 = threading.Thread()
# # print(threading.current_thread().name)
#
# def func():
#     print("123")
#     print(threading.current_thread().name)
#     print(f"当前总共有{len(threading.enumerate())}个线程在执行")
#
#
# print(threading.enumerate())
# t = threading.Thread(target=func)
# print(threading.current_thread().name)
# t.start()
# t.join()

# 守护进程
# 新状态 可运行状态 运行状态等待 阻塞 睡眠状态 死亡太
# 线程共享全局变量
# import threading
# import time
# num = 0
# print(f"主线程中num={num}")
# def func1():
#     global num
#     lock1.acquire()
#     for i in range(1000000):
#         num += 1
#     lock1.release()
#     print(f"子线程中1中num={num}")
#
# def func2():
#     global num
#     lock1.acquire()
#     for i in range(1000000):
#         num += 1
#     lock1.release()
#     print(f"子线程中2中num={num}")
# lock1 = threading.Lock()
#
# t1 = threading.Thread(target=func1)
# t2 = threading.Thread(target=func2)
# t1.start()
# # t1.join()
# t2.start()
# t1.join()  #
# t2.join()
# print(f"主线程中num={num}")
# 不理想状态中 可能会产生问题 所以需要线程同步(互斥锁)
# 直接进行join不科学 没有调度机制
# 互斥锁保证了每次只有一个线程进行操作 从此引入了一个状态 锁定非锁定

# 写一个程序实现三个进程间进行通信 传递一个字符串
# from multiprocessing import Process, Queue
#
# def func1(qu):
#     print("这是函数一要对函数二进行传递字符串")
#     qu.put("字符串一")
#
#
# def func2(qu, qu2):
#     a = qu.get()
#     print(f"这是函数二: {a}")
#     qu2.put(a)
#
#
# def func3(qu):
#     print(f"这是函数三: {qu.get()}")
#
#
# if __name__ == "__main__":
#     que = Queue(0)
#     que2 = Queue(0)
#     p1 = Process(target=func1, args=(que,))
#     p2 = Process(target=func2, args=(que, que2))
#     p3 = Process(target=func3, args=(que2,))
#     p1.start()
#     p2.start()
#     p3.start()
#     p1.join()
#     p2.join()
#     p3.join()

# 写一个包含10个线程的程序 每一个子线程执行的时候都需要打印当前线程名 当前活跃线程数量


# 3
# 4

import threading

money = 500


def func1():
    global money
    for i in range(100):
        money += 1


lis = []
for i in range(10):
    t = threading.Thread(target=func1)
    lis.append(t)
    t.start()
for i in lis:
    i.join()

print(money)