#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project:MyPythonLearn
# Product:PyCharm
# User:Gei
# Author: Gesiz
# Createtime: 2020/10/26 18:14


# from multiprocessing import Process
#
#
# def run(name):
#     print("子程序运行中 name=%s" % name)
#     print(f"子程序运行中 {name}")
#
#
# if __name__ == "__main__":
#     print("父进程启动")
#     p = Process(target=run, args=('test',))
#     # target 表示调用对象 , args表示调用对象的未知参数元组
#     # (注意 元组中只有一个元素时结尾要加)
#     print("子进程将要执行")
#     p.start()
#     print(p.name)
#     p.join()
#     print("子进程解除")

# from multiprocessing import Process
# import time
#
#
#
# def func(name, age):
#     print(f"这是第一个子进程的传递参数{name}")
#     time.sleep(1)
#     print("子进程一结束了")
#
#
# def func2(name):
#     print(f"这是第二个子进程{name}")
#     time.sleep(2)
#     print("子进程二结束了")
#
#
# if __name__ == "__main__":
#     print("父进程启动")
#     p = Process(target=func, name="进程1", args=("alex", 83))  # 位置参数元组
#     p1 = Process(target=func2, name="进程2", args=("kw",))  #
#     # 进入就绪状态 等待系统调度机制进行调用
#     p.start()
#     print(p.pid)
#     p1.start()
#     print(p1.pid)
#     p.join()
#     p1.join()
#     time.sleep(3)
#     print("主进程结束")


# 进程池
# from multiprocessing import Process
#
# num = 10
#
#
# def func1():
#     global num
#     num += 10
#     print(f"我在进程一中num的值为{num}")
#
#
# def func2():
#     global num
#     num += 30
#     print(f"我在进程二中num的值为{num}")
#
#
# if __name__ == "__main__":
#     p1 = Process(target=func1)
#     p2 = Process(target=func2)
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     num += 100
#     print(f"主进程中num的值为{num}")

# from multiprocessing import Process
#
#
# class MyPro(Process):
#
#     def run(self):
#         print("这是一个进程")
#
#
# if __name__ == "__main__":
#     p = MyPro()
#     p.start()
#     p.join()

# from multiprocessing import Process, Pool
# import time
#
# def func():
#     print(1123)
#     time.sleep(3)
#
#
# if __name__ == "__main__":
#     po = Pool(12)
#     for i in range(20):
#         po.apply_async(func)
#     po.close()
#     po.join()

# import random
#
# for i in range(20):
#     print(int(random.random()*4)+5)
# 进程间进行通信
from multiprocessing import Process, Queue, Pool, Manager
import time


def func1(q):
    for i in range(10):
        q.put("123")
        time.sleep(1)
        print("放入一条数据")


def func2(q):
    for i in range(10):
        time.sleep(2)
        print(q.get())


# Queue.qsize() Queue.empty() Queue.full() Queue.get([block[,timeout]])
#
if __name__ == "__main__":
    # qqq = Queue(3)
    qqq = Manager().Queue(3)
    # p = Process(target=func1, args=(qqq,))
    # p1 = Process(target=func2, args=(qqq,))
    # p.start()
    # p1.start()
    # p.join()
    # p1.join()
    po = Pool(3)
    po.apply_async(func1, (qqq,))
    po.apply_async(func2, (qqq,))
    po.close()
    po.join()
# 进程池创建的进程若要进行通信
