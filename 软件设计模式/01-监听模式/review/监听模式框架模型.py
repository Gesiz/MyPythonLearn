from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    """观察者的基本类"""

    @abstractmethod
    def update(self):  # 观察者需 !观察! 被观察 !对象!  在被观察者中 被被动改变状态的时候 主动调用观察者 进行状态刷新
        pass


class Observable:
    """被观察的类"""

    def __init__(self):
        self.__observers = []  # 将观察者对象添加到 被观察者的 属性中 每次 被观察的对象状态改变时 遍历该对象

    def addObserver(self, observer):  # 构造封装属性的访问方法 当出现新的观察者时 通过该构造方法 封装到这里
        self.__observers.append(observer)

    def removeObserver(self, observer):  # 删除封装属性的访问方法 当观察者退出时 删除自身
        self.__observers.remove(observer)

    def notifyObservers(self, object=0):    # 当状态发生变化 便调用该方法
        for o in self.__observers:
            o.update(self, object)
