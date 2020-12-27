from django.db import models

# Create your models here.
"""

1.定义模型类
2.模型迁移
    2.1 生成迁移文件(并不会生成表)      python manage.py makemigrations
            迁移文件在 migrations目录下
    2.2 执行迁移文件(才会生成表)       python manage.py migrate
            默认是表生成在 db.sqlite3中了
        表创建的规律是: 子应用名小写_模型类名小写
    特别强调: sqlite3 只是今天的过渡知识,后边我们将mysql

3.操作数据库



模型类

class 类名(models.Model):
    属性名(字段名)=models.字段类型(字段选项)

"""

class BookInfo(models.Model):
    # id        django 会为我们自动创建一个主键
    # name      varchar(10)
    name=models.CharField(max_length=10)


    def __str__(self):
        return self.name
# 人物
class PeopleInfo(models.Model):

    # id
    # name
    name=models.CharField(max_length=10)
    # gender  性别
    gender=models.BooleanField()
    # book  外键
    # 外键的级联关系
    # 外键相关的知识 先自己回顾,我们在后天会将
    # 外键在数据库中,系统会自动为我们添加一个 _id
    book=models.ForeignKey(BookInfo,on_delete=models.CASCADE)

    def __str__(self):
        return self.name