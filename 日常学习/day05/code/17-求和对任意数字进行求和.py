def my_sum(*args, **kwargs):
    num = 0
    for i in args:
        num += i

    for j in kwargs.values():
        num += j

    return num


print(my_sum())
print(my_sum(1))
print(my_sum(1, a=2))
