# 烤地瓜
# 1 地瓜有自己的狀態 默認是生的 地瓜可以進行燒烤
# 2 地瓜有自己燒烤的總時間 由每次燒烤的時間纍加得出
# 3 地瓜燒烤時 需要提供 本次燒烤的時間
# 4 地瓜燒烤時 地瓜狀態隨著燒烤總時間變化而變化
# 5 輸出地瓜時間 可以顯示地瓜的狀態和燒烤的總時間
# 6 可以添加佐料 還可以添加任意多個佐料

"""
類目：
    SweetPotato
屬性：
    狀態：status = ”生的“
行爲：
    燒烤 def cook(self，time)
    魔法方法 def __str__(self)
    添加佐料 add_condiment
"""


class SweetPotato:

    # 屬性
    def __init__(self):
        self.status = "生的"
        self.total_time = 0
        self.condiments = []

    # 對象方法
    def cook(self, time):
        # 總時間進行纍加
        self.total_time += time
        # 根據總時間範圍 設置對象的狀態
        if 0 <= self.total_time <= 3:
            self.status = '生的'
        elif 3 <= self.total_time <= 6:
            self.status = '半生不熟'
        elif 6 <= self.total_time < 8:
            self.status = '熟了'
        else:
            self.status = '糊了'

    # 添加佐料
    def add_condiments(self, condiments):
        self.condiments.append(condiments)

    def __str__(self):
        istr = "無"
        condiments = ','.join(self.condiments)
        return f"地瓜的狀態是:「{self.status}」," \
               f"地瓜的總時間是:「{self.total_time}," \
               f"添加的佐料是「{condiments if bool(condiments) else istr}」"


potato = SweetPotato()
# print(potato.status)
# print(potato.total_time)
potato.cook(3)
print(potato)
potato.cook(2)
print(potato)
potato.cook(2)
print(potato)
potato.condiments.append("甜")
potato.condiments.append("辣")
print(potato)

# 吃地瓜 誰吃地瓜 誰--》 對象(人)
# 類名：
"""
類名：
    People
屬性：
    吃了哪些東西 food_list = []
方法：
    吃 def eat(self,food)
"""


class People:
    def __init__(self):
        self.food_list = []

    def eat(self, food):
        self.food_list.append(food)

    def __str__(self):
        iStr = ",".join(self.food_list)
        return iStr


p = People()
p.eat("西瓜")
p.eat("香蕉")
print(p)
