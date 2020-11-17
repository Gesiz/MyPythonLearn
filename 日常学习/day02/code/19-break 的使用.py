for i in range(1, 6):
    if i == 4:
        print('吃饱了,不吃了')
        break
    print(f'正在是编号为{i} 的苹果')


# 注意点: break和continue 如果用在循环嵌套中,只对最近的一层循环起作用
for i in range(5):
    print('操场跑圈中.....')
    for j in range(3):
        if j == 1:
            break
        print('做了一个俯卧撑')