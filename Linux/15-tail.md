## tail  指令

```shell
tail [必要参数] [选择参数] [文件]
	#用来显示指定文件末尾的内容 不指定文件时 作为输入信息进行处理 常用查看日志文件
	-f 循环读取
	-q 不显示处理信息
	-v 显示详细的处理信息
	-c  数目 显示的字节数
	-n  行数 显示行数
	-pid --quiet --silent 从不输出给文件名的首部
	-s --sleep-interval=S 与-f合用 便是每次反复的间隔休眠S秒
```

- **显示文件末尾的内容**

```
tail -n 5 file
```

- **循环查看文件内容**

```
tail -f file
```

- **从第五行开始显示文件**

```
tail -n +5 file
```
