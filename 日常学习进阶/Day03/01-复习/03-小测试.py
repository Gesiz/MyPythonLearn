# TODO 类方法的定义
# 1 classmethod 装饰这个方法
# 2 在类中定义一个函数 必须设置第一个函数 参数名叫 cls

class Person:
    country = '中国'
    birthday = 1949

    # 定义类方法
    @classmethod
    def get_birthday(cls):
        return cls.birthday

    # 定义对象方法
    # 修改这个birthday属性加以
    def add_birthday(self):
        self.birthday += 1
        # 只能增加对象属性

# 调用
p1 = Person()
p1.add_birthday()
print(p1.get_birthday())
print(Person.get_birthday())