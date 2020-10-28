# coding:utf-8

# 模块:
# 1 开启新的旅程
# 2 拿来主义
# 3 以文件的行书管理代码

# 模块的分类
# 1 自定义模块
# 2 内置模块
# 3 第三方模块

# 自定义模块
# 模块 .py 文件就是一个模块
# 自定义一个.py文件
# import 导入
# print(globals())
# import test  # 获取所有内容
#
# print(globals())
#
# a = 20
# # import test
# # print(a)
# # print(test.a)
#
# from test import a as aa
#
# print(a)
# print(aa)

# from test import *
# from test import * func,foo
# 不同处一个文件分别import

# import sys
#
# print(sys.path)
#
# # for i in sys.path:
# #     print(i + "\\推导式")
#
# from Day_10 import Day10 as t
#
#
# # 导入顺序 内存 内置 sys.path
# # 模块安装 pip install 模块名
#
# # 模块的梁中原东路
# # 1 被当做脚本执行
# # 2 被当做模块执行
#
# def func():
#     print("this is a")
#
#
# if __name__ == '__main__':  # 启动接口
#     func()
#
# print(__name__)
#

# time分类
# 1 结构化时间 给程序员
# 2 时间戳 给程序员做计算
# 3 字符串时间 给用户看的 2020年10月14日10:15:35
# import time
#
# print(time.time())  # 时间戳
# print(time.localtime())  # 结构化时间
# t = time.localtime(time.time())
# print(t.tm_year)
# print(time.strftime("%Y-%m-%d %H:%M:%S", t))  # 字符串时间
#
# # 将字符串时间转换成时间戳
# str_time = "2020-10-14 10:22:52"
# t_time = time.strptime(str_time, "%Y-%m-%d %H:%M:%S")
# print(time.mktime(t_time))  # 转换为时间戳

# time.time()  # 时间戳
# time.sleep()  # 睡眠
# time.localtime()  # 将时间戳转换为结构化时间
# time.strftime()  # 将结构时间可以转化为字符串时间
# time.strptime()  # 将字符串时间转换为结构时间
# time.mktime()  # 将结构化时间转换为时间戳


# datetime 是封装了time 在time的基础上增加了新的功能
# from datetime import datetime, timedelta
#
# print(datetime.now())  # 获取当前时间
# print(datetime(2019, 10, 1, 12, 13, 14))  # 自定义时间
# s = str_time = "2019-10-01 12:13:14"
# print()
# year, time = str_time.split(" ")
# for i in year.split("-"):
#     print(int(i))
# print(datetime.strptime(str_time, "%Y-%m-%d %H:%M:%S") - datetime(2018, 10, 12))  # 将字符串时间转换成时间对象
#
# import time
#
# t = time.time()
# print(datetime.fromtimestamp(t) - datetime(2018, 10, 12))
# print(datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S"))  # 时间对象转换为字符串
# print(datetime.timestamp(datetime.now()))  # 时间对象转换为时间戳
#
# print(datetime.now() - timedelta(days=365))

# random
# from random import random
#
# print(random())
#
# import random
#
# print(random.random())  # 0~1 随机小数
# print(random.random() * 10)  # 0~10 随机整数
# print(random.randint(1, 10))  # 1-10 随机整数
# lst = [1, 2, 3, 4, 5, 6]
# print(random.choice(lst))  # 从列表中选择
# print(random.choices(lst, k=2))  # 从列表中选择两个
# print(random.sample(lst, k=2))  # 不会重复
#
# random.shuffle(lst)  # 洗牌
# print(lst)
#
# print(random.randrange(0, 100, 2))
# # 验证场景 验证码
# # 4位
# # 字母 数字
# # char()
#
# lst = [str(i) for i in range(10)]  # 数字
# lst2 = [chr(i) for i in range(65, 91)]
# lst3 = [chr(i) for i in range(97, 123)]
#
# lst4 = lst + lst2 + lst3
# print(lst4)
#
# print(random.sample(lst4, k=4))
# lst5 = "".join(random.sample(lst4, k=4))
# print(lst5)
#
# # join 将列表转换为字符串 且join 不支持数字
# # split 将字符串转换成列表
# # 使用以上验证码不分大小写验证
#
# msg = input("请输入验证码")
# if lst5.upper() == msg.upper():
#     print("ok")


# json 是一种专门的数据类型 是跟字典一模一样
#
# 序列化 将一些特殊的数据(字典,列表)转换成字符串
# 反序列化 将字符串装换成一些特殊的数据
# json pickle
# 两组
# 一组 dump load
# 二组 dumps loads

# # dic = {}  # 复杂繁琐
# s = '{"alex":"alexdas"}'
# new_s = s.strip("{}").replace('"', "")
# k, v = new_s.split(":")
# dic[k] = v
# print(dic,type(dic))

# import json
#
# new_dic = json.loads(s)
# print(new_dic)
# dic = {"key": 1}
# s = json.dumps(dic)
# print(repr(s))
#
# new_dic = json.loads(s)
# print(new_dic["key"])
#
# dic = {"宝元": "gaoyao"}
# s = json.dumps(dic, ensure_ascii=False)
# print(s)
#
# s = "{'key':'2'}"  # 不可 因为不满足序列化格式

