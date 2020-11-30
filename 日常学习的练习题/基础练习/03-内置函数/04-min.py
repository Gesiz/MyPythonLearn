def my_min(seq):
    """
    返回序列里最小的值
    @return:
    """

    min_value = None
    if not isinstance(seq, (list, tuple)):
        return min_value
    if len(seq) == 0:
        return min_value
    min_value = seq[0]
    for item in seq:
        if not isinstance(item, (int, float)):
            continue
        if item <= min_value:
            min_value = item
    return min_value


if __name__ == '__main__':
    iList = [1, 2, 3, 4, 5, 6]
    print(my_min(iList))
