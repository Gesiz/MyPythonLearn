# 一个类继承多个父类(两个及两个以上)

# 犬类
class Dog:
    def eat(self):
        print("吃骨头")

    def run(self):
        print("跑")


# 神仙类
class God:
    def fly(self):
        print("会飞")

    def run(self):
        print("神跑")


# 哮天犬类
class FlyDog(Dog, God):
    pass


flg_dog = FlyDog()
flg_dog.eat()
flg_dog.fly()
flg_dog.run()

# 继承链 mro 查找规则
print(FlyDog.__mro__)
print(FlyDog.mro())