# dic = {"key": 1}
# f = open("jb", "a", encoding="utf-8")
# json.dump(dic,f)
# f = open("jb", "r", encoding="utf-8")
# dic = json.load(f)
# print(dic)

# dic = {"key": 1}
# f = open("jd", "a", encoding="utf-8")
# f.write(json.dumps(dic) + "\n")
# f = open("jd", "r", encoding="utf-8")
# for i in f:
#     print(json.loads(i))

# pickle 是python独有的

# import pickle
#
#
# def func():
#     print(1)
#
#
# s = pickle.dumps(func)
# print(s)
#
# funcll = pickle.loads(s)
# funcll()
#
# if __name__ == "__main__":
#     print("hello")


# os 通过程序与操作系统做交互的

import os

# 四个维度
# 文件夹
# os.makedirs("a/b/c/d")  # 创建多个文件夹
# os.removedirs("a/b/c/d")  # 移除多个文件夹
# os.mkdir("a")  # 生成一个文件夹
# os.rmdir("a")  # 删除一文件夹
print(os.listdir("C:/Users/Gei/Desktop/MyPythonLearn/日常学习/"))

# 文件
# os.rename()  # 重命名
# os.remove()  # 删除文件 删除后不能恢复
# # 路径
# print(os.getcwd())  # 获取当前工作路径
# os.chdir()  # 切换路径
# print(os.path.abspath("tb"))  # 返回绝对路径

# print(os.path.split())  #  切割
# os.path.dirname()  # 返回一层
# os.path.basename()  # 拿到文件名
# os.path.join("")  # 路径连接
# os.path.exists("E:/aaa")  # 返回布尔值 判断路径是否存在
# print(os.path.getsize())  # 获取文件大小 字节
# print(os.path.isabs())  # 判断是否为绝对路径
# print(os.path.isdir())  # 判断是否为文件夹 isfile 文件

# os.system()  # 通过python 向当前的终端发出指令
# os.popen()  # 方法用于从一个命令打开一个管道。
# 其他


# sys 与 结束器做交互
import sys

# sys.path 模块导入的顺序列表
print(sys.path)

s = sys.argv  # 写脚本的人使用的
print(s)

# sys.modules  # 以加载的模块
# print(sys.version)  # 版本
# 软件
print(sys.platform)  # win32 darwin

try:
    print()
except Exception:
    sys.exit(1)

# sys.exit(0) 退出代码

# hashlib 加密

# md5 sha1 sha256 sha512

# 密码为明文不安全

# 加密步骤 铭文--> 字节 --> 密文
# 密文是不可逆的 不能破解
# 明文如果是一致的 密文也是一致的

# 用户注册
# alex
# 字节 密文 储存
# 登录
# 字节 密文 读取 校验
# user = "alex"
# pwd = "alex123"
# import hashlib
#
# s = hashlib.md5(user.encode("utf-8"))  # 初识化一个加密模板
# s.update(pwd.encode("utf-8"))
# m = s.hexdigest()  # 加密
# print(m)
# f = open("userinfo", "r", encoding="utf-8")
# # f.write(f"{user}:{m}\n")
# for i in f:
#     user_file, pwd = i.strip().split(":")
#     if user_file == user and pwd == m:
#         print("ok")

# 注册
# import hashlib
#
#
# def register():
#     user = input("user")
#     pwd = input("pwd")
#     s = hashlib.md5(user.encode("utf-8"))
#     s.update(pwd.encode("utf-8"))
#     m = s.hexdigest()
#     with open("userinfo", "a", encoding="utf-8") as f:
#         f.write(f"{user}:{m}\n")
#
#
# def login():
#     print("选择登录")
#     user = input("user")
#     pwd = input("pwd")
#     s = hashlib.md5(user.encode("utf-8"))
#     s.update(pwd.encode("utf-8"))
#     m = s.hexdigest()
#     with open("userinfo", "r", encoding="utf-8") as f:
#
#         for i in f:
#             file_user, file_pwd = i.strip().split(":")
#             if file_pwd == m and file_user == user:
#                 print("ok")
#                 break
#             else:
#                 print("no")
#                 break
#
#
# msg = """
#  1.注册
#  2.登录
#  """
# func_dic = {
#     "1": register,
#     "2": login
# }
# choose = input(msg)
# if choose in func_dic:
#     func_dic[choose]()
# else:
#     print("error")

# collections : 额外的数据类型
# ordereddict -- 有序字典
# deque 双端队列

from collections import OrderedDict, deque, Counter, namedtuple

lst = deque([1, 2, 3, 4, 5])

print(lst)
lst.append(5)
lst.appendleft(7)

lst.pop()
lst.popleft()

# Counter 计数器
lst = [1, 2, 3, 4, 5, 6, 1, 6, 11, 1, 1]
dic = {}
for i in lst:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
print(dic)
print(dict(Counter(lst)))

# 命名元组
test = namedtuple("test", ["x", "y"])
p = test(10, 20)
print(p)
print(test.x) # 函数伪装