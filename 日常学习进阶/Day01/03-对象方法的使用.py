# 定义一个Person类
class Person:
    # 属性
    # 方法(对象方法)
    def eat(self):  # 他是一个形参 叫什么名字都可以 一般我们就是叫做self
        print(type(self))
        print("火锅")


# 第一种方法的调用
# 通过对象来调用对象方法

p1 = Person()

p1.eat()

# 说明
# self 指的是调用这个方法的对象本身
# 当使用对象第哦啊用对象方法的时候 系统会自动把
# 这个对象以slef传入到方法内

# 第二种 方法的调用(一般不这样使用)
# 通过类名来调用对象方法
Person.eat(p1)
# 说明 使用类名ing调用对象的方法的时候 需要手动传入slef参数



