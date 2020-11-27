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
class Dog(Animal):  # object

    def __init__(self, name, age, color):
        # 第一种super 书写方式
        # super(Dog, self).__init__(name, age)
        # 第二种
        super().__init__(name, age)
        # Dog 当前类
        # self 当前类的实例
        self.color = color

    def call(self):
        super().call()
        print(f"{self.name}在旺旺叫")


dog = Dog("大黄", 3, "黄色")
dog.call()
