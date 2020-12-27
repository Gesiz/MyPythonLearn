from pprint import pprint

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpRequest
from book.models import BookInfo, PeopleInfo


# Create your views here.


# 视图函数

def index(request):
    return HttpResponse('asd')


# 通过路由传参 注意 这两个参数名 必须跟路由中 参数名一致
def book(request, cat_id, detail_id):
    print(cat_id, detail_id)
    # books = PeopleInfo.objects.filter(book__id=cat_id)
    # print([book.name for book in books])
    ################ 获取查询字符串 ##################
    query_string = request.GET
    # query_string
    # a=query_string.get('key')
    # b=query_string.get('value')
    # print(query_string)
    # print(a,b)
    """
    QueryDict 可以 一键一值  QueryDict_data.get(key)
                也可以一键一值 QueryDict_getlist(key)
    """
    alist = query_string.getlist('key')
    blist = query_string.getlist('value')
    print(alist, blist)
    #################key value 一键一值############################

    # 非常规使用

    # get(key,key不存时使用的默认值)
    page = query_string.get('page', 1)

    return HttpResponse('a,b')


def login(request):
    # POST 请求
    # 接收 form-data 数据的属性
    query_string = request.POST
    print(query_string)

    name = query_string.getlist('username')
    name = query_string.get('username')
    print(name)
    return HttpResponse("login")


def weibo(request):
    query_string = request.body

    import json
    print(json.loads(query_string.decode()))
    """{
        "name": "it",
        "age": 10
    }"""
    # b'{\n\t"name":"it",\n\t"age":10\n}\n'

    return HttpResponse("")


def site_register(request, mobile):
    return HttpResponse(mobile)


def get_header(request):
    # print(request.META['HTTP_ACCEPT'])
    pprint(request.META)
    return HttpResponse(request.META)


def get_method(request):
    return HttpResponse(request.method)


########################## 响应 #######################
def http_res(request):
    # content 翻译 内容 响应体的内容 响应体的内容 可以是 Str int list dict 不能是对象
    # content_type = 响应体数据类型 告知跨浏览器 我返回的是什么呢数据
    # 语法形式
    return HttpResponse("123", status=200, content_type='text/html')


from django.http.response import JsonResponse


def res_json(request):
    # JSON 数据 和 Python 中的字典很像
    # JSON <==>
    data = {
        'name': 'itcast',
        'age': 15
    }
    # JsonResponse 的第一个参数 data 要求 数据格式 为字典类型
    # safe 参数用来判断 是否判断 data 为 字典数据
    return JsonResponse(data, safe=False)


def get_redirct(request):
    # return redirect('http://www.baidu.com')
    return redirect('/json/')


# 返回cookie

def set_cookie(request):
    # 查询字符串的name 数据
    name = request.GET.get('name')

    # 设置cookie 是由服务器设置的
    # 我们要获取到响应对象 调用响应对象的 set_cookie 方法
    response = HttpResponse('set_cookie')
    # max_age 过期时间 默认关闭浏览器自动销毁

    response.set_cookie(key='name', value=name,max_age=60)

    # 删除cookie
    # response.delete_cookie(key='name)
    print('already set')
    return response


def get_cookie(request):
    # 服务器
    # 服务器获取cookie
    cookies = request.COOKIES
    print(cookies)
    return HttpResponse('cookies')

def set_session(request):
    # 服务器设置 session
    # request.session[''] 来设置session 操作 request.session 类似于操作字典

    # 新增一个数据
    request.session['value'] = 'B'
    request.session['name'] = 'A'
    # session 的数据是保存在服务器端


    return HttpResponse('')

def get_session(request):
    print(request.session.get('value'))
    print(request.session.get('name'))
    return HttpResponse('')

def session_clear(request):
    # request.session.clear() # 清除session内部
    # request.session.flush() # 清楚session本身
    # request.session.flush()
    # request.session.expiry(5) # 默认有效期为两周 如果 value 为 0 则 session的Cookie 将在浏览器关闭时过期
    # 如果 value 为None 那么
    pass