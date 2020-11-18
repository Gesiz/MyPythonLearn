# 素数: 只能被1 和本身整除的数
# 判断一个数字是不是素数, 从2开始到数字-1 为止, 所有的数字都不能被整除,

num = input("请输入一个数字")

for i in range(2, int(num)):
    if int(num) % i == 0:
        break
    else:
        print(f"{num}是素数")
        break

