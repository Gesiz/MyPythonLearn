"""



"""

from multiprocessing import Process
import time


def run():
    print("hello world")
    time.sleep(3)
    print("get out")


if __name__ == '__main__':
    p = Process(target=run)
    p.start()
    print("主")
"""
死了但是没有死透
当你开设了子进程之后 该进程死后不会立即 释放占用的进程号
因为我要让父进程能够看到他开设的子进程的一些基本信息 占用pid号 运行时间
所有的进程都会步入僵尸进程
    父进程不死并且在无限制创建子进程 且子进程也不结束
    回收子进程占用的PID号 
        父进程等待子进程运行结束
        父进程调用join方法 
"""
# 孤儿进程
"""
子进程存货 父进程意外死亡
操作系统 会开设一个儿童福利院 专门管理孤儿进程 进行回收
"""

# 守护进程
