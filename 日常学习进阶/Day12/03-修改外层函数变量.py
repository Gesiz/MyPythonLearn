# 1 在函数嵌套 函数里定义函数 的前提下
# 2 内部函数使用了外部函数的变量 还包括外部函数的参数
# 3 外部函数返回了内部函数

def func_out(data):
    num1 = 100
    print("外层函数1：", num1)

    def func_in():
        print(data)
        nonlocal num1  # 修改外层函数 就近原则
        num1 = 1000

        print("内部函数2", num1)

    # 执行func_in 这个时候变成了1000
    func_in()
    print(num1)
    return func_in


func_out(10)()
func_out(10)
