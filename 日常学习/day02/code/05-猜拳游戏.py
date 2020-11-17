# 1. 用户输入
player = int(input('请输入要出的内容: 1(石头) 2(剪刀) 3(布):'))
# 2. 电脑随机输入, 先假设电脑只会出一样
computer = 1
# 3. 判断胜负  shift enter 直接在下方新建一行
# 用户赢 ① player == 1 and computer == 2  ② player == 2 and computer==3 ③ player==3 and computer==1
if (player == 1 and computer == 2) or (player == 2 and computer == 3) \
        or (player == 3 and computer == 1):
    print('恭喜你,获得胜利')
# 平局 player == computer
elif player == computer:
    print('平局,不要走,大战三百回合')
# 用户输
else:
    print('弱鸡,你输了....')
