"""
自定义转换器的不走
1 创建一个文件 来定义一个转换器 目的 验证手机号
2 我们应该使用系统的方法来注册 自定义转换器
    需要到urls 中去注册
3 使用
"""


# 转换器

class MonileConverter:
    # 转换器起关键作用的是 regex的正则
    regex = '1[3-9]\d{9}'

    # 实现一个to_python 的方法
    # 获取到path中的参数 需要对这个参数做什么处理
    def to_python(self, value):
        return value
