# coding="utf-8"
menu_msg = """
*********************
        1 添加学生
        2 删除学生
        3 修改学生信息
        4 查询学生信息
        5 查询所有学生信息
        6 退出程序
*********************
"""


def TF(num):
    for i in user_info:
        if num in i.values():
            return False
    return True


def add_stu(user_info):
    num = input("请输入添加的学号")

    if TF(num):
        name = input("请输入姓名")
        age = input("请输入年龄")
        sex = input("请输入性别")
        user_info.append({"key": num, "name": name, "age": age, "sex": sex})
        print("添加完成")
    else:
        print("学号已存在")
        return False


def del_stu(user_info):
    num = input("请输入要删除的学号")
    if TF(num):
        print("学号不存在")
    else:
        for i in user_info:
            if i["key"] == num:
                user_info.remove(i)
                print("删除成功")


def mod_stu():
    num = input("请输入要修改的学号")
    if TF(num):
        print("学号不存在")
    else:
        name = input("请输入姓名")
        age = input("请输入年龄")
        sex = input("请输入性别")
        for i in user_info:
            if i["key"] == num:
                user_info.remove(i)
                user_info.append({"key": num, "name": name, "age": age, "sex": sex})

    pass


def find_stu(user_info):
    num = input("请输入要查询的学号")
    if TF(num):
        print("学号不存在")
    else:
        for i in user_info:
            if i["key"] == num:
                print("学号:", i["key"], "姓名:", i["name"], "年龄:", i["age"], "性别:", i["sex"])
    pass


def find_all_stu(user_info):
    if len(user_info) == 0:
        print("现在列表里没有数据哦")
    else:
        for i in user_info:
            print("学号:", i["key"], "姓名:", i["name"], "年龄:", i["age"], "性别:", i["sex"])


pass

menu = {
    "1": add_stu,
    "2": del_stu,
    "3": mod_stu,
    "4": find_stu,
    "5": find_all_stu,
}

if __name__ == "__main__":
    user_info = [{"key": "1", "name": "wx", "age": "15", "sex": "南"}]
    while True:
        opt = input(menu_msg)
        if opt in menu:
            menu[opt](user_info)
