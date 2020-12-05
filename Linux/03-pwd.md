## pwd 指令

- **用pwd命令查看默认工作目录的完整路径**

```shell
pwd
```

- **目录链接时 pwd -P 显示出实际路径 而非使用link路径 pwd 显示的是连接路径**

```shell
pwd -P
```

- **pwd [选项]**

```shell
pwd 
	-L 目录连接链接时 输出连接路径
	-P 输出物理路径
```

- **当当前目录被删除时 pwd仍会显示**

```shell
[root@localhost init.d]# cd /opt/soft
[root@localhost soft]# mkdir removed
[root@localhost soft]# cd removed/
[root@localhost removed]# pwd
/opt/soft/removed
[root@localhost removed]# rm ../removed -rf
[root@localhost removed]# pwd
/opt/soft/removed
[root@localhost removed]# /bin/pwd
/bin/pwd: couldn't find directory entry in “..” with matching i-node
[root@localhost removed]# cd 
[root@localhost ~]# pwd
/root
[root@localhost ~]#
```

