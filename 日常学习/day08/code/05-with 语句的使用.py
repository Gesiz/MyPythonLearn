# 1 打开文件
# 2 读写文件
# 3 关闭文件
# 如果使用with语句来操作文件 不需要书写关闭语句

# 文本文件 能使用姿势本程序打开的文件就是文本文件 没有特殊格式的文件
# .txt .py .md .log
# 二进制文件 不能使用记事本打开的 需要特定的软件才能打开 mp3 mp4 avi
# rmvb jpg png

# 打开方式
# 文本的方式打开 会将硬盘中的二进制代码进行解码
# 二进制方式打开 不会对二进制代码进行解析 就是二进制数据
# 结论
# 文本文件 可以使用文本方式打开文件 也可以使用二进制方式打开文件
# 二进制文件只能使用二进制方式打开
# r w a
# rb wb ab

# str 与 bytes 类型的转换