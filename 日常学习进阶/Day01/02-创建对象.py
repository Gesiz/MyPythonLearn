# 创建对象
# 变量 = 类名()  # 创建了一个这个类的对象(实现)

# 定义一个Hero类
class Hero:
    pass


# 创建Hero的实例

h1 = Hero()
print(id(h1))
print(h1)
print(hex(id(h1)))
h2 = Hero()
print(id(h2))

# 总结:
# 一个类可以创建多个对象 每个对象系统都会开辟一个内存空间进行存储
