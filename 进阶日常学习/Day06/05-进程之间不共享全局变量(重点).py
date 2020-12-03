#  导入模块

import multiprocessing
import time

# 全局变量列表

g_num = []


def my_write():
    """向全局变量g_num 写入数据"""
    global g_num
    for i in range(5):
        g_num.append(i)


def my_read():
    """读取全局变量g_num的值"""
    global g_num
    print(g_num)


if __name__ == '__main__':
    my_write = multiprocessing.Process(target=my_write)
    my_read = multiprocessing.Process(target=my_read)

    my_write.start()

    my_read.start()
