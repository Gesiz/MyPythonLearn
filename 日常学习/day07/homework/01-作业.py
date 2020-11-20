# 题目
# 题干 使用递归求 1-100 累加的和

def sumSum(n):
    if n == 1:
        return n
    return sumSum(n - 1) + n


def writeText(nStr):
    with open(file="a.txt", mode="w", encoding="utf-8") as f:
        f.write(nStr)


def readText():
    with open(file="a.txt", mode="r", encoding="utf-8") as f:
        print(f.read())


if __name__ == "__main__":
    print(sumSum(5))
    writeText("好好学习 天天向上")
    readText()
