class A:
    def __init__(self):
        self.name = "hello"
        self._age = 18

    def run(self):
        print(f'{self.name} was run away')

    def get_age(self):
        print(self._age)


class B(A):
    def get_age(self):
        print(self._age)


# 查看权限使用范围
"""
1 类的内部
2 类的外部
3 子类的内部
"""
a = A()
a.get_age()
print(a._age)
b = B()
b.get_age()
print(b._age)  # 在派生类可以被调用
# 结论 可以被继承
