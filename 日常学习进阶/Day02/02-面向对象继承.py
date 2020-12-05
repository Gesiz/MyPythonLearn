# """类的继承"""
#
#
# # 定义A类
# class A:
#     pass
#
#
# # 定义B类 B类继承A类
# class B(A):
#     pass
#
#
# # 定义一个员工类
# class Staff:
#     def __init__(self):
#         self.name = "fine"
#         self.job_number = 91322
#
#     def eat(self):
#         print("吃饭")
#
#
# # 再定义一个讲师类
#
# class Teacher(Staff):
#     def teach(self):
#         print("讲课")
#
#
# teacher = Teacher()
# teacher.eat()
#
# # 获取父类的属性
# print(teacher.name)
# print(teacher.job_number)
#
# # 获取父类的方法
# teacher.teach()
# teacher.eat()


# 定义一个员工类
class Staff:
    def __init__(self,name,job_number):
        self.name = name
        self.job_number = job_number

    def eat(self):
        print("吃饭")


# 再定义一个讲师类

class Teacher(Staff):
    def teach(self):
        print("讲课")

teather = Teacher("fine","9132")