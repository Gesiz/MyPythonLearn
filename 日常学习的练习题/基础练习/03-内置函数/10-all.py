# all() 函数用于判断给定的可迭代参数 iterable 中的
# 所有元素都是否为True

def my_all(seq):
    """
    如果列表里所有的元素都是True 则函数返回True 返回False
    @param seq: 列表
    @return:
    """
    for item in seq:
        if not item:
            return False

    return True


if __name__ == "__main__":
    my_all([True, False, True])


