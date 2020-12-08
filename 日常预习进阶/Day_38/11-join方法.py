# join 方法
# 是让主进程代码 等待主进程代码运行结束之后
# 再继续运行 不影响子进程的运行

from multiprocessing import Process
import time

def task(name,n):
    print(f'{name} is running')
    time.sleep(n)
    print(f'{name} is over')


if __name__ == '__main__':
    # 1 创建一个对象
    p1 = Process(target=task,args=('jason',1))
    p2 = Process(target=task,args=('egon',2))
    p3 = Process(target=task,args=('tank',3))
    # 容器类型无论里面几个元素 建议一定用逗号隔开
    # 2 开启进程
    p1.start()  # 告诉操作系统帮你创建一个程序  异步
    p2.start()  # 告诉操作系统帮你创建一个程序  异步
    p3.start()  # 告诉操作系统帮你创建一个程序  异步
    # p.join()
    print("主")