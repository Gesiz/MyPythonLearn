# 函数bin可以获得整数的二进制形式

def my_bin(value):
    """
    返回正整数value的二进制形式

    @param value:
    @return:
    """
    lst = []
    while value:
        if value % 2 == 1:
            lst.append('1')
        else:
            lst.append('0')

        value = value >> 1

    lst = lst[::-1]
    return ''.join(lst)


if __name__ == '__main__':
    print(my_bin(3))


