import time
import threading
import sys
def dance():
    time.sleep(1)
    sys.stdin.flush()
    print(threading.current_thread().name)
    sys.stdin.flush()


# 注意线程执行的是没有顺序的
if __name__ == '__main__':
    # 循环第一次创建出来的线程就是 thread-1
    # 循环第二次创建出来的线程就是 thread-2
    for i in range(5):
        my_dance = threading.Thread(target=dance)
        my_dance.start()