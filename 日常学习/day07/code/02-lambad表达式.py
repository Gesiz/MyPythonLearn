# 1 匿名函数中 不能使用if语句 while循环 for循环 只能编写单行的表达式 或函数调用 普通函数都可以
# 2
# 3

# 无参数 无返回值
def func():
    print("hello")


func1 = lambda: print("hell lambda")
func1()
# 匿名函数在定义的同时直接调用(匿名函数的定义)(调用实参)
(lambda: print("hello lambda"))()


# 无参有返回值
def func2():
    return 'aaa'


print((lambda: 'aaa')())
# 有参无返回值
(lambda *args: print(args))(3.14)

# 有参数 有返回值
print((lambda a, b: a + b)(10, 20))
c = [1, 2, 3]
print(filter((lambda x: x > 4), c))
