# 头 30 脚 86
# x+y = 30
# 2x+4y = 86

def get_ch(head, foot):
    x = 0
    y = 0
    for x in range(0, head + 1):
        for y in range(0, head - x + 1):
            if x + y == head and 2 * x + 4 * y == foot:
                return x,y
            else:
                print(x, y)




print(get_ch(100, 320))
