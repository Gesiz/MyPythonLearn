def my_max(seq):
    """
    返回数列的最大值
    @param seq:
    @return:
    """

    max_value = None
    if not isinstance(seq, (list, tuple)):
        return max_value

    if len(seq) == 0:
        return max_value

    max_value = seq[0]
    for item in seq:
        if not isinstance(item, (float, int)):
            continue
        if item > max_value:
            max_value = item
    return max_value


if __name__ == '__main__':
    lst = [2, 3, 4, 5, 6]
    print(my_max(lst))
