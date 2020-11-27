class Person:
    address = "北京"

    def __init__(self):
        self.address = "上海"


# 类的外部设置属性
Person.country = "中国"
print(Person.country)  # 通过类名访问
p = Person()
# 类的内部空间
print(Person.__dict__)
p.country = "asd"
print(p.country)  # 通过对象名访问
print(Person.country)
# print(p.__dict__)
# print(p.__class__)
# print(Person.__base__)