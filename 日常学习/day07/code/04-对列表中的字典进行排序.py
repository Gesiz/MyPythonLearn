# 补充对列表中的字典排序
list1 = [
    {'name': 'c', "age": 12},
    {'name': 'd', "age": 18},
    {'name': 'a', "age": 16},
    {'name': 'b', "age": 14},
    {'name': 'f', "age": 10}
]
list1.sort(key=lambda x: x["age"])

# sort 方法  默认是将列表中数据 按照 比大小进行排序 如果说列表中的内容是字典 在python 中没有指定字典如何比较大小 所以报错
# 解决方案 我们需要告诉列表他的排序方式
# 列表 .sort(key,reverse)
# key 参数 必须传递一个函数 函数还必须有一个形参 形参是列表中的数据

list1.sort(key=lambda x: x["age"])  # 按照年龄排序
list1.sort(key=lambda x: x["age"], reverse=True)  # 按照年龄排序
list1.sort(key=lambda x: x["name"])  # 按照年龄排序
list1.sort(key=lambda x: x["name"], reverse=True)  # 按照年龄排序
print(list1)


