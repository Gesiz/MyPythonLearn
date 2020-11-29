# 函数中的异常传递问题
def test1():
    print("t 1 1")
    print(num)
    print("t 1 2")


def test2():
    print("t 2 1")
    test1()
    print("t 2 2")


def test3():
    try:
        print("t 3 1")
        test1()
        print("t 3 2")
    except Exception as result:
        print(result)

    print("t 3 3")


test3()
print("--------------")
