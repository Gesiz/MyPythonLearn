import random

zero_or_one = random.randint(0,1)

try:
    num = 100 / zero_or_one
except Exception as e :
    print(e)  # 捕获到异常执行的代码
else:
    print("nothing")  # 没有抛出异常执行的代码
finally:
    print("告辞")  # 不管有没有异常都会执行

# finally 作用体现


