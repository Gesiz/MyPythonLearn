"""
    生产者
        生产 制造数据的
    消费者
        霞飞 处理东西的

该模型除了上述两个之外还需要一个东西 媒介
    生活中的例子做包子的将包子做好后放在蒸笼(媒介中) 买包子的从蒸笼里拿

    生产者和消费者之间不是直接做交互的 而是通过媒介 做交互

生产者 (做包子的)  +  消息队列(蒸笼)  + 消费者(吃包子的)
"""

from multiprocessing import Queue, Process, JoinableQueue
import time, random

"""
研究思路
    1 主进程跟子进程借助于队列通信
    2 子进程跟子进程借助于队列通信

"""


def producer(name, food, q):
    for i in range(10):
        data = f'{name} 生产了 {food}, {i}'
        # 模拟延迟
        time.sleep(random.randint(1, 3))
        # 将数据放入队列中
        q.put(data)
        print(data)


def consumer(name, q):
    while True:
        food = q.get()  # 没有数据就会卡住
        # 判断是否有结束标识
        if food is None:
            break
        time.sleep(random.randint(1, 3))
        print(f'{name} 吃了 {food}')
        q.task_done()


if __name__ == '__main__':
    # q = Queue()
    q = JoinableQueue()
    p1 = Process(target=producer, args=("大厨", "包子", q))
    p2 = Process(target=producer, args=("tank", "泔水", q))
    c1 = Process(target=consumer, args=("锤哥", q), daemon=True)
    c2 = Process(target=consumer, args=("星哥", q), daemon=True)
    p1.start()
    p2.start()
    c1.start()
    c2.start()
    p1.join()
    p2.join()
    # 等待生产者 生产完毕之后 往队列中 添加 特定的结束符号
    q.join()

    """
    JoinableQuene 每当你往该队列中存入数据的时候 内部会有一个计数器进行 + 1
    每当你调用task_done 的时候 计数器-1
    p.join 当计数器为0时 才往后减少一个
    """
    # 只要q.join 执行完毕 说明消费者已经处理完数据了 消费者就没有存在的必要了

