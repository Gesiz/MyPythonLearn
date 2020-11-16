# 函数的传参方式是指 如何将实参的值传递给形参
def func(name, age, gender):
    print(f"name:{name},age:{age},gender:{gender}")


# 1 位置传参
func("xw", 18, "男")
# func("xw", 18, "男",1)  # 程序报错
# func("xw", 18)  # 程序报错 实参的个数小于形参的个数

# 2 关键字传参 使用变量=数据值 规定将形参给那个形参 注意 变量名 必须是形参的名字 否侧会被程序报错
func(age=18, name="xw", gender="男")

# 3 混合使用 必须注意 先写 位置传参的实参值 再写关键字传参的实参值 关键字实参的后面只能是关键字
# func('xh',age=17,"nv")  # 程序报错
# func('xh',17,age=18)  # 程序报错 重复传参 一个形参只能接受一个形参值
func("xh", 17, gender="女")

