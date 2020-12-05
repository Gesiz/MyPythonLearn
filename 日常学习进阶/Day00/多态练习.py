class Animal:

    def __init__(self, name):
        self.__name = name

    def run(self):
        print(f"{self.__name}再跑")
        # raise Exception("请重写该方法")


class Cat(Animal):

    def eat(self):
        print(f"{self.__name}在吃")


class Dog(Animal):

    def eat(self):
        print(f"{self.__name}在吃")


def letRun(obj):
    obj.run()


c = Cat("波斯猫")
d = Dog("京巴狗")
a = Animal("动物")

letRun(c)
letRun(d)
letRun(a)