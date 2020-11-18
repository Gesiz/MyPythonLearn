my_str = 'good'

for i in my_str:
    print(i)  # i 是字符串中的每一个字符


print('*' * 30)
j = 0   # 当做下标使用
while j < len(my_str):
    print(my_str[j])
    j += 1
