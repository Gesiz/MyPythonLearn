# 可变类型作为参数 会直接修改可变类型的内部数据
def func(num):
    num += num  # 对于不可变数据类型 对于列表来说 += 其实执行的是 列表.extend()方法 即不会改变引用值
    print('函数内部:', num)


a = 1
func(a)
print('函数外部a', a)

my_list = [1, 2]
func(my_list)
print("函数外部my_list", my_list)
# 总结 列表作为参数 如果不改变形参的应用 执行其他的操作 远离恶的数据也是随着该笔那 += ======= extend()

# 可变类型做参数 之哟啊不改变 形参的引用 执行其他的操作 其他的数据也会改变
