# 素数: 只能被1 和本身整除的数
# 判断一个数字是不是素数, 从2开始到数字-1 为止, 所有的数字都不能被整除,

# num = int(input('请输入一个数字:'))
for num in range(100, 201):
    for i in range(2, num):  # range(2, 2)
        if num % i == 0:
            # print('这个数字不是素数')
            break
    else:
        # print(f'{num} 是素数')
        print(num, end=' ')



