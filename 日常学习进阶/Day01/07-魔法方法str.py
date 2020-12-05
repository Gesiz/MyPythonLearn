# __str__ 魔法方法
# print打印一個對象的時候會調用這個對昂的__str__方法
# __str__方法必須返回支付穿
class Hero:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):  # 必須返回字符串
        return f"name:{self.name},age:{self.age}"


h1 = Hero("hell", 18)
# print(h1)

h2 = Hero("apple", 18)
# print(h1)

hero_list = [h1, h2]
print(hero_list)
