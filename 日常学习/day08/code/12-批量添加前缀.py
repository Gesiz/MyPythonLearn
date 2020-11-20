import os
os.chdir("test")



[os.remove(i) for i in os.listdir() if not i.endswith('.txt')] # 批量删除文件

[os.rename(i, 'py_45_' + i) for i in os.listdir() if i.endswith('.txt')]  # 增加前缀

[os.rename(i, i[len('py_45_'):len(i)]) for i in os.listdir() if i.endswith('.txt')]  # 去除前缀