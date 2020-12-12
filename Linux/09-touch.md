## touch 指令

```shell
touch [选项] 文件
		-a 只更改存取时间
		-c 不建立任何文档
		-d 使用指定的日期时间 而非现在的时间
		-f 此参数将忽略不计处理 仅负责解决BSD版本touch指令的兼容问题
		-m 或--time=mtime 或--time=modify 只更改变动时间
		-r 把指定文档或目录的日期时间 统统设成和参考文档或目录的日期时间相同
		-t 使用指定的日期时间 而非现在的时间
```

- **创建不存在的文件**

```shell
touch file1 file2
```

- **若文件不存在 则不创建文件**

```shell
touch -c file1
```

- **文件1更新变为文件2 相同时间戳**

```shell
touch -r file1 file2
```

- **设置文件时间戳**

```shell
touch -t 201211142234.50 file
		-t time 作为知道那个文件相应的时间戳的新值 time规定为如下形式的十进制数
		[[CC]YY]MMDDhhmm[.SS]
```

