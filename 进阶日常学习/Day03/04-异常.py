# 异常 Day3
# 异常python 解释器再执行代码的时候抛出的错误信息

# 特点
# 显示错误的原因 错误的位置
# 组织代码继续向下执行
# 异常的组成
# Traceback
# 错误的来源 可以通过这个信息定位错误的位置 以及调用这些方法 或者函数的流程
# 错误的类型及描述信息
# 错误类型  和这个类型的实例描述

# 捕获单个异常
# 语法
try:
    open('hello.py', 'r')
except FileNotFoundError:
    Exception("nothing")
# TODO 常见的异常

print("要执行的代码1")
# open('hello.py', 'r')  # FileNotFoundError
print("要执行的代码2")
