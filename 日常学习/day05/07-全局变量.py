# 全局变量 在函数外部定义的变量是全局变量
# 在函数内部是否能使用全局变量
# 在函数内部能否修改全局变量
# 定义全局变量
num = 10


def func():
    # 函数内部是否能使用全局变量
    print(f"函数内部可以访问全局变量的值{num}")
    num = 100
    # 此时在函数内部使用的是局部变量的值
    print(f"函数不可直接修改num的值{num}")
    global num
    num = 100
    print(f"全局变量的值需要global之后才可以赋值")

def set_num_2():
    # 想要在函数内修改全局变量时需要在使用变量之前 需使用global关键字进行声明声明为全局变量
    global num
    num = 1999
    print(num)

set_num_2()