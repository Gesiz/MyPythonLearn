# 类表推导式 轻量级循环创建列表(快速的创建有规律的列表)
import random

# 方式一 [生成数据的规则 for 临时比那辆 in 可迭代序列]
# 每循环一次,就会按照规则向列表中添加一个数据
my_list = [i for i in range(5)]
my_lista = [i for i in [1231, 2, 31, 213]]
print(my_lista)

my_list2 = ["hello" for i in range(5)]
my_list3 = [f"hello{i}" for i in range(5)]
my_list3 = [random.randint(0, 100) for i in range(5)]

print(my_list)
print(my_list2)
print(my_list3)

# 方式二 [生成数据的规则 for 临时变量 in 可迭代序列 if 判断条件]
# 当条件为True时 按照规则向列表添加一个数据

my_list4 = [i for i in range(10) if i % 2]
print(my_list4)

# 方式三 [生成数据的规则 for 临时变量  in 可迭代序列 for 临时变量 in 可迭代序列]
# 第二个 for 循环每循环一次 就添加一个数据
my_list5 = [i + j for i in range(2) for j in range(3)]
my_list6 = [(i, j) for i in range(2) for j in range(3)]
my_list7 = [{i, j} for i in range(2) for j in range(3)]
print(my_list5)
print(my_list6)
print(my_list7)

# 思考练习
# 请写出一段python代码 实现分组一个list里面的元素 比如[1,2,3,4.....100]
# 变成[[1,2,3],[456]...]
a = [x for x in range(1, 101)]
b = [a[i:i + 3] for i in range(0, len(a), 3)]
print(b)

# 字典推导式{生成字典的一个规则 for  临时变量 in 可迭代对象}
my_dict = {f"key{i}": i for i in range(5)}
my_dict2 = {i: j for i in range(3) for j in range(2)}
print(my_dict2)
