import time


def wrapper(func):
    @wr
    def inner():
        iTime = time.time()
        func()
        print(f"运行时间为{time.time() - iTime}")

    return inner


@wrapper
def my_test():
    for i in range(100000):
        print(i)


my_test()
