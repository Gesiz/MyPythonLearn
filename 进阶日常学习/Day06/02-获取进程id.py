# 在同一时间内执行的多个任务

# 多任务的目的 充分利用cpu 提高程序执行效率


# 并发 在一段时间内交替去执行任务(只有一个cpu)
# 并行 在同一时刻执行多个任务(多核cpu)


# 多进程 (多任务的实现方式)

# *****进程是操作系统分配资源的最小单位*****
# *****线程是操作系统使用资源的最小单位*****
# 在运行的程序就是进程


# 多进程
#
# while True:
#    print(1)
#

# 多进程的使用流程
# 1 导入模块(multiprocesing)
# 2 创建子进程(start)
# 3 开启子进程
import multiprocessing
import os
import time


def dance():
    print(f"dance 子进程id:{os.getpid()}")
    print(f"dance 父进程id:{os.getppid()}")


def sing():
    print(f"dance 子进程id:{os.getpid()}")
    print(f"dance 父进程id:{os.getppid()}")


if __name__ == '__main__':
    # 单进程 需要10秒钟头完成
    # 多进程 需要5秒钟完成

    # 注意! 运行时会产生三个进程 1个主进程 2个子进程
    # 注意! 每个进程里会有一个线程
    print(f"主进程的id在{os.getpid()}")
    # 最少有一个进程 这个进程中最少有一个线程
    # dance()
    # sing()
    # 创建子进程
    # Process:
    # target : 指定执行的任务名 (函数名)
    my_dance = multiprocessing.Process(target=dance)
    my_sing = multiprocessing.Process(target=sing)

    # 开启子进程(如果不开启不会自动执行)
    my_dance.start()
    my_sing.start()

# 进程编号
# 目的 知道子进程是由哪个主进程创建的(子进程需要主进程回收资源)
# os.getpid()  表示当前进程pid
# os.getppid()  获取父类进程pid
