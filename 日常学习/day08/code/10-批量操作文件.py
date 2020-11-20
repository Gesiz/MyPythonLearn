import os
def createFiles(path: str):
    """
    批量创建文件
    @param path: 是指在那个目录创建文件
    @return:
    """
    for i in range(1, 11):
        file_name = f"name_{i}.txt"
        with open(path+'/'+file_name,'w') as f:
            pass

if os.path.exists('test'):
    createFiles('test')
else:
    os.mkdir('test')
    createFiles('test')

