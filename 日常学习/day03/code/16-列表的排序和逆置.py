# 想要对列表进行排序,需要保证列表中的数据的数据类型是一样的
my_list = [1, 4, 7, 2, 5, 8, 3, 6, 9]

# 排序, 列表.sort()  直接在原列表中进行排序,返回None
# my_list.sort()  # 默认是升序,从小到大的
my_list.sort(reverse=True)   # 降序排序
print(my_list)

my_list = [1, 4, 7]
# 逆置  [7, 4, 1]
my_list.reverse()  # 直接在原列表中进行操作,返回 None
print(my_list)

# 使用切片进行逆置, 不会改变原数据,生成一个新的列表
my_list1 = my_list[::-1]
print(my_list)
print(my_list1)


