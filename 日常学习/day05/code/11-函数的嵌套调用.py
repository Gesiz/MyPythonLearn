# 嵌套调用
# 在一个函数中调用另外一个函数


def func1():
    print("----func1 start-------")
    print("good good study")
    print("----func2 end  -------")  # 函数执行结束之后 会回到调用的地方 继续执行


def func2():
    print("-----func2 start------")
    func1()  # 函数调用 会进入函数内部执行
    print("-----func2 end  ------")


func2()  # 函数调用 会进入函数内部执行
