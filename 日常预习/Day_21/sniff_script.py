# encoding=utf-8

from scapy.all import *

receive = sniff(filter="udp and host 172.16.2.135", count=100)
receive.show()