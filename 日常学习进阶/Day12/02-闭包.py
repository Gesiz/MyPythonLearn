# 1 在函数嵌套 函数里定义函数 的前提下
# 2 内部函数使用了外部函数的变量 还包括外部函数的参数
# 3 外部函数返回了内部函数

def func_out(data):
    def func_in():
        print(data)
    return func_in

func_out(199)()