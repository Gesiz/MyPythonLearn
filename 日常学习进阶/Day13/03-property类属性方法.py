class Person:
    def __init__(self,age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self,new_age):
        self.__age = new_age

    # age 就是获取property属性了
    # 参数1 获取property属性的方法
    # 参数2 设置property属性的方法
    age = property(get_age,set_age)