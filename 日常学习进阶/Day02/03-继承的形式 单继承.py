# 继承的形式
# 单继承
# 多继承

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
    def call(self):
        print(f"{self.name}在旺旺叫")

class TianDog(Dog):
    pass

# 猫类

class Cat(Animal):
    def call(self):
        print(f"{self.name}在喵喵叫")


dog = Dog("大黄", 4)
dog.eat()
dog.run()
dog.call()

cat = Cat("大喵", 3)
cat.eat()
cat.run()
cat.call()