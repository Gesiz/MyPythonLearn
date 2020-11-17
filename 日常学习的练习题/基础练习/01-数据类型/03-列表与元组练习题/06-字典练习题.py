# 字典的基本操作

dic = {
    'python': 95,
    'java': 99,
    'c': 100
}

# 1. 字典的长度是多少
print(len(dic))
# 2. 请修改'java'这个key对应的value值为98
dic["java"] = 98
print(dic)
# 3. 删除c这个key
dic.pop("c")  # del dic['c']
print(dic)
# 4. 增加一个key-value对 存储在列表里
dic["http"] = 99
# 5. 获取所有key值 存储在列表里
print(dic.keys())
# 6. 获取所有的value值 存储在列表里
print(dic.values())
# 7. 判断javascript 是否在字典中
if 'javascript' in dic:
    print("存在")
else:
    print("不存在")
# 8. 获取字典里所有value的和
print(sum(dic.values()))
# 9. 获取字典里最大的value
print(max(dic.values()))
# 10. 获取字典里最小的value
print(min(dic.values()))
# 11 字典dic1 = {'php':97} 将dic1的数据更新到dic中
dic.update({'php': 99})
print(dic)
