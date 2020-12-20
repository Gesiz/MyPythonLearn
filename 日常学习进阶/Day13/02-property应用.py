class Person:
    def __init__(self, age):
        self.__age = age

    # def set_age(self, new_age):
    #     if new_age > 200 or new_age < 0:
    #         print("你成精了?")
    #     else:
    #         self.age = new_age
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age > 200:
            print("错了")
        else:
            self.__age = new_age


p = Person(100)
print(p.age)

p.age = 9999
print(p.age)
