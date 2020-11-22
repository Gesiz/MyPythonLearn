def inputStuinfo():
    iList = []
    while True:
        opt = input("请输入数字(0表示关闭数字:1表示输入)")
        if opt == "1":
            name = input("请输入名字")
            zy = input("请输入专业")
            nj = input("请输入年级")
            bn = input("请输入班级")
            iList.append([name, zy, nj, bn])
        elif opt == "0":
            with open(file="student.txt", mode="w", encoding="utf-8") as f:
                f.write(str(iList))
            break
        else:
            print("只能输入0或1 请重新输入!")
            continue


def readFile():
    with open(file="student.txt", mode="r", encoding="utf-8") as f:
        iList = eval(f.read())
        for i in iList:
            print(f"姓名: {i[0]}, 专业: {i[1]}, 年级: {i[2]} ,班级: {i[3]}")


if __name__ == '__main__':
    inputStuinfo()
    readFile()
