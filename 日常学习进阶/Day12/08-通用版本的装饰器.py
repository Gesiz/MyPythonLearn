


def wrapper(func):
    def inner(*args, **kwargs):
        ret = func(*args, **kwargs)
        return ret

    return inner


@wrapper
def func(*args, **kwargs):
    return
