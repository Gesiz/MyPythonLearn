# any 函数用于判断给定的可迭代参数 iterable中
# 所有的元素是否至少有一个为True

def my_any(lst):
    """
    列表lst中有一个Tru 则返回函数True

    @param lst:
    @return:
    """
    for item in lst:
        if item:
            return True

    return False


if __name__ == '__main__':
    print(my_any([True, False, False]))


