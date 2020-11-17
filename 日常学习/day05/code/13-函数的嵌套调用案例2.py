# 写一个函数求三个数的和
def my_sum(a, b, c):
    return a + b + c


# 写一个函数求三个数的平均值
def my_avg(a, b, c):
    return my_sum(a, b, c) / 3


result = my_sum(1, 2, 3)
result1 = my_avg(1, 2, 3)
print(result1)
