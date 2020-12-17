# coding=utf-8

import time
# 导入时间处理模块
from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, observable, object):
        pass


class Observable:  # 可观察的
    def __init__(self):
        self.__observers = []

    def addObserver(self, observer):
        self.__observers.append(observer)

    def removeObserver(self, observer):
        self.__observers.remove(observer)

    def notifyObserver(self, object=0):
        for o in self.__observers:
            o.update(self, object)


class Account(Observable):
    """用户账户"""

    def __init__(self):
        super().__init__()
        self.__latestIp = {}
        self.__latestRegion = {}

    def login(self, name, ip, time):
        region = self.__getRegion(ip)
        if self.__isLongDistance(name, region):
            self.notifyObserver({"name": name, "ip": ip, "region": region, "time": time})
        self.__latestRegion[name] = region
        self.__latestIp[name] = ip

    def __getRegion(self, ip):
        # 由IP地址获取的地区信息 这里只是模拟 真是项目中应该调用ip地址解析服务
        ipRegions = {
            "101.47.18.9": "浙江省杭州市",
            "67.218.147.69": "美国洛杉矶",
        }
        region = ipRegions.get(ip)
        return "" if region is None else region

    def __isLongDistance(self, name, region):
        # 计算本次登录与最近几次登录地区的差距
        # 这里只是简单地用字符串匹配来模拟 真是的项目中应该调用地理信息相关的服务
        latestRegion = self.__latestRegion.get(name)
        return latestRegion is not None and latestRegion != region


class Smssender(Observer):
    def update(self, observable, object):
        print(f'[短信发送] {object["name"]} 您好！ 检测到您的账户可能存在异常 最近一次的登录信息:\n'
              f'登录信息 {object["region"]}'
              f'登录IP  {object["ip"]}'
              f'登录时间 {time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(object["time"]))}')


class MailSender(Observer):
    """邮件发送器"""

    def update(self, observable, object):
        print(f'[邮件发送] {object["name"]} 您好！ 检测到您的账户可能存在异常 最近一次的登录信息:\n'
              f'登录信息 {object["region"]}'
              f'登录IP  {object["ip"]}'
              f'登录时间 {time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(object["time"]))}')


def testLogin():
    accout = Account()
    accout.addObserver(Smssender())
    accout.addObserver(MailSender())
    accout.login("Tony", "101.47.18.9", time.time())
    time.sleep(2)
    accout.login("Tony", "67.218.147.69", time.time())


if __name__ == '__main__':
    testLogin()
