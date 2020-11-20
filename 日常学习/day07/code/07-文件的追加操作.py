# 1 打开文件 追加的方式打开文件
f = open('bb.txt', 'a', encoding='utf-8')
# 2 写文件 向文件写入内容 使用 write() 方法
# write() 函数的返回值是字节数
print(f.write("hello"))
# 写入换
f.write('\n')
print(f.write("你好"))  # 汉字在字符串里 一位占一位
f.write('\n')
# 3 关闭文件
f.close()
