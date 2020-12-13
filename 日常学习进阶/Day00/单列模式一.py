class A():
    __instance = None

    def __init__(self, name):
        print("我是init")
        self.name = name

    def __new__(cls, *args, **kwargs):  # 开辟空间
        print("我是new")
        if not cls.__instance:
            cls.__instance = super().__new__(cls)  # 让父类开空间
            print(cls.__instance)
        return cls.__instance

    def show(self):
        print(self.name)


a = A("alex")
a1 = A("asdasd")
print(a.name)
print(a1 )
