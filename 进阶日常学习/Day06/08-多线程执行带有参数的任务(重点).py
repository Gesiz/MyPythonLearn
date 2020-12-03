import time
import threading
def dance(count,tw):
    for i in range(count):
        print(f"dancing {i} {tw}")
        time.sleep(1)
        

if __name__ == '__main__':
    # 2 创建子线程
    my_dance = threading.Thread(target=dance,args=(5,),kwargs={"tw":111})
    my_dance.start()