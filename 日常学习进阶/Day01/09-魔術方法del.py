# __del__
# 儅這個對象被銷毀的時候 會調用這個對象的__del__方法

class Hero:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print("del被調用了")


h1 = Hero("hello", 18)
del h1

h2 = Hero("hello", 18)
print("123")

# __init__ 構造方法

# __del__ 析構方法
