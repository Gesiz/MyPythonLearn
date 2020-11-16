print(1)
print(1, 2)
print(1, 2, 3)


# 不定长参数 有两种
# 1 *arg 不定长位置实参 元组参数
# 2 **kwarg 不定长关键字实参 字典参数

# 想要将一个普通参数变为不定长位置参数  只需要在这个形参的前面边上加一个*前缀即可 可以接受所有的位置实参
# 一般来说 定义不定长位置参数 变量名为 args 即写作 **kwargs
def func(*num):
    print(num)  # num是元组类型 接收所有的位置实参


func()
func(1, 2)
func(1, 2, 3)


# 想要将一个普通的形参 变为不定长的关键字参数 加两个*就可以
# 一般来说 定义不定长关键字参数 变量名为 kwargs 机械做 **kwargs

def func(**num):
    print(num)

func()
func(a=1, b=2)
func(a=1, b=2, c=3)

