## cat 指令

```shell
cat [选项] [文件]
	# cat 主要有三大功能
	# 1 一次显示整个文件 cat filename
	# 2 从键盘创建一个文件 cat > filename 只能创建新文件 不能编辑已有文件
	# 3 将几个文件合并为一个文件 cat file1 file2 file3 > file
	-A --show-all 等价于 -vET
	-b 对非空输出行编号
	-e 等价于 -vE
	-E --show-ends 在每行结束处显示$
	-n --number 对输出的所有行编号 由1开始对所有输出的行数编号
	-s --squeeze-blank 由连续两行以上的空白行 就代换为一行的空白行
	-t 与 —vT 等价
	—T --show-tabs	将跳格字符显示为 ^I
	-v --show-nonprinting 使用特殊引用
```

- **把 file1 的文件加上行号输入到 file2 这个文件里**

```
cat -n file1 file2
```

- **把 file1 和 file2 的文件内容加上行号 空白行不加 之后将内容附加到 log.log里**

```
cat -b file1 file2 log.log
```

- **把 file 的文件内容加上行号输入 file2 这个文件中**

```
cat -n file1 > file2
```

- **使用here doc 来生成文件**

```
cat > log.txt << EOF
```

- **反向显示**

```
tac
```
