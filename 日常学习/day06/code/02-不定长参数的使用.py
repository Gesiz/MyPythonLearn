# coding:"utf-8"

def func(*args, **kwargs):
    print(args)
    print(kwargs)


my_list = [1, 2, 3, 4, 5]
my_dict = {'name': 'xw', 'age': 18, 'gender': '男'}
# 需求 将类表中的元素按照位置传参的方式传递给args --》 对函数调用的时候 对列表（元组）进行拆包 *变量
# 将字典中的数据按照关键字传参的方式传递给kwargs

# 将字典中的数据按照关键字传参的方式传递给kwargs --> 函数调用的时候对字典进行拆包 **变量

# 若不加星的时候将会将 容器数据整体封装到元组中进行传递
func(*my_list)  # 将列表进行拆包 分别将列表中的数据传递给args
# 若字典仅仅使用一个型号的话 会将字典中的key 封装到元组中传递过去
func(**my_dict)  # 将字典中的键值对作为一组数据传递给kwargs

