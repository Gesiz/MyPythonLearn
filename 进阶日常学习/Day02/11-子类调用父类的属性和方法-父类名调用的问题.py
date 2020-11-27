# 父类名的问题

class D:
    def info(self):
        print("D")


class C(D):
    def info(self):
        print("C")
        D.info(self)


class B(D):
    def info(self):
        print("B")
        D.info(self)


class A(B, C):
    def info(self):
        B.info(self)
        C.info(self)
        print("A")


print(issubclass(A, B))
a = A()
print(isinstance(a, A))
a.info()
