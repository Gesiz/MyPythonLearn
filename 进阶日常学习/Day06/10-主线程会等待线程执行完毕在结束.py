import threading
import time

def func():
    for i in range(5):
        time.sleep(0.2)
        print("func")

# 多线程的注意点

if __name__ == "__main__":
    # 让子线程随着主线程结束而结束
    # 守护线程
    # 1 Thread(daemon=True)
    # my_func = threading.Thread(target=func,daemon=True)
    my_func = threading.Thread(target=func,daemon=True)
    # 2 setDaemon
    my_func.setDaemon(True)
    my_func.start()
    time.sleep(0.5)
    print('over')

