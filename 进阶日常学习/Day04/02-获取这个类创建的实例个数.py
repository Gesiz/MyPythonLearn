# 类在实例化的时候，会触发__init__这个方法，
# 在init里面进行计数器加一
# 计数器设置在类属性上

# 类中的__del__方法，在类的实例被销毁的时候回触发，计数器减一

class Person:     # __dict__ = {类属性名：类属性值的引用，类中的方法：方法的引用}
    __count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # init被执行，代表一个实例对象已经创建，在这儿计数器加一
        Person.__count += 1

    def __del__(self):
        Person.__count -= 1

    @classmethod
    def get_count(cls):
        return cls.__count


p1 = Person('hello', 11)    #  __dict__ = {实例属性名：实例属性值的引用}
p2 = Person('fine', 12)
p3 = Person('apple', 13)

print(Person.get_count())


del p1
del p2
del p3
print(Person.get_count())
