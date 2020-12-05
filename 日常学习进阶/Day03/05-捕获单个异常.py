# 捕获单个异常的语法


print("要执行的代码1")
try:
    open('hello.py', 'r')
except FileNotFoundError:
    print("捕获到异常执行的代码")

print("要执行的代码2")
