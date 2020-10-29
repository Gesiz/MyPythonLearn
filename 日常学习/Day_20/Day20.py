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

