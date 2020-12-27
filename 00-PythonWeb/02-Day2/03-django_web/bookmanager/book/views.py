from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse


# Create your views here.


# 视图
# 视图 其实他就是特殊的 python函数

# 1. 视图函数的第一个参数 是表示 实例对象
# request
def index(request):

    # 定义一个字典
    # data = {
    #
    # }
    data = {
        'show' : '圣诞节快乐'
    }
    # return HttpResponse('this is test page')
    # render 加载并渲染html
    # request 请求对象
    # 模板名称
    # 传递字典
    return render(request,'book/index.html',context=data)
# 2 视图函数必须有响应 返回一个HttpResponse 的子类对象
