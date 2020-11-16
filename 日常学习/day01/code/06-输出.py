print('hello python')  # 输出str
print(123)  # int
print(3.14)  # float
print(True)  # bool

print('hello', 123, 3.14, False)
print(1 + 3)

# 定义三个变量
name = 'isaac'
age = 10
height = 179.1
print(name, age, height)

# 格式化输出
# %s 占位符 可以填充任意类型的数据
print("我的名字是%s" % name)
print("我的年龄是%s" % age)
print("我的身高是%s" % height)

# %f 占位符 需要填充 float 类型的数据
print('我的身高是%f' % height)
# %.nf 表示显示几位小数
print("我的身高是%2f" % height)

# %d 占位符 需要填充 int类型的数据
print('我的年龄是 %d 岁' % age)
print('我的年龄是 %d cm' % height)

# %s %f %d 三个连用
print('我的名字是 %s 我的年龄是 %d 我的身高是 %f ' % (name, age, height))

# 注意 若果使用格式化占位符 同时想要在格式化占位符后显示一个 % 后边需重叠转移 %%
num = 80
print('本次考试的及格率是 %.1f' % num)
print('本次考试的及格率是 %.1f %%' % num)

# f-string 从python3.6开始支持
# 在字符串中使用{}占位 要填充的数据直接写在{}中
print(f"我的名字是{name}，我的年龄是{age}")
print(f'我的名字是{name},我的年龄是{age} 我的身高是{height:.2f}')


