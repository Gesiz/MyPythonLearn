from django.db import models

# Create your models here.
"""
模型类的定义
class 模型类名(models.Model):
    属性名 字段名=models.类型(选项) 

# 注意不要使用python 和 mysql 的关键字


类 和 表 的关系

表名 类名
字段 属性
记录 实例对象
create table bookinfo{
    id int primary key comment
    name varchar(11) default  '' not null comment "书籍名字"
}

"""


class BookInfo(models.Model):
    """
    id 主键
    name  书籍名称
    pub_date 数据发布日期
    readcount 阅读量
    commentcount 评论量
    is_delete 是否删除

    # id 自动生成
    """
    name = models.CharField(max_length=21, verbose_name='admin站点相关不是重点')
    pub_date = models.DateField(null=True)
    readcount = models.IntegerField(default=1)
    commentcount = models.IntegerField(default=1)
    is_delete = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    # 默认数据表的名字是 子应用名小写_子应用小明_类名向小写

    # 表面是可以修改的

    class Meta:
        db_table = 'bookinfo'  # 表名是可以修改的
        verbose_name = '图书信息'
        verbose_name_plural = verbose_name


class PeopleInfo(models.Model):
    """
    id
    name  人物名
    gender 性别
    description 描述
    is_delete 逻辑和三处
    book_id 书键外籍

    """
    name = models.CharField(max_length=10)
    # choices 的值 定义元组
    # 只能从元组中选取一个
    GENDER_CHOICE = (
        (0, 'boy'),
        (1, 'girl')
    )
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=0)
    description = models.CharField(max_length=128, null=True)
    is_delete = models.BooleanField(default=False)

    # 外键
    # 属性 -- 字段 表的字段 会自动给我们的属性值添加一个_id
    # 类型 -- models.ForeignKey
    # 选项 -- 第一个参数 关联的类名
    #        第二个参数 on_delete

    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'peopleinfo'  # 表名是可以修改的
        verbose_name = '人物信息'
        verbose_name_plural = verbose_name
