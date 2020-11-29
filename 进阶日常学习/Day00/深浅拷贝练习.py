
a = [1, 2]
a[1] = a
print(a[1])

class A:
    def func(self):
        pass
        raise Exception("WRONG")

class B(A):
    pass

def Text(obj):
    obj.func()

b = B()
Text(b)