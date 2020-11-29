# 捕获多个异常

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
