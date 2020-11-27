# __repr__ 魔法方法
# 當把對象保存在集合數據類型中是 對他進行打印的時候會處罰這個方法
class Hero:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):  # 必須返回字符串
        return self.__repr__()

    def __repr__(self):
        return f"name:{self.name},age:{self.age}"


h1 = Hero("hell", 18)
print(h1)

h2 = Hero("apple", 18)
print(h1)

hero_list = [h1, h2]
print(hero_list)
