# 代码功能如下：
# 请编写程序，键盘录入1个字符串，之后将字符串中的”a”替换成”*”，
# 之后将替换后的字符串写入项目根目录下的text.txt文件中

# 定义一个空的字符串
str = ""
# 键盘录入1个字符串赋值给str，之后将str中的”a”替换成”*”

str = input("请输入字符串").replace("a", "*")

# 将替换后的字符串写入项目根目录下的text.txt文件中

with open(file="text.txt",mode="w",encoding="utf-8") as f:
    f.write(str)
