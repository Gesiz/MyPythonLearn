class Car:
    def add_car(self):
        print('add_car')

    def edit_car(self):
        pass



name = 'car'

# print('car模块的name输出的内容：', __name__)


# 上面用来定义代码
# if判断里面写代码的调用
if __name__ == '__main__':
    car = Car()
    car.add_car()
