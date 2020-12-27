from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
# Create your views here.

# 视图
# 视图 其实就是特殊的 python函数

# 1. 视图函数的第一个参数,是表示 请求实例对象
# request = HttpRequest()

# 2. 视图函数必须有响应  .返回一个 HttpResponse的(子类)实例对象
def index(request):

    # return HttpResponse('this is test page')

    #定义一个字典
    data = {
        'show':'元旦 快乐~~~~'
    }

    # render 加载并渲染HTML
    # request,              请求对象
    # template_name,        模板名字. 我们写相对路径
    # context=None          我们可以将字典数据传递给context
    return render(request,'book/index.html',context=data)

