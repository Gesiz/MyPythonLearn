import multiprocessing


def dance(count):
    # 获取进程名
    print(multiprocessing.current_process())
    for i in range(count):
        print(f"跳舞{count}")


if __name__ == '__main__':
    # 创建子进程
    # Process
    # target 指定任务名
    # name 子进程名
    print(f"")
    # 执行带有参数的任务
    # my_dance = multiprocessing.Process(target=dance, name="老王", args=(5,), kwargs={"count":5})
    my_dance = multiprocessing.Process(target=dance, name="老王", kwargs={"count": 5})
    my_dance.start()
    my_dance.join()
    print(f"")
