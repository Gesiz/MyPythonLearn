# TODO 类方法的定义
# 1. @classmethod 装饰的这个方法
# 2. 在类中定义一个函数 必须设置第一个函数 参数名 默认为 cls

class Person:
    country = '中国'

    # 定义类方法
    @classmethod
    def get_country(cls):  # cls 是类对象本身
        return cls.country

    # 定义修改country 属性的方法
    @classmethod
    def set_country(cls, country):
        cls.country = "美国"

    # 测试对象方法修改属性
    def set_country(self):
        print("asdsad")


# 类中的方法保存在
# 类.__dict__ = {属性名:属性值}


# TODO 类方法的调用
# 1 类名进行调用
# 2 类实例的操作
p = Person()
print(Person.get_country())
Person.country = "asd"
print(p.get_country())
p.country = "dsa"
print(Person.get_country())
print(p.get_country())
print(Person.__dict__)
print(p.__dict__)  # 类属性不能被对象直接修改 也不能对对象方法修改
# 类方法的作用
# 用来操作类属性

# TODO 类方法获取类属性
print(Person.get_country())

# TODO 类的内部通过类方法修改属性


# TODO 对象不能修改属性验证


# TODO 测试类中相同方法的调用情况
