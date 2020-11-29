# 多态的实现
"""
1 子类继承父类
2 子类重写父类方法
3 调用子类方法
"""


# 定义动物类
class Animal:

    def call(self):
        print("叫")
        raise Exception("有问题")




# 定义狗类
class Dog(Animal):
    def call(self):
        print(f"旺旺")

# 定义猫类
class Cat(Animal):
    def call(self):
        print(f"喵喵")

class Pig(Animal):
    def call2(self):
        print("213")

# 之前的调用方法
# dog = Dog()
# dog.call()

# 多态会定义一个同意的接口进行调用
def do_call(obj):
    print("添加功能1")
    obj.call()
    print("添加功能2")


# TODO 多态的调用方式
# 第一种方式
dog = Dog()
do_call(dog)
cat = Cat()
do_call(cat)
# 第二种方式 优化后
do_call(Dog())
do_call(Cat())
# do_call(Pig())
p = Pig()