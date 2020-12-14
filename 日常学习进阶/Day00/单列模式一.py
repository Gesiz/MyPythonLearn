# 使用模块实现单列模式
# 单列模式时最常使用的一种设计模式 该模式的目的是确保在一个系统中 一个类 只有 一个实例
# 模块天然就是 单列的 因为模块只会被加载一次 加载之后 其他脚本里如果使用import 二次加载这个模块
# 会从 sys.modules 里找到已经加载好的模块 模块里的对象天然就是 单列的 即使是多线程环境下 也是如此
# 1
# class Singleton:
#     def __init__(self,name):
#         self.name = name
#
#     def do_something(self):
#         pass
#
# singleton = Singleton("模块单列")


# from xxx import singleton
# 单列模式 设计模式的目的不是为了防止人为的搞破坏 而是让系统解耦合 让系统易于 理解 和 工作
# 2 使用装饰器
#
# def Singleton(cls):
#     instance = {}
#
#     def _singleton_wrapper(*args, **kwargs):
#         print(args,kwargs)
#         if cls not in instance:
#             instance[cls] = cls(*args, **kwargs)
#         return instance[cls]
#
#     return _singleton_wrapper
#
#
# @Singleton
# class SingletonTest:  # SingletonTest = Singleton(SingletonTest)
#     def __init__(self, name):
#         self.name = name
#
#
# slt_1 = SingletonTest("第一次创建")
# slt_2 = SingletonTest("第二次创建")
# print(slt_1)
# print(slt_2)
# 通过装饰器修饰的类进行创建实例对象时将自己的 类名 作为 key 空间地址作为 value 存入到字典中 每次实例化对象的时候会进行 查询 若
# 实例化过 则直接返回 对象空间地址
# 但是 在多线程中时不安全的 因为 假若多线程 同时进行查询时 字典为空 所有线程都会创建新的对象

# 3 通过类方法
class Singleton:

    def __init__(self, name):
        self.name = name

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            Singleton._instance = Singleton(*args, **kwargs)
        return Singleton._instance

# class A():  # 普通单列模式
#     __distance = None
#
#     def __init__(self):
#
#         pass
#
#     def __new__(cls, *args, **kwargs):
#
#         if cls.__distance is None:
#             cls.__distance = super().__new__(cls)
#
#         return cls.__distance
#
# a = A()
# b = A()
# print(a)
# print(b)
# class A():
#     __instance = None
#
#     def __init__(self, name):
#         print("我是init")
#         self.name = name
#
#     def __new__(cls, *args, **kwargs):  # 开辟空间
#         print("我是new")
#         if not cls.__instance:
#             cls.__instance = super().__new__(cls)  # 让父类开空间
#             print(cls.__instance)
#         return cls.__instance
#
#     def show(self):
#         print(self.name)
#
#
# a = A("alex")
# a1 = A("asdasd")
# print(a.name)
# print(a1 )
