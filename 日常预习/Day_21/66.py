# encoding=utf-8

from scapy.all import *
import utils
import os

from scapy.layers.inet import IP,UDP

os.system("python sniff_script.py >> sniff.log")


def forge(address, port):
    """ 通过嗅探到的数据，进行伪造数据 """
    forge_data = "This is forge data."
    pkt = IP(src='172.16.2.200', dst=address) / UDP(sport=12345, dport=port) / forge_data
    send(pkt, inter=1, count=3)
    pass


sniff_file = open("sniff.log", "rb")
for data in sniff_file.readlines():
    result = utils.match(data)
    if result is not None and result[0] != '172.16.2.135':
        print(result)
        forge(result[0], int(result[1]))
        pass
    pass