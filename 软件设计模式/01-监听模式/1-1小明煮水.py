# 监听模式
# 在对象间定义一种一对多的依赖关系 当这个对象状态发生改变时 多有依赖他的对象都会被通知并自动更新
from abc import ABCMeta, abstractmethod

# 观者模式是对象的行为模式 又叫 发布/订阅(Publish/Subscribe)模式
# 模型/视图(Model/View)模式 源/监视器模式(Source/Listener)模式
# 或者从属者模式(Dependents)模式
# 监听模式的核心思想就是在被观察者与观察者之间建立一种自动触发的关系

# 引入ABCMeta 和 abstractmethod 来定义抽象类和抽象方法

class WaterHeater():
    """热水器 战胜寒冬的有利武器"""

    def __init__(self):
        self.__observers = []  # 观察者
        self.__temperature = 25  # 25

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self, temperature):
        self.__temperature = temperature
        print(f"当前温度是:{str(self.__temperature)}℃")
        self.notifies()

    def addObserver(self, observer):
        self.__observers.append(observer)

    def notifies(self):
        for o in self.__observers:
            o.update(self)


class Observer(metaclass=ABCMeta):
    """洗澡模式和引用模式的父亲"""

    @abstractmethod
    def update(self, waterHeater):
        pass


class WashingMode(Observer):
    """该模式用于洗澡"""

    def update(self, waterHeater):
        if 50 <= waterHeater.getTemperature() < 70:
            print("水已烧好！温度正好！可以用来洗澡了")

class DrinkingMode(Observer):
    """该模式用于引用"""

    def update(self,waterHeater):
        if waterHeater.getTemperature() >= 100:
            print("水已烧开！可以饮用了")


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