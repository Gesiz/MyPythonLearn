from multiprocessing import Process, Lock
import json, time, random


# 查票
def search(i):
    # 文件操作读取票数
    with open('data', 'r', encoding='utf-8') as f:
        dic = json.load(f)
    print(f'用户查询余票:{dic.get("ticket_num")}')
    # 字典取值不要用[]的形式 推荐使用get 你写的代码打死都不能报错


# 买票  1 先查 2 再买
def buy(i):
    # 先查
    with open('data', 'r', encoding='utf-8') as f:
        dic = json.load(f)
        time.sleep(random.randint(1, 3))
    # 判断当前是否有票
    if dic.get('ticket_num') > 0:
        # 修改数据库 买票
        dic['ticket_num'] -= 1
        # 写入数据库
        with open('data', 'w', encoding='utf-8') as f:
            json.dump(dic, f)
        print(f"用户{i}买票成功")
    else:
        print(f"用户{i}买票失败")


# 整合上面两个函数
def run(i,mutex):
    search(i)
    # 给买票环节加锁处理
    mutex.acquire()
    buy(i)
    mutex.release()

if __name__ == '__main__':
    # 在主进程中生成一把锁
    # 让所有子进程抢 谁先抢到谁先买票
    mutex = Lock()
    for i in range(10):
        p = Process(target=run, args=(i,mutex))
        p.start()

# 针对多个进程操作操作同一份数据的时候 会出现数据错乱的问题
# 针对上述问题 解决方式是将并发变为穿行 牺牲效率 但是保证了数据的安全
"""
扩展 行锁 表锁
    # 注意 锁不要轻易的使用 容易造成死锁现象() 我们一般写代码不会用到 
        都是内部封装好的
    # 锁只在处理数据的部分加 来保证数据安全 
"""