import threading
import time

g_num = []

# 结论 由于线程是依附于进程的 一个进程中的所有线程都是使用同一片内存空间
# 一个进程中的 线程是共享全局变量

def my_write():
    global g_num

    for i in range(5):
        g_num.append(i)


def my_read():
    global g_num
    print(g_num)


if __name__ == '__main__':
    sub_write = threading.Thread(target=my_write)
    sub_read = threading.Thread(target=my_read)
    sub_write.start()
    time.sleep(1)
    sub_read.start()

