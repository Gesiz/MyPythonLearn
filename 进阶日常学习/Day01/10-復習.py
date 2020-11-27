# 類的定義
class Person:
    # 屬性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 方法
    def eat(self):
        print(f"{self.name}在吃飯")


# 創建對象
p1 = Person("嗎", 11)
p1.eat()
