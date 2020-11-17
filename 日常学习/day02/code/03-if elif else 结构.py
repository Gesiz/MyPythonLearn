score = eval(input('请输入你的成绩:'))  # int float
# 1. 成绩大于等于90 ，输出优秀
if score >= 90:
    print('优秀')
# 2. 成绩大于等于80，小于90，输出良好
elif score >= 80 and (score < 90):
    print('良好')
# 3. 成绩大于等于60，小于80，输出及格
elif score >= 60:
    print('及格')
# 4. 小于60，输出不及格
else:
    print('不及格')

print('成绩判断完毕')
