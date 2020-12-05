# 存放家具
# 家具分不同的類型 並占用不同的面積
# 輸出家具信息時 顯示家居的類型和家具占用的面積

# 房子有自己的地址和占用的面積
# 房子可以添加家具 如果房子的剩餘面積可以容納家具 則提示家具添加成功 否則提示添加失敗
# 5 輸出房子信息時 可以顯示房子的地址 占用100% 剩餘面積

# 家具類
"""
類名
    Furniture
屬性
    name
    area
方法
    pass
"""


class Furniture:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        # return f"name:{self.name},area:{self.area}"
        return self.__repr__()

    def __repr__(self):
        return self.name


# f1 = Furniture("椅子", 3)
# print(f1)

# 房子類
"""
類名:
    Hourse
屬性:
    地址 address
    佔地面積 total_area
    剩餘面積 free_area
方法:
    添加家具 add_furniture(self,furniture)
"""


class House:
    def __init__(self, address, total_area):
        self.address = address
        self.total_area = total_area
        self.free_area = self.total_area
        self.furniture_list = []

    def add_furniture(self, furniture):
        # 如果房子剩餘面積大於家具面積的時候
        # 才可以添加 否則提示添加失敗
        if self.free_area > furniture.area:
            self.furniture_list.append(furniture)
            self.free_area -= furniture.area
        else:
            print("添加失敗")

    def __str__(self):
        furniture_list = [furniture.name for furniture in self.furniture_list]

        return f"房子的地址 {self.address}, " \
               f"房子的佔地面積 {self.total_area}, " \
               f"房子的剩餘面積 {self.free_area}, " \
               f'房子裏的家具有 {",".join(furniture_list)}' \



# 調用方法
f1 = Furniture('椅子', 3)
f2 = Furniture('桌子', 5)
h1 = House("北京", 100)
h1.add_furniture(f1)
h1.add_furniture(f2)
print(h1)

