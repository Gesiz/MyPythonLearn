#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project:MyPythonLearn
# Product:PyCharm
# User:Gei
# Author: Gesiz
# Createtime: 2020/9/5 11:10

# 列表是一个容器
# 列表是可变数据类型
# 列表学习 所有元素以逗号分隔
# 列表可存储大量数据 储存不同数据类型

import random


def randomList(n):
    iList = []
    for i in range(n):
        iList.append(random.randrange(1000))
    print(iList)
    return iList


lst = ["钥匙", "电脑", "背包", "鞋子"]
print(lst)

# 末尾追加
lst.append("水杯")
# 选择位置插入
lst.insert(1, "书本")

# 迭代添加
lst.extend("abc")

# 弹出 列表最后一个 返回弹出内容 可通过索引
poplst = lst.pop()

# 移除 通过元素名删除 只删除第一个查找到的
lst.remove("鞋子")
print(f"{lst}")

# 清除变量
# del lst
# 通过索引 删除
del lst[0]
# 通过切片删除
del lst[0:2]

# 清空但是不影响
lst.clear()

# 改 通过列表索引
lst = ["key", "com", "shoe", "He"]
# lst[0] = "mine_key"
# print(lst)
#
# lst[0:2] = "你好"
# 默认步长为1 不唯一需一一对应
lst[0:3:2] = "你", 2
lst[0:3:2] = "你2"
print(lst)

# 元组可以迭代 ("","","")

# 索引
# for 循环

# 列表的其他操作

lst = randomList(10)
lst.sort()  # 正序排列 根据ASCII码(ord)排 不可混合排序
print(lst)
lst.reverse()  # 颠倒列表 lst[::-1]
print(lst)

lst.count("123")  # 计数
# lst.index("123")  # 查找第一个角标


# 列表的嵌套

nike = [["idCard", "Card", "money", "yuan", "key"],
        ["aa", "bb", "cc", "dd", "ee", "ff"],
        ["gg", "hh"],
        ["shoe", "dress"],
        "雨伞", "纸巾"
        ]

print(nike[1].index("cc"))

# coding:utf-8
# list -- 列表 --可变的
# tuple -- 元组 --不可变的

tuple = (2, 3, 4, 5, 6)  # 元组的作用就是保护数据的安全性
print(list(tuple))
# ip_port("192.168.1.1", 8000) -- 配置文件经常出现
# 可查询 索引 for

# 元组不可单一覆盖
money = (100,)
print(money[0])

tuple.index(2)
tuple.count(2)

# 支持嵌套且支持索引
tu = (100)  # 小括号为数据本身
tu1 = ("100",)  # 元组
tu2 = ()  # 元组

# range 范围
r1 = range(1, 5)
print(list(r1))

# 50 ~ 1 所有的奇数
for i in range(49, 0, -2):
    print(i)

# 字典 键值对数据 dict 无序
# [] -- list 中
# () -- tuple 小
# {} -- dict 大
# list 不可做 hash 可哈希的数据类型不可变 不可 哈希的数据类型是可变的

dic = {"key": "value",
       1: 10,
       }

print(dic)

# 字典的键 不可变数据类型 保证唯一性
# 字典的值 任意
# 字典的查询速度比列表快 存储的数量比 列表大

# 字典本身是可变的 本身也是一个容器

iphone = {
    "徐乐": "华为",
    "张荣": "小米手机",
    "王元": "华为手机",
    "左小龙": "华为",
    "牛存果": "华为"
}
# print(iphone[1])
print(iphone["王元"])
iphone["母建军"] = "华为001"  # 暴力增加 会强制覆盖
print(iphone)

iphone.setdefault("王元", "诺基亚")  # 试探增加 若存在则不增加
# 先查看键是否在字典中存在
# 若不存在就进行添加 否则就不添加
# 存在返回值 若不存在则返回None
print(iphone.setdefault("王元"))  # 若为None 则可以覆盖
print(iphone.setdefault("王云", [1, 2]))
print(iphone)

iphone = {
    "徐乐": "华为",
    "张荣": "小米手机",
    "王元": "华为手机",
    "左小龙": "华为",
    "牛存果": "华为",
    1: 10
}
print(iphone)
iphone.pop("徐乐")  # 删除
print(iphone)

iphone.popitem()  # 随机删除任何一个 python 默认删除最后一个
iphone.clear()  # 清空字典

# # del iphone  #  整个字典
# del iphone["张荣"]
# print(iphone)
#
# # 修改
# iphone["左小龙"] = "小米"
# iphone.update({"key": 1, 1: 20})  # 合并有相同的键会直接替换成 update 的值:
# print(iphone)

iphone = {
    "徐乐": "华为",
    "张荣": "小米手机",
    "王元": "华为手机",
    "左小龙": "华为",
    "牛存果": "华为",

}
print(iphone)
# 查询
print(iphone["徐乐"])
print(iphone.get("徐乐", 0))
print(iphone.get("关乐", 0))

