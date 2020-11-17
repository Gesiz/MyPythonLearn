# 坐车案例,需要先判断有没有钱,有钱上车,再判断有没有空的座位,有才能做下
money = int(input('请输入你有多少钱:'))

if money >= 2:
    print('有钱,可以上车....')
    seat = int(input('请输入空座位的个数:'))
    if seat > 0:
        print('有座位,可以坐着,很舒服')
    else:
        print('没有座位,站着吧,锻炼身体')
else:
    print('余额不足,你走吧')

