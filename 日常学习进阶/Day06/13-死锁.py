import threading

g_num = 0
# 互斥锁 保证同一时间只能由一个线程去操作

def sum_num1():
    mutex.acquire()
    if g_num == 1:
        return
    mutex.release()
    print("sum_num1", g_num)


def sum_num2():
    mutex.acquire()

    mutex.release()
    print("sum_num1", g_num)


if __name__ == '__main__':
    mutex = threading.Lock()
    sum_num1 = threading.Thread(target=sum_num1)
    sum_num2 = threading.Thread(target=sum_num2)
    sum_num1.start()
    # sum_num1.join()
    sum_num2.start()


