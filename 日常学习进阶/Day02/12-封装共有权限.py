class A:
    def __init__(self):
        self.name = "hello"
        self.age = 18

    def run(self):
        print(f'{self.name} was run away')

class B(A):
    pass

# 查看权限使用范围
"""
1 类的内部
2 类的外部
3 子类的内部
"""
a = A()
a.run()

b = B()
print(b.name)