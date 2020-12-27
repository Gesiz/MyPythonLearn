from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from book.models import BookInfo, PeopleInfo


# Create your views here.


def index(request):
    # 无缓存
    BookInfo.objects.all()
    [book.id for book in BookInfo.objects.all()]
    # 这里隔离了很多的
    [book.id for book in BookInfo.objects.all()]
    # 需要缓存
    books = BookInfo.objects.all()

    [book.id for book in books]

    [book.id for book in books]

    # 限制结果集 通过切片
    PeopleInfo.objects.all()[1:3]

    return HttpResponse('ok')


# 1 导入分页类

from django.core.paginator import Paginator

# 2 查询结果集

people = PeopleInfo.objects.all()

# 3 创建分页类
# object_list
# per_page
paginator = Paginator(object_list=people, per_page=2)
# 4 获取分页
persons = paginator.page(2)
persons.object_list
paginator.num_pages

# 5 获取分页总数
# 手动调用save方法
# from  book.models import BookInfo
# book = BookInfo()
#
# book.name = 'django'
# book.readcount = 10
# book.commentcount = 100
# book.pub_date = '2002-2-2'
# book.save() 是父类 orm 中已经封装好的

# 方法二
# BookInfo.object.save
# object 相当于代理人 这个代理人 可以帮助我们实现增删改查操作
# BookInfo.objects.create(
#     name = 'python',
#     pub_date = '2020-1-1',
#     readcount =10,
#     commentcount = 100,
# )

# 修改数据
# 方法 1
# 获取实例对象 通过修改hi里对象的属性来修改数据
# 1 获取实例对象
# book = BookInfo.objects.get(id = 1)
# # 通过修改实例对象的属性来修改
# book.name =  '射雕英雄后传'
# book.pub_data = 2020-1-1
# # 人为的调用 实例对象那的 save 方法
# book.save()

# 方法二
# 直接调用 查询数据的方法 查询数据之后 直接调用update方法
# filter() 就是根据条件查询数据
# BookInfo.objects.filter(id=1).update(
#     name='射雕英雄中传',
#     pub_date='2020-2-1',
# )
#
# # 删除对象
# # 方法一
# # 获取实例对象 通过调用delete 方法来实现数据的删除
# # 注意 id 对应的数据一定要存在
# book = book.objects.get(id=6)
# # 调用 delete方法
# # delete 方法是父类中orm已经定义好  的方法
# book.delete()
#
# # 方法二
# book.objects.filter(id=5).delete()
#
# # all() 查询所有结果

# # count() 查询结果数量
# book.objects.all().count()
# # get() 只能查询唯一值 如果不存在则会抛出模型类 DoesNotExist 异常
# Bookinfo.objects.get(id=1)
# try:
#     BookInfo.objects.get(id=1)
# except Exception as e:
#     print(e)
#
# # 查询 过滤查询
# # filter 过滤出多个结果 返回的是列表
# # exclude 排除掉符合条件剩下的结果
# # get 过滤单一的结果
# ############  filter get exclude #############
#
# # 模型类名.objects.filter(属性名__运算符=值)
# # exact 精确的 准确的
# BookInfo.objects.get(id__exact=1)
# # 和 BookInfo.objects.get(id = 1)
#
#
# # 对比 get 和 filter的区别
# BookInfo.objects.filter(id=2)
# # filter 返回的是列表数据
# # get 若查询不存在 则会报错 filter 查询的数据如果不存在 不会报异常 空列表
#
# # 查询编号为1 的图书
# book = BookInfo.objects.get(id=1)
# list = BookInfo.objects.filter(id=1)  # 若存在多个
#
# # 查询书名包含 '湖' 的图书
# BookInfo.objects.filter(name__contains='湖')
#
# # 查询书名以'部'结尾的图书
# BookInfo.objects.filter(name__endswith='部')
#
# # 查询书名为空的图书
# BookInfo.objects.filter(name__isnull=True)
#
# # 查询编号为 1,3,5 的图书
# BookInfo.objects.filter(id_in=[1, 3, 5])
#
# # 查询编号大于3的图书
# # gt 大于
# # gte 大于等于
# # lt 小于
# # lte 小于等于
#
# BookInfo.objects.filter(id_gt=3)
#
# # 查询1980发表的图书
# BookInfo.objects.filter(pub_date__year='1980')
#
# # 查询大于1980年的图书
# BookInfo.objects.filter(pub_date__gt='1980-1-1')
#
# # 查询编号不等于3的图书
# # not
# BookInfo.objects.exclude(id=3)
#
################# F 对象

# 例查询阅读量大于等于评论量的对象
# 2个属性的比较

from django.db.models import F

# 导包的快捷方式
# 光标在的地方 alt+enter

# 语法形式
# 模型类名.objects.filter(属性名__运算符=F('属性名'))
# BookInfo.objects.filter(readcount_gte=F('commentcount'))
# # 查询阅读量大于两倍评论量的图书
# BookInfo.objects.filter(readcount_gte=F('commentcount') * 2)
#
# # Q 对象
# # 查询编号大于2 并且 阅读量大于20的图书 并且
# BookInfo.objects.filter(id__ge=2).filter(readcount__gt=20)
# BookInfo.objects.filter(id__ge=2, readcount__gt=20)
# # 多条件查询
# from django.db.models import Q
#
# # Q对象的语法形式
# BookInfo.objects.filter(Q(id__gt=2) & Q(readcount_gt=20))
#
# #  | 或者
# # 查询编号大于2 或者阅读量大于20的图书
# BookInfo.objects.filter(Q(id__gt=2) | Q(readcount_gt=20))
#
# # ~非
# BookInfo.objects.filter(~Q(id=2))
# BookInfo.objects.exclude(id=2)
#
#
# # 聚合函数
#
# # 模型类名.objects.aggregate(Xxx)
#
# from django.db.models import Max,Min,Count,Sum,Avg
# # 返回的是字典
# BookInfo.objects.aggregate(Sum('readcount'))
# {'readcount__sum':114}
#
# # 默认是升序
# BookInfo.objects.all().order_by('readcount')

# 级联查询
# from book.models import BookInfo
#
# # 1 获取书籍信息
# book = BookInfo.objects.get(id=2)
# # 根据书籍信息获取人物信息
# book.peopleinfo_set.all()
#
# from book.models import PeopleInfo
# # 1 获取人物现信息
# people = PeopleInfo.objects.get(id=6)
# people.book.name
# people.book.readcount
#
#
# # 关联查询的过滤
#
# # 1 需要明确的数据
# # 2 添加条件
# # 查询图书 要求图书中 人物的描述 包含八
# BookInfo.objects.filter(属性值__运算符='值')
#
# BookInfo.objects.filter(peopleinfo__description__contains='八')
# # 查询图书 要求图书的人物为 ‘郭靖’
# BookInfo.objects.filter(peopleinfo__name='郭靖')
# BookInfo.objects.filter(peopleinfo__name_exact='郭靖')
#
#
# # 它会自动为我们添加一个字段
#
# # 查询图书阅读量大于30的所有人物
# from book.models import PeopleInfo
# PeopleInfo.objects.filter(book__readcount__gt=30)
#
# # 查询书名为 天龙八部的所有人物
# PeopleInfo.objects.filter(book__name__exact='天龙八部')
#
#
#
# BookInfo.objects.get(id=2)
# BookInfo.objects.all()
# Queryset 查询集
# 特性 1
# 多ing执行
# 创建查询集不会立即访问数据库 直到调用数据库


# 特性 打开mysql 的日志
