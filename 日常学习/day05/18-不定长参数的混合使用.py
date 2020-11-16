# 普通参数 不定长位置 缺省 不定长关键字 最合适的写法
# 普通参数 缺省 不定长位置 不定长关键字 语法不会报错 但不建议使用

def func(name, age=18, *args, **kwargs):  # 无法使用缺省值
    print(f'name:{name},age:{age},args:{args},kwargs:{kwargs}')


func("kw", 12, 1, 2, a=3, b=4)  # 给缺省参数传递实参值
func("kw", 1, 2, a=3, b=4)  # 想要使用缺省参数的默认值


def func(name, *args, age=18, **kwargs):  # 可以使用缺省值
    print(f'name:{name},age:{age},args:{args},kwargs:{kwargs}')


func("kw", 12, 1, 2, a=3, b=4)  # 给缺省参数传递实参值
func("kw", 1, 2, a=3, b=4)  # 想要使用缺省参数的默认值 使用关键字传参给缺省参数 传递实参值
