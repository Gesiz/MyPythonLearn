# 自定义异常
# 说明 由于系统的异常类不能满足开发需求 我们可以自定义异常
"""
1. 定义一个类继承自Exception
2. 一般会实现一个__str__魔术方法 用与打印出异常描述信息
"""

"""
需求
input('要求输入一个整形')
当接收道德数据是一个非整形字符串时 抛出自定义的这个异常
"""


# class InputNoNumberError(Exception):
#     # 优化自定义异常类 补充异常描述信息
#
#     def __str__(self):
#         return "value is not number"

class InputNoNumberError(Exception):
    # 继续优化自定义异常类 补充异常描述信息
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return f"{self.num} is not number"


def user_input():
    num = input("请输入一个整数")
    try:
        if not num.isdigit():
            raise InputNoNumberError(num)
    except Exception as e:
        print(e)

class MyError(InputNoNumberError):
    pass

user_input()
print(type('123'))
