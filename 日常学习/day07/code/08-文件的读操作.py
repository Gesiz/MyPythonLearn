# 1 打开文件1读打开文件 使用的是r
# 文件不存在 会报错
f = open('bb.txt', mode="r", encoding="utf-8")
# 2 读文件 文件对象.read(n)
# n 代表一次读取多少个字节的内容 默认不屑 读取全部内容
# 返回值 读取到的一个内容
print(f.read())
# 3 关闭文件
f.close()
