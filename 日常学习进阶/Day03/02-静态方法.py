# TODO 定义静态方法
# 1. @staticmethod 装饰函数的静态方法
# 2. 下面在类中定义一个函数 参数没有特别要求

class Person:

    @staticmethod
    def info():
        print('info')


# TODO 调用静态方法
# 1. 通过类名调用
Person.info()
# 2. 通过对象调用
p1 = Person()
p1.info()


# TODO 查看静态方法是否保存在类中
print(Person.__dict__)