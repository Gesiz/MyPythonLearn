class F:
    def info(self):

        print('F')


class E(F):
    def info(self):
        print('E')
        super().info()


class D(F):
    def info(self):
        print('D')
        super().info()


class C(E):
    def info(self):
        print('C')
        super().info()


class B(D):
    def info(self):
        print('B')
        super().info()


class A(B,C):
    def info(self):
        print('A')
        super().info()

a = A()
a.info()