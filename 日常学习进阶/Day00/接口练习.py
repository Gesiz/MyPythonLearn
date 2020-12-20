iDict = {}


def out(state):
    def wrappy(func):
        iDict[state] = func
        def inner(*args, **kwargs):
            return func(*args, **kwargs)

        return inner

    return wrappy


@out("qwe")
def myfunc1():
    print(111)


@out("asd")
def myfunc2():
    print(222)


if __name__ == '__main__':
    iDict["qwe"]()
