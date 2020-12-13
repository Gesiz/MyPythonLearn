def logging(flag):
    def func_out(func):
        def func_in(num1, num2):
            if flag == "+":
                print("--正在努力加法计算--")
            elif flag == "-":
                print("--正在努力减法计算--")
            result = func(num1, num2)
            return result

        return func_in

    return func_out


@logging('+')
def add(a, b):
    result = a + b
    return result


result = add(1, 2)
print(result)
