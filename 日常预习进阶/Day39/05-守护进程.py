from multiprocessing import Process
import time


def task(name):
    print(f"{name} is line")
    time.sleep(3)
    print(f"{name} is die")


if __name__ == '__main__':
    p = Process(target=task, args=('egon',))
    p.daemon = True  # 一定要放到 start 方法上面才会有效 否则失效
    p.start()

    print("主进程结束")

    