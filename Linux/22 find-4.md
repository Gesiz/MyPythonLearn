## find 命令的参数详解

- **根目录$HOME中查找文件名符合*.log的文件**

```shell
find ~ -name "*.log" -print
```

- **想要在当前目录及子目录中查找所有的‘ *.log‘文件**

```shell
find . -name "*.log" -print
```

- **想要的当前目录及子目录中查找文件名以一个大写字母开头的文件**

```shell
find . -name "[A-Z]*" -print
```

- **想要在/etc目录中查找文件名以host开头的文件，可以用： **

```shell
find /etc -name "host*" -print
```

- **想要查找$HOME目录中的文件，可以用： **

```shell
find ~ -name "*" -print
```

- **从根目录查找所有文件**

```shell
find / -name "*" -print
```

- **如果想在当前目录查找文件名以一个个小写字母开头，最后是4到9加上.log结束的文件：  **

```shell
find . -name "[a-z]*[4-9].log" -print
```

- **如在当前目录下查找文件权限位为755的文件**

```shell
find . -perm 755 -print
```

- **在test目录下查找文件，但不希望在test/test3目录下查找**

```shell
find test -path "text/test3" -prune -o -print
```

- **避开多个文件夹:**

```shell
find test \( -path test/test4 -o -path test/test3 \) -prune -o -print 
```

- **查找某一确定文件，-name等选项加在-o 之后**

```shell
find test \(-path test/test4 -o -path test/test3 \) -prune -o -name "*.log" -print
```

- **在$HOME目录中查找文件属主为peida的文件**

```shell
find ~ -user peida -print
```

- **为了查找属主帐户已经被删除的文件，可以使用-nouser选项。在/home目录下查找所有的这类文件**

```shell
find /home -nouser -print
```

- **在/apps目录下查找属于gem用户组的文件，可以用**

```shell
find /apps -group gem -print
```

- **要查找没有有效所属用户组的所有文件**

```shell
find / -nogroup-print
```

- **希望在系统根目录下查找更改时间在5日以内的文件**

```shell
find / -mtime -5 -print
```

- **为了在/var/adm目录下查找更改时间在3日以前的文件**

```shell
find /var/adm -mtime +3 -print
```

- **查找更改时间比文件log2012.log新但比文件log2017.log旧的文件**

```shell
find -newer log2012.log ! -newer log2017.log
```

- **查找更改时间在比log2012.log文件新的文件** 

```shell
find . -newer log2012.log -print
```

- **在/etc目录下查找所有的目录**

```shell
find /etc -type d -print 
```

- **在当前目录下查找除目录以外的所有类型的文件**

```shell
find . ! -type d -print
```

- **在/etc目录下查找所有的符号链接文件**

```shell
find /etc -type l -print
```

- **在当前目录下查找文件长度大于1 M字节的文件**

```shell
find . -size +1000000c -print
```

- **在/home/apache目录下查找文件长度恰好为100字节的文件**

```shell
find /home/apache -size 100c -print
```

- **在当前目录下查找长度超过10块的文件（一块等于512字节）** 

```shell
find . -size +10 -print
```

- **find命令从文件系统的根目录开始，查找一个名为CON.FILE的文件**

```shell
find / -name "CON.FILE" -depth -print
```

- **从当前目录开始查找位于本文件系统中文件名以XC结尾的文件**

```shell
find . -name "*.XC" -mount -print 
```