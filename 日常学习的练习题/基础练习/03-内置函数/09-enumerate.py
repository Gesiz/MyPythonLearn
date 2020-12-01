# enumerate() 函数用于将一个可遍历的数据对象 如列表 元组 或字符串
# 组合为一个索引序列 同时列出数据和数据下标 一般用在for循环当中
# 下面是使用示例

def my_enumerate(lst):
    for i in range(len(lst)):
        yield i, lst[i]


for index, item in my_enumerate([1, 2, 3, 4, 5, 6]):
    print(index, item)

if []:
    print(111)
else:
    print(222)
