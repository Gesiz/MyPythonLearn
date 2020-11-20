def readFileline() -> int:
    f = open('bb.txt', mode='r', encoding='utf-8')
    # 按行读取 一次读取一行的内容 文件对象.readline()
    buf = f.readline()  # 参数 不够一行的长度
    print(buf)
    # 按行读取 一次读取所有行 文件对象.readlines() -->列表
    # 列表中的每一个数据是一行的内容
    buf_list = f.readlines()
    print(buf_list)
    f.close()
    return 0
