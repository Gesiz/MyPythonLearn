# __init__

class Hero:
    def __init__(self, name="馬保囯", age=18):
        print("init被調用了")
        self.name = name
        self.age = age


h1 = Hero("馬雲", 45)
print(h1.name)
print(h1.age)

# 説明
# init 會在對象實例化的時候被系統自動調用 用來初始化對象的屬性
