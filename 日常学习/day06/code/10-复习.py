msg = """
1 增加学生
2 删除学生
3 修改学生
4 寻找学生
5 查找所有学生
"""


# stu_info = {
#     "001": {"name": "xw", "age": "17"},
#     "002": {"name": "xa", "age": "27"}
#     "003": {"name": "xaa"}
# }

def add_stu(info):
    opt = input("请输出您想添加的学号")
    if opt in info:
        return print("已存在")
    else:
        info[opt] = {}
        name = input("请输入您的姓名")
        info[opt]["name"] = name
        age = input("请输入您的年龄")
        info[opt]["age"] = age
        return print("已完成")


def del_stu(info):
    opt = input("请输出您想添加的学号")
    if opt in info:
        del info[opt]
    else:
        return print("您输入的学号不存在无法删除")


def mod_stu(info):
    pass


def find_stu(info):
    pass


def find_all_stu(info):
    print(info)
    pass


iDict = {
    "1": add_stu,
    "2": del_stu,
    "3": mod_stu,
    "4": find_stu,
    "5": find_all_stu
}


def main():
    stu_info = {
        "001": {"name": "xw", "age": "17"},
        "002": {"name": "xa", "age": "27"}
    }
    while True:
        opt = input(msg)
        if opt in iDict:
            iDict[opt](stu_info)


main()
