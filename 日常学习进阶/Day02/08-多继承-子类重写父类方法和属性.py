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

    def eat(self):
        print("吃空气")


# 哮天犬类
class FlyDog(Dog, God):
    def eat(self):
        print("吃的蟠桃")


fly_dog = FlyDog()
fly_dog.eat()