msg_menu = """******************************
        1. 添加学生
        2. 删除学生
        3. 修改学生信息
        4. 查询学生信息
        5. 查询所有学生
        6. 退出系统 
******************************
请输入要选择的功能
"""


def succ():
    print("操作成功")
    return True


def print_info(name, age, sex):
    print(f"姓名:{name},年龄:{age},性别:{sex}")


def add_student(stu_info):
    num = input("请输入学生的学号")

    ch = stu_info.get(num, 0)
    if type(ch) == dict:
        print("已存在禁止添加")
        return False
    name = input("请输入学生的姓名")
    age = input("请输入学生的年龄")
    sex = input("请输入学生的性别")
    stu_info[num] = {}
    stu_info[num]["name"] = name
    stu_info[num]["age"] = age
    stu_info[num]["sex"] = sex
    return succ()


def del_student(stu_info):
    stu_info.pop(input("请输入要删除的学生学号"))
    return succ()


def mod_student(stu_info):
    opt = input("请输入要查询的学生信息")
    if exict(opt):
        name = input("请输入学生的姓名")
        age = input("请输入学生的年龄")
        sex = input("请输入学生的性别")
        stu_info.update(opt, {"name": name, "age": age, "sex": sex})
    else:
        return False
    return succ()


def find_student(stu_info):
    opt = input("请输入要查询的学生信息")
    if exict(opt):
        print_info(stu_info[opt]["name"], stu_info[opt]["age"], stu_info[opt]["sex"])
    else:
        return False
    return succ()


def find_all_student(stu_info):
    stu_in = stu_info
    find_all(stu_in)
    return succ()


def find_all(stu_in):
    for key, value in stu_in.items():
        if type(value) == dict:
            print("学号:", key, end="")
            find_all(value)
        else:
            print_info(stu_in["name"], stu_in["age"], stu_in["sex"])
            return True


def exict(opt):
    num = stu_info.get(opt, 0)
    if num == 0:
        print("该人不存在")
        return False
    return True


menu = {
    "1": add_student,
    "2": del_student,
    "3": mod_student,
    "4": find_student,
    "5": find_all_student,
}

if __name__ == "__main__":
    stu_info = {"1": {"name": "aaa", "age": "15", "sex": "男"}}  # 学生信息有 学号 姓名 年龄 性别
    while True:
        opt = input(msg_menu)
        if opt in menu:
            menu[opt](stu_info)
