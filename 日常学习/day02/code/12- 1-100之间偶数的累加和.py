# 偶数: 能被2整数的数字, % 2 == 0
# 定义变量i ,为数字的起始值
i = 1

# 定义变量,保存求和的结果
my_sum = 0

while i <= 100:
    if i % 2 == 0:
        # 求和
        my_sum = my_sum + i
    i += 1

print('求和的结果为:', my_sum)

# 1 - 100 之间的偶数和,
j = 2
result = 0
while j <= 100:
    result = result + j
    j += 2

print('求和的结果是:', result)
