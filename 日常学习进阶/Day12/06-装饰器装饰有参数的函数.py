import time


def wrapper(func):
    def inner(*args, **kwargs):
        iTime = time.time()
        func(*args, **kwargs)
        print(f"运行时间为{time.time() - iTime}")

    return inner


@wrapper
def my_test(n):
    for i in range(n):
        print(i)


my_test(10)
