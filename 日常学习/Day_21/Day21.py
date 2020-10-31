#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project:MyPythonLearn
# Product:PyCharm
# User:Gei
# Author: Gesiz
# Createtime: 2020/10/30 17:48

# from socket import *
#
# s = socket(AF_INET, SOCK_DGRAM)
# addr = ("192.168.79.2", 8888)
# while True:
#     da = input("请输入")
#     s.sendto(da.encode("gb2312"), addr)
#     data = s.recvfrom(1024)
#     print(data[0].decode("gb2312"))


import threading
import socket


def udp_read(sock):
    while True:
        data = sock.recvfrom(1024)
        print(data[0].decode("gb2312"))


def udp_write(sock, addr):
    while True:
        da = input("请输入")
        sock.sendto(da.encode("gb2312"), addr)


if __name__ == "__main__":
    addr = ("192.168.79.2", 8888)
    lock = threading.Lock()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # s.bind(("", 8881))
    s.sendto("准备开始".encode("gb2312"), addr)
    t2 = threading.Thread(target=udp_write, args=(s, addr))
    t1 = threading.Thread(target=udp_read, args=(s,))
    t2.start()
    t1.start()
    t2.join()
    t1.join()
