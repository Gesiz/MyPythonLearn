class Person:
    count_new = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__class__.count()


    @classmethod
    def count(cls):
        cls.count_new += 1

    @classmethod
    def re_count(cls):
        cls.count_new -= 1

    @classmethod
    def f_count(cls):
        return cls.count_new

    def __del__(self):
        self.__class__.re_count()

    @classmethod
    def show_info(cls):
        print(f"这是一个{cls.__name__}类 谢谢查看")

    def __str__(self):
        print(f"我的名字是{self.name}我的年龄是{self.age}")

    def study(self):
        print(f"我叫{self.name}我要好好学习")


a = Person("a", 11)
b = Person("b", 22)
print(f"当前实例化的数量为 {b.f_count()}")
del a
print(f"当前实例化的数量为 {b.f_count()}")
a = Person("a", 11)
print(f"当前实例化的数量为 {b.f_count()}")
Person.__