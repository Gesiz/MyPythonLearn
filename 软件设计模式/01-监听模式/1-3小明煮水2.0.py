from abc import ABCMeta, abstractmethod


# 引入 ABCMeta 和 abstractmethod 来定义抽象类和抽象方法

class Observer(metaclass=ABCMeta):
    """观察者类的基本类"""

    @abstractmethod
    def update(self, observable, object):
        pass


class Observable:  # 被观察的
    def __init__(self):
        self.__observers = []

    def addObserver(self, observer):
        self.__observers.append(observer)

    def removeObserver(self, observer):
        self.__observers.remove(observer)

    def notifyObserver(self, object=0):
        for o in self.__observers:
            o.update(self, object)


class WaterHeater(Observable):
    """热水器 战胜寒冬的有力武器"""

    def __init__(self):
        super().__init__()
        self.__temperature = 25

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self, temperature):
        self.__temperature = temperature
        print(f"当前温度是{self.__temperature}℃")
        self.notifyObserver()


class WashingMode(Observer):
    """该模式用于洗澡"""

    def update(self, observable, object):
        if isinstance(observable, WaterHeater) \
                and 50 <= observable.getTemperature() < 70:  # isinstance 可以判断是否为子类 也可以判断 数据类型
            print("水已经烧好 可以洗澡了")


class DrinkingMode(Observer):
    """该模式用于饮用"""

    def update(self, observable, object):
        if isinstance(observable, WaterHeater) \
                and 50 <= observable.getTemperature() < 70:
            print("水已经烧好了 可以洗澡了")


def testWaterHeater():
    heater = WaterHeater()
    washingObser = WashingMode()
    drinkingObser = DrinkingMode()
    heater.addObserver(washingObser)
    heater.addObserver(drinkingObser)
    heater.setTemperature(40)
    heater.setTemperature(60)
    heater.setTemperature(100)


if __name__ == '__main__':
    testWaterHeater()