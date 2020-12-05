"""
try:
    可能出现的异常代码
except:
    捕获到执行所要执行的代码
"""

# 说明 except 后面什么都不写 捕获所有代码级别的异常类型
import random

zero_on_one = random.randint(0, 1)
try:
    num = 100 / zero_on_one
except:     # PEP8不建议使用
    print('捕获到异常')

