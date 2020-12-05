# 查看一个类继承了哪些父类
class Animal:
    pass

class God:
    pass

class Dog(Animal, God):
    pass


print(Dog.__bases__)
print(Animal.__bases__)