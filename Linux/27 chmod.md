## chmod 命令

- **增加文件所有用户组可执行权限**

```shell
chmod a+x log2012.log
```

- **同时修改不同用户权限**

```shell
chmod ug+w,o-x log2012.log
# 即设定文件text的属性为：文件属主（u） 增加写权限;
# 与文件属主同组用户（g） 增加写权限;其他用户（o） 删除执行权限
```

- **删除文件权限**

```shell
chmod a-x log2012.log
```

- **使用“=”设置权限** 

```shell
chmod u=x log2012.log
# 撤销原来所有的权限，然后使拥有者具有可执行权限 
```

- **对一个目录及其子目录所有文件添加权限** 

```shell
chmod -R u+x test4
# 递归地给test4目录下所有文件和子目录的属主分配权限 
```

```shell
chmod 751 file   
# 给file的属主分配读、写、执行(7)的权限，给file的所在组分配读、
# 执行(5)的权限，给其他用户分配执行(1)的权限
chmod u=rwx,g=rx,o=x file 
# 理论同上

chmod =r file 
# 为所有用户分配读权限

chmod 444 file 
# 同上

chmod a-wx,a+r   file
# 同上
```
