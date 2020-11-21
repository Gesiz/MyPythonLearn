# conding=utf-8

def writeMovie():
    with open(file="moive.txt", mode="w", encoding="utf-8") as f:
        f.write("功夫，周星驰\n一出好戏，黄渤\n我不是药神")


def readLine():
    with open(file="moive.txt", mode="r", encoding="utf-8") as f:
        for i in f:
            print(i)
        # print(f.read())
        # f.seek(0,0)
        # print("从此处一行一行读")
        # for i in f.readlines():
        #     print(i)
        # f.seek(0, 0)
        # while True:
        #     content = f.readline()
        #     if content == "":
        #         break


import os


def createDir():
    # os.mkdir("黑马")
    print(os.getcwd())
    os.listdir("./")
    # 04
    os.chdir("../")
    # 05
    os.rmdir("黑马")


def docuBak():
    msg = """请输入文件名 列如: gailun.txt"""
    docuName = input(msg)
    with open(file=docuName, mode="w", encoding="utf-8") as f, \
            open(file=docuName, mode="r", encoding="utf-8") as f2, \
            open(file=docuName + ".bak", mode="w", encoding="utf-8") as f3, \
            open(file=docuName + ".bak", mode="r", encoding="utf-8") as f4:
        f.write("功夫，周星驰\n一出好戏，黄渤\n我不是药神")
        f.flush()
        a = f2.read()
        print(a)
        f3.write(a)
        return f4.read()


if __name__ == '__main__':
    # writeMovie()
    # readLine()
    # createDir()
    print(docuBak())


