for i in range(1, 6):
    if i == 4:
        print('发现半条虫子,这个苹果不吃了,继续吃下一个')
        continue
    print(f'正在是编号为{i} 的苹果')


j = 1
while j < 6:
    if j == 4:
        print('发现半条虫子,这个苹果不吃了,继续吃下一个')
        j += 1
        continue
    print(f'正在是编号为{j} 的苹果')
    j += 1
