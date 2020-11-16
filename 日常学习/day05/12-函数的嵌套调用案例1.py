# 定义一个函数 打印一条横线
def print_line():
    print("_" * 30)


# 定义一个函数 打印任意行数的横线
def print_lines(num):
    for i in range(num):
        print_line()

print_lines(5)
