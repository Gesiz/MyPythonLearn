# coding:utf-8
# day1 字符串的 索引 切片 步长
# python3 只有int类型
# python2 有int和long  -2**31 ~ 2**31-1

# 索引
# 元素中的单独字母

s = "meet"
#    0123
#    -4-3-2-1
print(f"第二位 + {s[2]}")
print(f"第一位 + {s[-4]}")


# 练习题1
s = "alexdsb"
# 从左向右查找x
# 从右想左查找l

for i in range(0, len(s)):
    print(s[i])

# 切片
# print(s[起始位置:终止位置])

s = "今天是个好日子,今天星期五,明天不上班"
# 1. 从做导游或取代 日子啊 今天
# 2. 从右向左或取代 是个好日子啊
print("\n"+s)
print("s[5:11] " + s[5:11])
print("s[-19:-15] " + s[-19:-15])
print("s[-1:] " + s[-1] + "\n")

# 步长:默认为1
# print(s[起始位置:终止位置:步长大小])
print("\ns[0:5:2] " + s[0:5:2])
print("s[0:7:3] " + s[0:7:3] + "\n")
print(s)
print("\ns[-1:-10:-2] " + s[-1:-10:-2])
print("s[-1:3:-3] " + s[-1:3:-3] + "\n")

s = "abcdefg"
print(s[-1:3:-3])
print(s[::2])
print(s[0:2])
#
# name = "alex_dsb"
#
# # 1.请输出 name 变量对应的值的第二个字符
# # 2.请输出 name 变量对应的值的前三个字符
# # 3.请输出 name 变量对应的值的后两个字符
# # 你今天看着状态很不错 将这句话反转(通过步长)
# print(name[-2:-7])
# sentence = "你今天看着状态很不错"  # 倒序输出
# print(f"{sentence[-1:-len(sentence):-1]}")
# print(name[-2:])  # -2 到起始位置
#
# print(name[0:100])  # 切片时可以超出索引
# # print(name[8])  # 索引不可以超出范围
#
#
# # s = "你今天看着状态很不错啊"
# # print(s+"\n"+s[-1:-12:-1])
# # print(s[::-1])
# # print(s[:])
# # s = input("请输入")
# # print(s)
# # print(s[::-1])
# # if s == s[::-1]:
# #     print("是回文")
# # else:
# #     print("不是回文")
#
#
# name = "Alex"
# # 1.修改
#
# print(name.upper())  # 全部大写
# print(name.lower())  # 全部小写
#
# # 验证码:
#
# # msg = input("请输入验证码")
# # if msg.upper() == "J98K":
# #     print("OK")
# # else:
# #     print("NO")
#
# # 替换
# name = "alexnb"
# name1 = name.replace("n", "s")
# print(name1)
# # 敏感词替换
# # lst = ["TMD"]
# # msg = input("敏感词")
# # for i in lst:
# #     if i in msg:
# #         msg = msg.replace(i, len(i)*"*")
# # print(msg)
# # 2.操作
#
# name = "alex_meeteee"
# # name1 = name.count("e")  # 统计元素出现的次数
# name1 = name.strip("ae")  # 去除头尾两端的空格 换行符\n 制表符(Tab)\t 可指定字符
# print(name1)
#
#
# # split 分隔
#
#
# s = "alex_wusir_meet"
# slist = s.split("_")
# for i in slist:
#     print(i)
#
# # num = input("请输入数字：")
# # numList = num.split("+")
# # # print(numList)
# # # intNums = [int(x) for x in numList]  # 将列表中的str转换为int
# # # print(intNums)
# #
# # sum = 0
# #
# # for i in numList:
# #     sum += int(i)
# #
# # print(sum)
#
# # 3.判断
# name = "alex"
# print(name.startswith("1", 1, 3))
# print(name.endswith("a"))
# # is 系列  字母 数字
# s = ""
# print(s.isalnum())
# # 判断是否由字母 中文汉字
# print(s.isalpha())
#
# # 判断是否是阿拉伯数字
# s = "12341"
# print(s.isdigit())
#
# # 判断是否是十进制数
# print(s.isdecimal())
#
# name.istitle()
# name.isupper()
# name.islower()
#
# # 格式化 name = ""
# name = "{}:你好"
# name1 = name.format("元宝")  # 安装位置填充
# print(name1)
#
# name = "{0} {1} {2}"
# name1 = name.format("anna", "Dai", "Given")
# print(name1)   
#
# name = "{a} {b} {c}"
# name1 = name.format(a="anna", b="Dai", c="Given")
# print(name1)
#
# # 4. 查找 查询到最近的索引值
# name = "alexdsb"
# print(name.find("c"))
# print(name.find("a"))
#
# # 获取长度是公用方法 除了不能求数字的长度意外 其他数字类型都可以获取
# len("123123123")
# print(len(str(123123123)))
#
# s = "alexdsb"
# # for i in range(len(s)):
# #     print(s[i])
# # num = 0
# # while num < len(s):
# #     print(s[num])
# #     num += 1
# for i in s:
#     pass
#
# # 1.有变量 name = "aleX"

# while breake 终止当前循环
# continue 调出本次循环
# while else
# while 嵌套
# 格式化
# %s 占字符串位置 %d 占整形位置 %%转义百分号
# 运算符 算术运算符 比较运算符 逻辑运算符
# and 都为真 为真 选择 右边的内容
# or 一个为真就为真 为真选择左边的内容
# 优先级 ()>not>and>or
# 计算顺序 从左往右
# 成员计算 in 在 not in 不在
# 编码初识 ascii 不执行中文
# gbk国标 应为一个自付使用1字节8位
# 中文 一个字符 使用两个字节 16位
# unicode 万国码 英文和中文一个字符 使用四个字节 == 32位
# utf-8 英文一个字节 欧洲两个字节 亚洲三个字节
# 单位转换 1Bytes(字节) == 8bit(位)
# 1KB == 1024Bytes
# 进制转换 十进制转二进制 整除 码位
# 二进制转十进制 幂运算 码位
# 使用计算机进行进制转换 10 -- 2 bin
# 2 -- 10 int
