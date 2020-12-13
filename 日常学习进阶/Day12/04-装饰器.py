# 装饰器 在不修改原有代码的前提下 给函数增加新的功能

def func_out(func):

    def func_in():
        print("注册")
        func()

    return func_in


@func_out  # login = func_out(login"(原始login)")
def login():
    print("登录")


login()
# 结论 1 调用login() 相当于 ==> func_in()

#       调用被装饰的函数就相当于调用闭包中的内层函数
# 结论 2 外层函数的参数 func ==> 原始的login
