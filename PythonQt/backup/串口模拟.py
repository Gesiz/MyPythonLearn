#!/usr/bin/python
# -*-coding: utf-8 -*-

import serial
import serial.tools.list_ports
import threading
import time
from datetime import datetime

#列出所有当前的com口
port_list = list(serial.tools.list_ports.comports())
port_list_name = []

class SerialPort:
    def __init__(self,port,buand):
        self.port = serial.Serial(port,buand)
        self.port.close()
        if not self.port.isOpen():
            self.port.open()

    def port_open(self):
        if not self.port.isOpen():
            self.port.open()

    def port_close(self):
        self.port.close()

    def send_data(self):
        #date = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        while True:
            date = datetime.now().strftime('%H:%M:%S.%f')[:-3]
            print("send:",date)
            self.port.write(date.encode())
            time.sleep(1)

    def read_data(self):
        while True:
            count = self.port.inWaiting()
            if count > 0:
                rec_str = self.port.read(count)
                print("receive:",rec_str.decode())

def show_all_com():
    if len(port_list) <= 0:
        print("the serial port can't find!")
    else:
        for itms in port_list:
            port_list_name.append(itms.device)

if __name__ == '__main__':

    baunRate = 115200

    print("1.list all com")
    show_all_com()
    print(port_list_name)

    print("2.open write port ",port_list_name[0])
    serialPort_w = port_list_name[0]
    mSerial_w = SerialPort(serialPort_w,baunRate)

    print("3.start write thread")
    t1 = threading.Thread(target=mSerial_w.send_data)
    t1.setDaemon(True)
    t1.start()

    print("4.open read port ",port_list_name[1])
    serialPort_r = port_list_name[1]
    mSerial_r = SerialPort(serialPort_r,baunRate)

    print("5.start read thread")
    t2 = threading.Thread(target=mSerial_r.read_data)
    t2.setDaemon(True)
    t2.start()

    #do something else, make main thread alive there
    while True:
        time.sleep(10)