## mkdir 指令

```shell
mkdir [选项] 目录
	-m --mode=模式 设定权限<模式>
	-p --parents 可以是一个路径名称 若此时路径中的某些目录尚不存在 加上此选项后 系统将自动建立好哪些尚不存在的目录 即一次可以建立多个目录
	-v --verbose 每次创建新目录都显示信息
	--version 输出版本信息
	--help 显示此帮助信息并退出
```

- **创建一个新目录**

```shell
mkdir ./dir
```

- **递归创建多个目录**

```shell
mkdir ./dir/dir
```

- **创建权限为777的目录**

```shell
mkdir -m 777 ./dir
```

- **创建新目录都显示信息**

```shell
mkdir -v ./dir
```

- **一个命令创建项目的目录结构**

```shell
mkdir -vp scf/{lib/,bin/,doc/{info,product},logs/{info,product},service/deploy/{info,product}}
```

