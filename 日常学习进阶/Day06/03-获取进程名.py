import multiprocessing


def dance():
    # 获取进程名
    print(multiprocessing.current_process())
    for i in range(5):
        print("跳舞")


if __name__ == '__main__':
    # 创建子进程
    # Process
    # target 指定任务名
    # name 子进程名
    print(f"")
    my_dance = multiprocessing.Process(target=dance, name="老王")
    my_dance.start()
    my_dance.join()
    print(f"")
