#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project:MyPythonLearn
# Product:PyCharm
# User:Gei
# Author: Gesiz
# Createtime: 2020/10/30 17:48

from scapy.layers.inet import IP, UDP
from scapy.sendrecv import send

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

# def udp_read(sock):
#     while True:
#         data = sock.recvfrom(1024)
#         print(data[0].decode("gb2312"))
#
#
# def udp_write(sock, addr):
#     while True:
#         da = input("请输入")
#         sock.sendto(da.encode("gb2312"), addr)
#
#
# if __name__ == "__main__":
#     # addr = ("127.0.0.1", 2425)
#     lock = threading.Lock()
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
#     # s.bind(("", 8888))
#     send_content = "1:1213:赵子旭:PC-MAC:32: 我最帅"
#     network = '<broadcast>'
#     dest = ('192.168.144.255', 2425)
#     s.sendto(send_content.encode("gb2312"), dest)
#     # t2 = threading.Thread(target=udp_write, args=(s, addr))
#     # t1 = threading.Thread(target=udp_read, args=(s,))
#     # t2.start()
#     # # t1.start()
#     # t2.join()
#     # t1.join()
#
import random
# import time
# while True:
#     time.sleep(random.randint(1, 5))
send(IP(src=f'192.168.144.30', dst='192.168.144.255') / UDP(sport=4444, dport=2425) /
     "1:1213:我可太帅了:PC-MAC:288: 麋鹿".encode('gb2312'))

print("1:1213:麋鹿:PC-MAC:32: 今天也是我最帅".encode('gb2312'))
