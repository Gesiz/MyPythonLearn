for i in range(5):
    print('操场跑圈中.....')
    for j in range(3):
        print('做了一个俯卧撑')

for i in range(5):
    for j in range(i+1):
        print('*', end=' ')
    print()

for i in range(5):
    for j in range(5-i):  # i=0 j range(5) 0 1 2 3 4  i=4 j range(1) 0
        print('*', end=' ')
    print()
