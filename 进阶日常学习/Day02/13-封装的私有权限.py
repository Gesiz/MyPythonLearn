class A:
    def __init__(self):
        self.name = "hello"
        self.__age = 18  # 私有属性

    def __run(self):   # 私有方法
        print(f'{self.name} was run away')

    def get_age(self):
        print(self.__age)


class B(A):
    def get_age(self):
        print(self.__age)


# 查看权限使用范围
"""
1 类的内部
2 类的外部
3 子类的内部
"""
a = A()
print(a._A__age)
print(a.__dict__)
# a.get_age()
# b = B()     # 报错
# b.get_age()

# 结论 不可被继承
