# 让子进程随着主进程的结束而结束的两种方式
# 1 守护进程
# 2 手动设置 销毁子进程方式
#
import multiprocessing
import time

def func():
    for i in range(5):
        time.sleep(0.2)
        print("func")


if __name__ == '__main__':
    # 程序一旦运行 就会默认创建主进程
    # 主进程会等待子进程结束之后在结束
    # 程序一旦运行 就会默认创建主进程
    my_func = multiprocessing.Process(target=func)  # daemon=True

    # 设置守护进程(注意 需要在start 之前设置 否则无效)
    # my_func.daemon = "True"

    my_func.start()
    time.sleep(0.5)

    # 手动设置
    my_func.terminate()
    print("over")
    exit()

    # 结论 主进程默认会等待子进程结束之后在结束

    # 让子进程随着主进程的结束而结束
    # 1 守护进程  daemon=True 注意！ 须在start设置之前设置
    # 2 手动结束子进程 my_func().terminate()
