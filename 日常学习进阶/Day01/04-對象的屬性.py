# 對象屬性的添加
# 對象屬性的獲取
# 對象屬性的修改
# 對象屬性的刪除


# 對於對象的增刪改查
class Hero:

    # 對象方法
    def eat(self):
        # 在方法中添加對象的屬性
        self.skill = "閃電五連鞭"
        print("麻辣燙")

    def run(self):
        # 在對象方法中獲取屬性
        # print(self.name)
        # print(self.age)
        print(f'{self.age}的{self.name}邊跑步邊打{self.skill}')

    def set_name(self, name="馬保囯"):
        self.name = name


# 對象屬性的添加

# 對對象屬性的添加
h1 = Hero()
# 類的外部添加
h1.name = '馬保囯'
h1.age = 69

# 對象屬性的獲取
# 類的外部獲取誰能夠
# print(h1.name)
# print(h1.age)
# h1.eat()
# print(h1.skill)

# 調用run方法 查看方法内獲取屬性
h1.eat()
h1.run()

# h1.name = "馬化騰"
# print(h1.name)

h1.set_name("馬雲")
print(h1.name)


# 4 對象屬性的刪除
# del h1.name
# print(h1.name)
