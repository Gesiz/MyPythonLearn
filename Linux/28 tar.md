## tar指令

```shell
	# 打包和压缩。打包是指将一大堆文件或目录变成一个总的文件；压缩则是将一个大的文件通过一些压缩算法变成一个小文件
	-A 新增压缩文件到已存在的压缩
    -B 设置区块大小
    -c 建立新的压缩文件
    -d 记录文件的差别
    -r 添加文件到已经压缩的文件
    -u 添加改变了和现有的文件到已经存在的压缩文件
    -x 从压缩的文件中提取文件
    -t 显示压缩文件的内容
    -z 支持gzip解压文件
    -j 支持bzip2解压文件
    -Z 支持compress解压文件
    -v 显示操作过程
    -l 文件系统边界设置
    -k 保留原有文件不覆盖
    -m 保留文件不被覆盖
    -W 确认压缩文件的正确性
    可选参数如下：
    -b 设置区块数目
    -C 切换到指定目录
    -f 指定压缩文件
    --help 显示帮助信息
    --version 显示版本信息
```

- **使用 tar 对文件进行打包**

```shell
# 解包 
	tar -xvf FileName.tar
# x 从压缩的文件中提取文件 v 显示操作过程 f 指定压缩文件

# 打包 
	tar -cvf FileName.tar DirName
# c 建立新的压缩文件 
```

- **对 .gz 文件类型进行 压缩与解压**

```shell
# 解压 
	gunzip FileName.gz
	gzip -d FileName.gz
# 压缩 
	gzip FileName
	
.tar.gz .tgz
# 解压  z 支持compress解压文件
	tar zxvf FileName.tar.gz
# 压缩  j 支持bzip2解压文件
	tar zcvf FileName.tar.gz DirName
```

- **对 .bz2文件类型进行 压缩与解压**

```shell
# 解压
	bzip2 -d FileName.bz2
	bunzip2 FileName.bz2
# 压缩
	bzip -z Filename

.tar.bz2
# 解压
	tar -jxvf FileName.tar.bz2
# 压缩
	tar -jcvf Filename.tar.bz2 DirName
```

- **对 .bz 文件类型进行 压缩与解压**

```shell
# 解压
	bzip2 -d FileName.bz
	bunzip2 FileName.bz

.tar.bz
# 解压
	tar jxvf FileName.tar.bz
```

- 

```shell

```

- 

```shell

```

- 