str_int_dic = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
}


def my_int(string):
    """
    将字符串转成int类型
    不考虑string的类型 默认就是符合要求的字符串
    传入字符串”432“返回证书432

    @return:
    """
    res = 0
    for item in string:
        int_value = str_int_dic[item]
        res = res * 10 + int_value
    return res


if __name__ == '__main__':
    print(my_int("341"))
