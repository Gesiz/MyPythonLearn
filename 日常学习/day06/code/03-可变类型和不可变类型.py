# 在不改变变量引用的前提下 看能否修改内存中存储的内容
# 能修改就是可变的 不能修改就是不可变类型

# 只有赋值运算符才可以改变变脸的引用
# 可变类型 列表 字典
# 不可变数据类型 int float bool str tuple

# 想要改变不可变类型的数据值 引用一定会发生变化

# 可变类型
my_list = [1, 2]
print(my_list, id(my_list))
my_list.append(3)
print(my_list, id(my_list))



