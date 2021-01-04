## find 指令-3

- **查找系统中的每一个普通文件 然后使用xargs 命令来测试他们分别属于哪类文件**

```shell
find . -type f -print | xargs file
```

- **在整个系统中查找内存信息 转储文件(core dump) 然后把结果保存到 /tmp/core.log**

```shell
find / -name "core" -print | xargs echo "" > /tmp/core.log
```

- **在当前目录下查找所有用户具有读写 和执行权限的文件 并收回响应的写权限**

```shell
find ./ -perm -7 -print | xargs chmod o-w
```

- **用grep命令在所有普通文件中搜索 hostname这个词**

```shell
find ./ -name \* type f -print | xargs grep "hostname"
```

- 

```shell

```

- 

```shell

```

- 

```shell

```

- 