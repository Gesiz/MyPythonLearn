* **更新conda至最新版本**
```
conda update conda
```
* **切换环境**

```
activate <env_name>
```

* **创建环境**

```
conda create --name <env_name> <package_names>
conda create --name python2 python=2.7
```

* **复制环境**
```
conda create --name <new_env_name> --clone <copied_env_name>
```

* **查看环境 安装pyside2**
```
conda info --envs
conda info -e
conda env list

pip install pyside2 -i https://pypi.douban.com/simple/
```


* **删除环境**
```
conda remove --name <env_name> --all
```
* **PIP国内镜像 -i**
```
 阿里云 http://mirrors.aliyun.com/pypi/simple/ 
 中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/ 
 豆瓣(douban) http://pypi.douban.com/simple/ 
 清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/ 
 中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/
```

