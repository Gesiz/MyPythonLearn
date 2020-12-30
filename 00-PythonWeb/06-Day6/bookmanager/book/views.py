from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


# Create your views here.


def index(request):
    return render(request, '')


def test(request):
    if request.method == 'GET':
        return HttpResponse("GET")
    elif request.method == 'POST':
        return HttpResponse("POST")


# 面向对象 --类
# 类中 除了属性 就是方法

"""
class 类名():
    def get():
        pass
    def post():
        pass
类视图的定义
1 类视图继承自 View
2 类视图的方法 是根据请求方式来实现的
    如果我们用post发送了一个个post请求 我们就实现类视图中post方法
"""
from django.views import View


class JDLogin(View):

    # self 指的是实例对象
    # request 指的是请求对象
    def get(self, request):
        return HttpResponse('jd - login - get')

    def post(self, request):
        return HttpResponse('jd - login - post')

    def test(self, request):
        return HttpResponse("")


############复习面向对象##############
class Person(object):
    # 实例方法
    def say(self):
        pass

    # 类方法
    @classmethod
    def eat(cls):
        pass

    # 静态方法
    @staticmethod
    def run():
        pass


#####################################
"""
如果我们访问 个人中心页面 必须要求用户登录

1 定义个人中心类视图
2 必须要求用户登录
"""

# 我们可以使用装饰器
# 也可以使用多继承
# class CenterView(View):
#     def get(self, request):
#         isLogin = True
#         if isLogin:
#             # 展示个人信息
#             return HttpResponse('cneter GET')
#         else:
#             return HttpResponse('请登录')
#
#     def post(self, request):
#         # 修改个人信息
#
#         isLogin = True
#         if isLogin:
#             # 展示个人信息
#             return HttpResponse('cneter POST')
#         else:
#             return HttpResponse('请登录')


from django.contrib.auth.mixins import LoginRequiredMixin


# LoginRequiredMixin

# LoginRequiredMixin 继承自 ACCessMixin
# AccessMixin 继承自 object
# CenterView 要求既要继承View 又要继承LoginRequiredMixin


# View 有一个 dispath
# LoginRequiredMixin 也有一个dispath

# 期望是 应该先验证是否登录 如果登录了 正常访问 如果没有登录 因该跳到登录页面
# 分析的结果是 应该先走 LoginRequiredMixin
class CenterView(LoginRequiredMixin, View):
    def get(self, request):
        # 展示个人信息
        return HttpResponse('center GET')

    def post(self, request):
        return HttpResponse('center POST')
