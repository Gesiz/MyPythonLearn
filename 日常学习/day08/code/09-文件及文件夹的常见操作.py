# 想要使用这些操作 必须先导入os模块 所有涉及文件名的操作 都可以使用相对路径 也可以使用绝对路径
import os

# 1.重命名 os.rename(原文件，新文件名) 源文件不存在 程序会报错
# os.rename("bb.txt", "a.txt")
# 2.删除文件 os.remove(文件名)
# os.remove("a.txt")
# 3.创建目录(文件夹) os.mkdir(目录存在) 目录存在 程序报错
os.mkdir("test")
# 4. 获取当前的目录 os.getpwd() 返回的是当前所在的绝对路径(get current working directory)
result = os.getcwd()
print(result)
# 5. 修改当前所在的目录os.chdir("路径") 切换目录
os.chdir('test')
print(os.getcwd())
os.chdir('../')
# 6. 获取目录中所有目录 os.listdir(路径)  返回值是列表 目录中的文件 入宫不屑路径
# 则默认是在当前所在的目录
buf_list = os.listdir()
print(buf_list)
# 7 删除目录
os.rmdir("test")
result = os.getcwd()
print(result)
# 8 判断文件是否存在 os.path.exists(文件名)
if os.path.exists('bb.text'):
    os.remove('bb.text')
else:
    print("文件不存在")