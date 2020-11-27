# 子类重写父类的属性和方法

# 动物类
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name}在吃")

    def run(self):
        print(f"{self.name}在跑")

    def call(self):
        print(f"{self.name}在叫")


# 狗类
class Dog(Animal):

    def __init__(self, name, age, color):
        Animal.__init__(self, name, age)
        self.color = color

    def call(self):
        Animal.call(self)
        print(f"{self.name}在旺旺叫")


dog = Dog("大黄", 3, "黄色")
dog.call()

print()