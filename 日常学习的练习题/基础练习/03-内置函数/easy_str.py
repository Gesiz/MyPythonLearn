def my_str(int_value):
    """
    将int_value 转换成字符串
    @return:
    """
    if int_value == 0:
        return '0'

    lst = []
    is_positive = True
    if int_value < 0:
        is_positive = False
        int_value = abs(int_value)

    while int_value:
        number = int_value % 10
        int_value //= 10
        str_number = chr(number + 48)
        lst.append(str_number)

    if not is_positive:
        lst.append('-')

    lst = lst[::-1]

    return ''.join(lst)


if __name__ == '__main__':
    print(my_str(0))
    print(my_str(123))
    print(my_str(-1))



