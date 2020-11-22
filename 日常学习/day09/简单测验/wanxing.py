# 1）.现有学员姓名的字符串names="张三,李四,王五,赵六,孙七,周八"，将字符串中的每个姓名做为key并获取随机数0-100（包含0和100）做为代表成绩的value，存入字典。
# 2）.遍历字典将成绩大于等于60的学员信息写入根目录下的data.txt文件，写入格式如下：
# 张三-82
# 王五-63
# 周八-66
import random

# 创建姓名字符串，存储学员姓名。
names = "张三,李四,王五,赵六,孙七,周八"

# 创建一个空的字典，用于存储学员姓名和成绩。
dict = {}
# 将姓名字符串按逗号切割获取到姓名列表，遍历列表将每个姓名做为key并获取随机数0-100（包含0和100）做为代表成绩的value，存入字典。
iStr = names.split(",")
for i, j in enumerate(iStr):
    dict[j] = random.randint(0, 101)

# 遍历字典，将字典中成绩大于等于60的学员信息写入根目录下的data.txt文件。
iDict = {}
for i, j in dict.items():
    if j >= 60:
        iDict[i] = j
with open(file="data.txt", mode="w", encoding="utf-8") as f:
    f.write(str(iDict))
