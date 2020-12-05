# eval() exec() 禁止使用
print(eval("3+2*2/2"))

msg = """
print(input('>>>'))
"""
eval(msg)  #

msg = """
def func():
    print("aaa")
func()
"""
exec(msg)
