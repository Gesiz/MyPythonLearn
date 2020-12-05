# class A:
#     def __init__(self):
#         self.__name = "hell"
#
#
# class B:
#     def __init__(self):
#         self.name = "hell"
#
# class C(A):
#     pass
#
# class D(B):
#     pass
#
# # a = A()
# b = B()
# print(b.name)
# # print(a.name)
# # c = C()
# # print(c.name)
# d = D()
# print(d.name)
#

# import sys
# class A():
#     def __init__(self,name):
#         self.name = name
# # print(sys.getrefcount(A()))
# a = A("name")
# b = a
# del a
# print(sys.getrefcount(b))
# print(b.__dict__)
