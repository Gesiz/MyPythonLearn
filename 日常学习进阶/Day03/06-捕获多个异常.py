# # 捕获多个异常
# try:
#     可能发生异常的代码
# except（异常类型,异常类型2,....）:
#     捕获到异常的反馈
#
# # 第二种方式
# try:
#     可能发生异常的代码
# except 异常类型1:
#     ...
# except 异常雷星2:
#     ...
#
import random

try:
    zero_or_one = random.randint(0, 1)
    print(zero_or_one)
    num = 100 / zero_or_one
    open('FileNotFoundError')
except (FileNotFoundError, ZeroDivisionError, NameError):
    print("捕获到异常执行的代码")

import random

try:
    zero_or_one = random.randint(0, 1)
    print(zero_or_one)
    num = 100 / zero_or_one
    open('FileNotFoundError')
except FileNotFoundError:
    print("捕获到异常执行的代码1")
except ZeroDivisionError:
    print("捕获到异常执行的代码2")
except NameError:
    print("捕获到异常执行的代码3")
else:
    print("其他异常")