print(iphone.setdefault("关", "啊"))

# 获取字典中所有的键
lst = iphone.keys()
print(lst)

for i in lst:
    print(i)
# 获取字典中所有的值
lst1 = iphone.values()
print(lst1)

# 获取字典中所有的键值对
lst2 = iphone.items()
print(lst2)
print("11111111111111111111111")
tu1, tu2 = (10, 20)
print(tu1)

tu1, tu2, tu3 = [10, 20, 30]

tu1, tu2, tu3 = "101"
print(tu1, tu2, tu3)

a = 10
b = 20
a, b = b, a

tu1, tu2 = {"key": 1, 1: 2}
print(tu1, tu2)

print(iphone.items())
print(iphone.items())
for k, v in iphone.items():
    print(k, v)

i = j = k = 10
print(i, k, j)

#
# lst = [1, 2, 3, 2]
# print(lst.count(2))
# dic.clear()
# for i in lst:
#     print(i, lst.count(i))
#     dic[i] = lst.count(i)
# print(dic)
#
# dic = {
#     "010": "北京",
#     "020": "天津",
#     "030": "河北"
# }
# new_dic = {}
# lst = ["010-8812312", "010-11123213", "020-112311213"]
# for i in lst:
#     key = i[0:3]
#     print(dic.get(key))
#     new_dic_key = dic.get(key)
#     new_dic[new_dic_key] = new_dic.get(new_dic_key, 0) + 1
# print(new_dic)

# 数据类型嵌套

"""
dic = {}
list = []
tuple = ()
str = "abc"
int = 123
bool = True
"""

dic = {
    101: {
        1: {"刘亦菲":
                {"中国": ["天龙八部", "神雕侠侣", "四大名捕", "仙剑奇侠"],
                 "美国": ["花木兰", "功夫之王"]
                 }
            },
        2: {"皮裤男": {"汪峰": ["春天里", "北京北京", "恒心"]}
            },
        3: {"皮裤女": {"邓紫棋": ["泡沫", "你不是真正的快乐", "我要我们在一起", "再见", "黑风雷"]}
            }
    },
    102: {
        1: {1: {"蔡徐坤": ["唱", "跳", "rap", "篮球", "姬霓太美"]},
            2: {"鹿晗": [100, "上海堡垒", "重返二十岁", "跑男", ""]}
            },
        2: {True: [1, "", -1],
            False: [0, "", 1]
            }
    },
    103: {
        1: {"倚天屠龙记": [{
            "张无忌": ["乾坤大挪移", "小昭", "周正若", "赵敏", "杨不悔", "啊高", "灭绝师太"],
            "谢逊": ["屠龙宝刀"],
            "杨逍": ["光明左使"]}
        ]},
        2: {

        }
    }
}


# 整形 python3 中全都是int
# python2 中分为 int long
# 字符 存储少量数据 数据类型单一 不能再原内存地址进行修改 索引从 从左向右
# 切片 起始位置 终止位置 顾头不顾腚 查出范围不会报错
# 步长 起始位置 终止位置 步长 步长作用一 绝对查找时 的步子 和方向
# 字符串的方法
# 修改 upper 全部大写 lower 全部小写 replace （old，new）
# format 格式化 按照位置 按照索引 按照关键字
# 操作 count 统计出现次数 split 分割 默认以空格换行符 制表符 可以自己制定
# strip 去除头尾两端的空格 换行 制表符 可以自己指定
# 判断 startwith 判断以什么开头
# 判断 endwith 判断以什么结尾
# isalnum 判断中文 和 英文 数字
# isalpha 判断中文 英文
# isdigist 判断数字
# isdecimal 判断十进制
# 查找 find 差找不到时返回-1
# for 循环 可迭代对象 int bool 不可 pass



# 列表 存储大量数据 存储不同数据类型 可变 有序
# list 增 append insert
# 删除 pop 默认删除最后一个 可以通过索引删除 具有返回值
# del list[索引]
# 该 list[索引] = "值"
# 查 for 循环 索引
# 其他操作 sort 排序 升序
# sort(reverse = true) 降序
# reverse 反转
# 列表嵌套 一层一层查找
# 元组 是一个不可变的数据类型
# 支持索引 for 循环 不可变(10)，(10,),()
# range 范围 能够循环数字 range(起始位置,终止位置,步长) 如果不写起始位置 默认为0
# 字典 存储大量数据 可变 无序 键值对数据 查找快 使用字典 可以让数据和数据缠身关联
# 字典的键 不可变数据 可HASH 可哈希 保证唯一
# 字典的值 任意
# 增 字典【键】 = 值
# 删除 字典.pop【键位】
# 改 字典【键】 = 值
# 查 字典。get（键）
# 其他操作 keys values items键值对
# 数据类型的转换


