# 当序列中的内容全部遍历结束,会结束循环
for i in 'hello':
    print(i)  # 变量i 是字符串中的每一个字符

# for 结合range() 的使用
# range(n) 生成[0, n-1] 的可迭代序列

for i in range(5):  # 0 1 2 3 4
    print('操场跑圈中....')

# range(start, end, step)  生成[start, end) 的可迭代序列,步长是step,
# 步长是指两个相邻数据之间的间隔,默认是1, 可以不写

for i in range(3, 6):  # 3 4 5
    print(i)

print('-' * 30)
for i in range(2, 8, 2):   # 2 4 6
    print(i)

print('-' * 30)
for i in range(2, 9, 2):   # 2 4 6 8
    print(i)

print('-' * 30)
for i in range(9, 2, -3):  # 9  6 3
    print(i)

print('-' * 30)
for i in range(3, 1, 1):  # 不能生成数据,数据序列是空的,不能进入循环
    print('循环中的代码会执行吗')
