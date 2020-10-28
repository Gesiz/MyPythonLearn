#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project:MyPythonLearn
# Product:PyCharm
# User:Gei
# Author: Gesiz
# Createtime: 2020/9/6 10:28

"""
li = ["alex", "wusir", "meet"]
利用下划线将列表的每一个元素拼接成字符串"alex_wusir_meet"
"""

# li = ["alex", "wusir", "meet"]
# lis = ""
# for i in range(0, len(li)):
#     if i == len(li) - 1:
#         lis = lis + li[i]
#     else:
#         lis = lis + li[i] + "_"
# print(lis)

# s = ""  # alex_wusir_meet_
# li = ["alex", "wusir", "meet"]
# for i in li:
#     s = s + i + "_"
# print(s.strip('_'))
# print(s[:-1])

"""
查找列表li中的元素，移除每个元素的空格，
并找出以"A"或者"a"开头，并以"c"结尾的所有元素，
并添加到一个新列表中,最后循环打印这个新列表。
"""

li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", " aqc"]
new_li = []
for i in range(0, len(li)):
    li[i] = li[i].strip()
    if li[i][0:1] in ["A", "a"] or li[i][-1:-2] in ["c"]:
        new_li.append(li[i])
print(new_li)

for i in li:
    new_i = i.replace(" ", "")

# for i in li:
#     new_i = i.replace(" ","")
#     if new_i.startswith("A") and new_i.endswith("c") or new_i.startswith("a") and new_i.endswith("c"):
#         print(new_i)

# for i in li:
#     new_i = i.replace(" ","")
#     if (new_i.startswith("A") or new_i.startswith("a")) and new_i.endswith("c"):
#         print(new_i)

# 有如下字典,请按照一下的需求对字典进行操作(20分钟)
av_catalog = {
    "欧美": {
        "www.宝元.com": ["很多免费的,世界最大的", "质量一般"],
        "www.alex.com": ["很多免费的,也很大", "质量挺好"],
        "oldboy.com": ["多是自拍,高质量图片很多", "资源不多,更新慢"],
        "hao222.com": ["质量很高,真的很高", "全部收费,屌丝请绕过"]
    },
    "日韩": {
        "tokyo-hot": ["质量怎样不清楚,个人已经不喜欢日韩范了", "verygood"]
    },
    "大陆": {
        "1024": ["全部免费,真好,好人一生平安", "服务器在国外,慢"]
    }
}
# a.给此 ["很多免费的,世界最大的","质量一般"]列表第二个位置插入一个 元素：'量很大'。
# b.将此 ["质量很高,真的很高","全部收费,屌丝请绕过"]列表的 "全部收费,屌丝请绕过" 删除。
# c.将此["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]列表的 "verygood"全部变成大写。
# d.给 '大陆' 对应的字典添加一个键值对 '1048' :['一天就封了']
# e.删除这个键值对："oldboy.com": ["多是自拍,高质量图片很多","资源不多,更新慢"]
# f.给此["全部免费,真好,好人一生平安","服务器在国外,慢"]列表的第一个元素对应的字符串，加上一句话：'可以爬下来'
print(av_catalog["欧美"]["www.宝元.com"].insert(1, "量很大"))
print(av_catalog["欧美"]["www.宝元.com"])
av_catalog["欧美"]["hao222.com"].remove("全部收费,屌丝请绕过")
print(av_catalog["欧美"]["hao222.com"])
av_catalog["欧美"].pop("oldboy.com")
print(av_catalog)


li = ["苍老师", "东京热", "武藤兰", "菠萝野结业"]
msg = input("请输入您的审批词汇")
for i in li:
    if i in msg:
        msg = msg.replace(i, len(i) * "*")
print(msg)

