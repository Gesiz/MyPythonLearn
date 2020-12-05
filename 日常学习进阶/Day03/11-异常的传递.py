# 第一种 try 里面嵌套 try
# 如果内层的tyr没有捕获到异常会传递到外层的try继续捕获 直到捕获到异常 或者抛出异常
"""
try:
    try:
        可能出现异常的代码
    except 捕获不到当前异常的类型:
except 可以捕获到当前异常的类型:
"""


# 第二种 函数异常的传递
def func():
    print(abc)  # 没有定义的变量


"""
def func2():
    try:
        func()
    except:
        捕获到异常的代码
func2()
"""

# 以下是第一种
# 内层try没有捕获到异常传到外层继续捕获
try:
    try:
        print(asd)
    except ZeroDivisionError:
        print("11")
except Exception as e:
    print(e)
