# 字符串内置方法联系
# 1将字符串"abcd"转成大写
print("abcd".upper())
# 2计算字符串"cd" 在字符串abcd中出现的位置
print("abcd".find("cd"))
# 3 字符串 a,b,c,d 请用都好分割字符串 分割后的结果是什么类型的?
print(type("a,b,c,d".split(",")))  # 列表
# 4 "{name}喜欢{fruit}".format(name="李雷") 执行会出错 请修改代码让其正确执行
print("{name}喜欢{fruit}".format(name="李雷", fruit="苹果"))
# 5 string = "Python is good" 请将字符串里的Python 替换成python 并输出替换后的结果
string = "Python is good"
print(string.replace("Python", "python"))
# 6 有一个字符串 string = "python修炼第一期.html"，请写程序从这个字符串里获得.html前面的部分 要用尽可能多的方式来做这个事情
string = "python修炼第一期.html"
print(string.split(".")[0])
# 7 如何获取字符串的长度？
print(len("hello world"))
# 8 "this is a book", 请将字符串里的book替换成apple
print("this is a book".replace("book", "apple"))
# 9. "this is a book", 请用程序判断该字符串是否以this开头
# print("this is a book".title("this"))
print("this is a book".find("this"))
print("this is a book".startswith("this"))
# 10. "this is a book", 请用程序判断该字符串是否以apple结尾
print("this is a book".find("apple") == ("this is a book"[-4:]) == "apple")
print("this is a book".endswith("apple"))

# 11. "This IS a book", 请将字符串里的大写字符转换成小写字符
print("This IS a book".lower())
# 12. "This IS a book", 请将字符串里的小写字符 转成大写字符
print("This IS a book".upper())
# 13. "this is a book\n", 字符串的末尾有一个回车符,请将其删除
print("this is a book\n".strip("\n"), end="")
"this is a book".capitalize()