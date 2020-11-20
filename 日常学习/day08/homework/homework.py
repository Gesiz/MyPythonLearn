# conding=utf-8

def writeMovie():
    with open(file="moive.txt", mode="w", encoding="utf-8") as f:
        f.write("功夫，周星驰\n一出好戏，黄渤\n我不是药神")


def readLine():
    with open(file="moive.txt", mode="r", encoding="utf-8") as f:
        print(f.read())
        f.seek(0,0)
        print("从此处一行一行读")
        for i in f.readlines():
            print(i)
        f.seek(0, 0)
        while True:
            content = f.readline()
            if content == "":
                break

import os

def 


if __name__ == '__main__':
    writeMovie()
    readLine()
