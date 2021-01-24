## find 指令-2

- **ls -l 命令放在 find命令的exec选项中**

```shell
find ./ -type f -exec ls -l {} \;
```

- **在目录中查找更改时间在n日以前的文件并删除他们**

```shell
find ./ -type f -mtime +14 -exec rm {} \;
```

- **在目录中查找更改时间在n日之前的文件并删除它们 在删除之前先给出提示**

```shell
find ./ -name "*.log" -mtime +5 -ok rm {} \;
```

- **-exec 使用 grep指令**

```shell
find /etc -name "passwd*" -exec -grep "root" {} \;
```

- **查找文件移动到指定目录**

```shell
find ./ -name "*.log" -exec mv {} .. \;
```

- **用exec 选项执行cp命令**

```shell
find ./ -name "*.log" -exec cp {} test3 \;
```
