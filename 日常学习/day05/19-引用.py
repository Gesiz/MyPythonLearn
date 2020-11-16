# 引用 看作是数据值的一个内存地址 可以使用id这个函数 查看是否是同一个值的引用地址
# 只有赋值运算符可以改变变量引用值
a = 100  # 将100数据值的引用地址给了a变量
b = a  # 将a中存储的的数据值的引用地址给到了b
print(id(a))
print(id(b))
a = 2  # 将数据2的引用地址给a
# python 中数据值的传递 传递的是引用

my_list = [1, 2]
my1_list = my_list
print(id(my_list), id(my1_list))
my1_list[1] = 100
print(id(my_list), my_list, id(my1_list), my1_list)
my_list[1] = 200
print(id(my_list), my_list, id(my1_list), my1_list)

# 元组中的数据是不能被修改的
my_tuple = (1, 2, [3, 4])
print(my_tuple, id(my_tuple))
my_tuple[2][1] = 100
print(my_tuple, id(my_tuple))
