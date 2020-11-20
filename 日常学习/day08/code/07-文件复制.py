# 获取要备份的文件名
file_name = input('请输入要备份的文件名')
# 使用切片获取文件名后缀
# 找点对应的下标
num = file_name.index('.')
new_file_name = file_name[0:num] + ['备份'] + file_name[num:]
print(new_file_name)

# 1 使用读打开原文件 rb
f = open(file_name,'rb')
buf = f.read()
f_new = open(new_file_name,'wb')
f_new.write(buf)
f.close()
# 2 读取原文件中内容
# 3 使用写打开新文件 wb
# 4 将第二步读取的内容 写入到新文件中
# 5 关闭源文件
