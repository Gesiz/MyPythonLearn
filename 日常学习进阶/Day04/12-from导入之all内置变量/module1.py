# all设置了允许调用的资源
# __all__ = ['name1', 'name2', 'info']   # 也可以是元组，里面写需要被外部调用的资源名的字符串形式
# name1 、 name2被外部调用
name1 = 'module1'
name2 = 'module2'
name3 = 'module3'
name4 = 'module4'



def info():
    print('info')

__all__ = ['name1', 'name2', 'info']
# all放在任意位置都可以