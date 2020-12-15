# 进程间通信
# 队列 Queue
"""
队列 先进先出
堆栈 先进后出
"""

from multiprocessing import Queue

# 创建一个队列

q = Queue(5)  # 括号内可以放入数字提示生成的队列最大可以同时存放的数量  # 32767

# 往队列中存数据

q.put(111)
q.put(222)
q.put(333)
print(q.full())  # 判断队列是否满了
print(q.empty())  # 判断队列是否空了
q.put(444)
q.put(555)
# q.put(666)  # 当队列数据放满之后 程序会阻塞 直到位置有让出来

"""
存取数据 存是为了更好的取
千方百计的存 简单快捷的取

同在一个屋檐下
差距为何这么大
"""

# 去队列中取数据
v1 = q.get()
v2 = q.get()
v3 = q.get()
v4 = q.get()
v5 = q.get()
print(q.empty())

try:
    v6 = q.get(timeout=3)
except Exception as e:
    print("nothing")
# v6 = q.get_nowait()  没有数据直接报错 queue.Empty
# v6 = q.get(timeout=3)  原地等待三秒
# v6 = q.get()  # 如果没有数据的话 get 方法会原地阻塞
print(v1,v2)


"""
q.full()
q.empty()
q.get_nowait()
在对进程的情况下时不精确的
"""