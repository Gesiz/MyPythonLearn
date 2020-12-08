# 代码开启进程和线程的方式代码书写基本是一致的
# 第一种
# from multiprocessing import Process
# import time
#
# def task(name):
#     print(f'{name} is running')
#     time.sleep(3)
#     print(f'{name} is over')
#
#
# if __name__ == '__main__':
#     # 1 创建一个对象
#     p = Process(target=task,args=('jason',))
#     # 容器类型无论里面几个元素 建议一定用逗号隔开
#     # 2 开启进程
#     p.start()  # 告诉操作系统帮你创建一个程序  异步
#     print("主")

# 第二种方式 类的继承
from multiprocessing import Process
import time


class MyProcess(Process):
    def run(self):
        print('hello bf gitl')
        time.sleep(1)
        print('get out')


if __name__ == '__main__':
    p = MyProcess()
    p.start()
    print("主")


# 总结创建进程就是在内中 申请已快内存空间 将需要运行的代码丢进去1一个进程就是在内存中一块独立的空间 多个进程对应在内存中是多块独立的内存空间
# 进程与进程之间的数据默认情况下是无法直接交互 如果向交互 可以借助于第三方工具


