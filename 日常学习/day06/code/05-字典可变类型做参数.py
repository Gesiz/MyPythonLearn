def add_age(num):
    """num 需要是一个字典"""
    num['age'] = 18
    print("函数内部num:", num)


my_dict = {'name': 'xw'}
add_age(my_dict)
print("函数外部 my_dict", my_dict)

