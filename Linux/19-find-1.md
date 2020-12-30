## find 指令

- **linux 下 find 指令提供相当多的查找条件 但由于其非常消耗资源 大部人更倾向于 把它放在后台运行**

```shell
find pathname -options [-print -exec -ok ...]  # 用于在文件树中查找文件
	pathname: find 命令所查找的目录的路径 
	-print find 命令 将匹配的文件进行标准输出
	-exec  对匹配的文件执行该参数所给出的 shell 命令 'command' {} \; 注意空格
	-ok 与 -exec 作用相同 只不过以一种更为安全的方式 执行
	
	-type # 查找某一类型的文件
		b  # 块设备文件
		d  # 目录
		c  # 字符设备文件
		p  # 管道文件
		l  # 符号链接文件
		f  # 普通文件
```

- **查找指定时间内修改过的文件**

```shell
find -atime -2  # 查找出 48小时内被访问过的数据
```

- **分局关键字查找**

```shell
find ./ -name "*.log"  # 在当前目录下 以log结尾的文件
```

- **按照目录或文件的权限来查找文件**

```shell
find ./ type f -name "*.log"  # 查找当前目录 以log 结尾的普通文件
```

- **查找当前所有目录并排序**

```shell
find ./ -type d | sort
```

- **按照大小查找文件**

```shell
find ./ -size +1000c -print  # 查询当前目录文件大于 1K 的文件 
```
