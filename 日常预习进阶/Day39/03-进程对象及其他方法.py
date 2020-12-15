# 进程对象及其他方法
from multiprocessing import Process, current_process
import time
import os


def task():
    # print(f"{current_process().pid} is running")  # 查看当前进程的进程号
    print(f"{os.getpid()} is running2")  # 查看当前进程的进程号
    time.sleep(3)


# 一台计算机上面 运行着很多进程 那么计算机是如何区分并管理这些进程和服务的呢
# 计算机会给每一个运行的进程分配一个PID号
# 如何查看呢
# windows 电脑 进入 cmd 输出 tasklist 即可查看 tasklist | findstr PID
# mac 电脑 进入终端之后 输出 ps aux | grep 端口名

if __name__ == '__main__':
    p = Process(target=task)
    p.start()
    p.terminate()  # 杀死当前进程
    # 告诉操作系统帮你去杀死当前进程 但是需要一定的时间 而代码运行速度极快
    time.sleep(0.1)
    print(p.is_alive())  # 判断当前进程是否存活
    """
    一般情况下 我们会默认将
    存储布尔值的变量名 和返回的结果是布尔值的方法名都以 is_开头
    """
    # print(f"主 进程 {current_process().pid}")
    print(f"{os.getpid()} is running1")
    print(f"{os.getppid()} parent is running")

