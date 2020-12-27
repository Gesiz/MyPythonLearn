from django.db import models

# Create your models here.
"""
1 定义模型类
2 模型迁移
    2.1 生成迁移文件(并不会生成表) python manage.py makemigrations
            迁移文件 在 makemigrations
    2.2 执行迁移文件(才会生成表)   pyyhon manager.pu migrate
            默认表是生成在 db.sqlite3 总
            # sqlite 小型关系型数据库 一般在移动端使用的多
            # mysql sql server orical 中型数据库
            # db2 大型
        表船舰的规律时 子应用名小写_类型类名小写
模型类

class 类名(models.Model):
    属性名(字段名) = models.字段类型(字段选项)
    
"""


class BookInfo(models.Model):
    # id    jango 会为我们自动创建一个主键
    # name  varchar
    name = models.CharField(max_length=10)
    def __str__(self):
        """将模型类以字符串的方式输出"""
        return self.name

# 人物
class PeopleInfo(models.Model):
    # id
    # name
    name = models.CharField(max_length=10)
    # gender 性别
    gender = models.BooleanField()
    # book
    # on_delete 外键的级联关系
    # 外键相关的只是 我们在后天会讲
    # 外键在数据库中 系统会自动为我们添加一个id
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)  # 模型的定义
    def __str__(self):
        """将模型类以字符串的方式输出"""
        return self.name