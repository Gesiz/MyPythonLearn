import time


def wrapper(func):
    def inner(*args, **kwargs):
        iTime = time.time()
        res = func(*args, **kwargs)
        print(f"运行时间为{time.time() - iTime}")
        return res
    return inner


@wrapper
def my_test(n):
    return [i for i in range(n)]



print(my_test(10))
