a = int(input('请输入第一个数字:'))
b = int(input('请输入第二个数字:'))
# if a > b:
#     result = a - b
# else:
#     result = b - a

result = (a - b) if a > b else (b - a)

print('两个数字之间的差值为:', result)
