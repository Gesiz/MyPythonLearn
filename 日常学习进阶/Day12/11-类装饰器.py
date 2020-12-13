class Func:
    def __init__(self, fn):
        self.__fn = fn

    # 让我们的对象() 直接就可以调用这个call方法
    def __call__(self):
        print("验证")
        self.__fn()


@Func
def my_test():
    print("登录")

my_test()

