import sys


def func(num, my_list=[]):  # my_list默认参数 是可变类型 就相当于是全局变量 不会随着函数的结束
    my_list.append(num)
    print(my_list)
    print(sys.getrefcount(my_list))
    print(object.__dict__)
    del my_list
    print(object.__dict__)
    print(my_list)



func(1)
func(2)

