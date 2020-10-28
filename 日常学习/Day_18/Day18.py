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

from multiprocessing import Process
import time



def func(name, age):
    print(f"这是第一个子进程的传递参数{name}")
    time.sleep(1)
    print("子进程一结束了")


def func2(name):
    print(f"这是第二个子进程{name}")
    time.sleep(2)
    print("子进程二结束了")


if __name__ == "__main__":
    print("父进程启动")
    p = Process(target=func, name="进程1", args=("alex", 83))  # 位置参数元组
    p1 = Process(target=func2, name="进程2", args=("kw",))  #
    # 进入就绪状态 等待系统调度机制进行调用
    p.start()
    print(p.pid)
    p1.start()
    print(p1.pid)
    p.join()
    p1.join()
    time.sleep(3)
    print("主进程结束")
