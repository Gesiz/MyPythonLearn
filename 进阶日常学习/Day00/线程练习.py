# import threading
# import time
#
#
# def func2():
#     global i
#
#     while True:
#
#         if i == 52:
#             return None
#         mutex2.acquire()
#         i += 1
#         print(i, end='')
#         i += 1
#         print(i, end='')
#         mutex1.release()
#
#
#
#
# def func1():
#
#     lst = [chr(x) for x in range(65, 91)]
#
#     while True:
#         mutex1.acquire()
#         if bool(lst):
#             print(lst.pop(0))
#         else:
#             return None
#         mutex2.release()
#
#
#
#
# if __name__ == '__main__':
#     i = 0
#
#     mutex1 = threading.Lock()
#     mutex2 = threading.Lock()
#     t1 = threading.Thread(target=func1)
#     t2 = threading.Thread(target=func2)
#     mutex1.acquire()
#     t1.start()
#     t2.start()
import threading, time,multiprocessing,sys


def func1():
    while True:
        print("进程信息")
        sys.stdout.flush()
        time.sleep(1)


def func2(count):
    while count:
        print(f"循环的第{count}次")
        sys.stdout.flush()
        count -= 1
        time.sleep(1)



if __name__ == '__main__':
    p1 = multiprocessing.Process(target=func1,daemon=True)
    p2 = multiprocessing.Process(target=func2,args=(5,))
    p1.start()
    p2.start()
    p2.join()
