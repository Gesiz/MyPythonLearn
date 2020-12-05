class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def info(self):
        print(self.name, self.__age)

    def set_age(self, age):
        if 1 <= age <= 150:
            self.__age = age
        else:
            print('年龄不合法')


p1 = Person('fine', 18)
# print(p1.name, p1.age)

p1.name = 'hello'
# p1.age = 100
p1.set_age(1000)
# print(p1.name, p1.age)
p1.info()
