# sum 函数可以获取列表所有数据的总和 模仿这个功能实现下面的函数

def my_sum(lst):
    """
    返回裂变里u松油数据的综合
    如果列表里有非数字类型的数值 忽略不管
    @param lst:
    @return:
    """
    sum_res = 0

    if not isinstance(lst, list):
        return sum_res

    for item in lst:
        if isinstance(item, (float, int)):
            sum_res += item

    return sum_res


if __name__ == '__main__':
    iList = [3, 4, 5, 6, 7, '123']
    print(my_sum(iList))
