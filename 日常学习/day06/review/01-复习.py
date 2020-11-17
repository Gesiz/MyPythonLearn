# 定义全局变量

g_num = 100

def func():
    global g_num
    print(g_num)  # 若使用时没有先global 使用全局变量在进行 global 操作后进行修改全局变量会导致 报错
    g_num = 100

func()  # 全局变量在函数内使用时最好显示用global修饰

# 字符串拆包时需要一一对应
# a,b = 'he'  a h b e
# a,b = 'hel'  # 报错
# a,b,c = 'he'  # 报错

# 字典拆包的时候拆的是一个key值


# 数据优化是对 不可变数据的优化 https://cnblogs.com/guobaoyuan/p/9833517.html
# 数据驻留 内存优化

# import keyword   # 导入工具包
#
# print(keyword.kwlist)

# sum(可迭代序列)  # 求和 列表 元组 必须是 数字类型
result = sum([1,2,3,4])
print(result)