# __init__

class Hero:
    def __init__(self, name, age, skill):
        self.name = 'hello'
        self.age = 18
        self.skill = skill

    def kong_fu(self):
        print(f"{self.name}在打{self.skill}")


h1 = Hero("Hero", 69, "五連鞭")

print(h1.name)
print(h1.age)
h1.kong_fu()
h2 = Hero("馬保囯", 50, "超能力")
print(h2.name)
print(h2.age)
h2.kong_fu()