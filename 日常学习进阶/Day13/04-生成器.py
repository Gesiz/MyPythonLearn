# 特点: 生成器可以记录代码的执行状态
#      节省空间资源

def func():
    for i in range(5):
        print("start")
        # 如果函数中有yield 这个函数成为了一个生成器
        yield i
        print("end")


# 通过func创建了生成器a
a = func()
# 1 next可以执行我们的生成器,next执行完毕之后会把yield后的数值返回(return很相似)
#   next一旦超出范围会报异常(异常处理解决)
ret = next(a)
print(ret)

ret = next(a)
print(ret)

ret = next(a)
print(ret)

# 2 for循环也可以使用生成器 不会报异常
for i in a:
    print(i)


