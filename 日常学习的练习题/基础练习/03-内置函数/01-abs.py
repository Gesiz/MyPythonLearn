# abs函数返回数字的绝对值 请实现下面函数 模仿abs函数的功能 返回数字的绝对值

def my_abs(number):
    if not isinstance(number, (float, int)):
        return number

    if number < 0:
        number *= -1
        return number
