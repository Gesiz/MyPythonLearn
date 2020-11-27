class Person:
    country = "中国"

    @classmethod
    def get_country(cls):
        print(cls.country)

    @classmethod
    def set_country(cls, country):
        cls.country = country


Person.set_country("美国")
Person.get_country()

# 第一种 类名调用

# 第二种 类的实例调用
p1 = Person()
p1.set_country("英国")
p1.get_country()
Person.set_country("美国")
Person.get_country()
print(Person.__dict__)