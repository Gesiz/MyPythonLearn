## head 指令

```shell
head [参数] [文件]
	-q 隐藏文件名
	-v 显示文件名
	-c 字节 显示字节数
	-n 行数 显示行数
```

- **显示文件前n行**

```
head -n 5 file
```

- **显示文件前n个字节**

```
head -c 20 file2
```

- **文件的除了最后n个字节以外的内容**

```
head -c -32 file
```

- **谁出除了文件最后n行的全部内容**

```
head -n -6 file
```