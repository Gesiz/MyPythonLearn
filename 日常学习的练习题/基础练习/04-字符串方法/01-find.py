def my_find(source, target, start=0):
    """
    返回字符串source中 子串target開始的位置 从start索引开始搜索
    如果可以找到多个返回第一个
    @param source:
    @param target:
    @param start:
    @return:
    """
    if not source or not target:
        return -1

    # 处理不合理的搜索起始位置
    if start < 0 or start >= len(source):
        return -1

    if len(target) > len(source):
        return -1

    for index in range(start, len(source) - len(target) + 1):
        t_index = 0
        while t_index < len(target):
            if target[t_index] == source[t_index + index]:
                t_index += 1
            else:
                break

        if t_index == len(target):
            return index
    return -1


if __name__ == '__main__':
    print(my_find('this is a book', 'a'))

