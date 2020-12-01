# 内置函数可以获得可迭代对象的长度
# 插入字符串 列表 元组 字典 集合 实现一个类似的功能的函数
# 获得数据的长度



def my_len(obj):
    """
    获得obj对象的长度
    @return:
    """
    pass

    if not isinstance(obj, (str, set, list, dict)):
        return None

    length = 0
    for item in obj:
        length += 1

    return length


if __name__ == '__main__':
    print(my_len([1, 2, 3, 4, 5, 1, 6, 7]))
