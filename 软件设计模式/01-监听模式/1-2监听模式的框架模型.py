from abc import ABCMeta, abstractmethod


# 引入 ABCMeta 和 abstractmethod 来定义抽象类和抽象方法

class Observer(metaclass=ABCMeta):
    """观察者类的基本类"""

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
