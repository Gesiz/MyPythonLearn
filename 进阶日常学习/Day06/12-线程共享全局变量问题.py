import threading

g_num = 0


def sum_num1():
    global g_num

    for i in range(1000000):
        g_num += 1

    print("sum_num1", g_num)


def sum_num2():
    global g_num
    for i in range(1000000):
        g_num += 1
    print("sum_num1", g_num)


if __name__ == '__main__':
    sum_num1 = threading.Thread(target=sum_num1)
    sum_num2 = threading.Thread(target=sum_num2)
    sum_num1.start()
    sum_num2.start()
