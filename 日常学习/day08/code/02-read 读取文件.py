# 文件的读操作
# 使用r方式打开文件

def func():
    f = open('bb.txt', 'r', encoding='utf-8')
    # f 文件对象.read(n) n是一次读取到的字节数 默认是读取全部内容 返回值是读取到的一个内容
    buf = f.read()  # 一次读取全部内容
    print(buf)
    f.seek(1,)
    buf1 = f.read()  # 文件中的内容只能读取一次 读了之后不能重复的读
    # 若文件读到最后则返回的是空字符串
    print('buf1', buf1, type(buf1), len(buf1))
    f.close()

def func2():
    f = open('bb.txt','r',encoding='utf-8')
    buf = f.read(5)  # 读取5个字节的内容
    print(buf)
    buf1 = f.read(5)  # 读取5个字节的内容
    print(buf1)
    f.close()

func()