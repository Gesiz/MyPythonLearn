# 递归函数
# 属于自己调用自己
# 函数必须有一个终止tiaojian

# 已知 A 比 B大两岁 B 比 C 大两岁....F 18 岁
# 求

# def getAge(n):
#     if n == 1:
#         return 18
#     return getAge(n - 1) + 2
#
#
# if __name__ == "__main__":
#     print(getAge(3))

# 阶乘
def func(n):
    if n == 1:
        return 1
    return func(n - 1) * n


if __name__ == "__main__":
    print(func(5))
