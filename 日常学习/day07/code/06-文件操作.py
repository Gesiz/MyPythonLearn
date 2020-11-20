# 打开文件 读写文件 关闭文件
# open(file ,mode='r',encoding)
# file 要打开的文件
# mode 要打开的文件 str
# encoding 文件的编码 将我们认识的内容转换为二进制文件 常见的话你妈又两种utf-8 和 gbk
# utf-8 将一个中文字符 转换成三个字节 gbk将一个中文字符 转换为两个字节去处理
# 返回值 返回一个文件对象 后续对所有文件的所有操作都需要借助这个对象
# w 方式打开文件 文件不存在会创建文件文件存在会覆盖文件
f = open("aa", "w", encoding="utf-8")
f.write('hello python')
f.write("你好中国")
f.close

# 1 使用代码程序open函数打开文件 windows下默认使用的是gbk编码 mac linue 默认使用utf-8
# 2 f.write('你好') 将中文使用gbk的编码写入硬盘中
# 3 在python 中打开的文件默认使用的编码是utf-8

# 解决方案 保持两者的编码一致即可
# open 打开文件 指定使用utf-8 推荐
# pycharm 中设置显示格式