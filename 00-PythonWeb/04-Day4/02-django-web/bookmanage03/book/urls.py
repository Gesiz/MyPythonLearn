from book.views import index, book, login, weibo, site_register, \
    get_header, get_method, http_res, get_redirct, res_json, \
    set_cookie, get_cookie, set_session, get_session
from book.converters import MonileConverter
from django.urls import path, include, converters, register_converter

# 系统 django 为我们提供了一些 验证路径参数
# converter 自定义转换器类
# type_name 自定义转换器的名字
register_converter(MonileConverter, 'phone')

urlpatterns = [
    path('index/', index),
    path('<cat_id>/<int:detail_id>/', book),
    path('login/', login),
    path('weibo/', weibo),
    # 自定义 路由转换器
    path('site/register/<phone:mobile>/', site_register),

    # 获取请求头
    path('header/', get_header),
    path('method/', get_method),
    path('res/', http_res),
    path('json/', res_json),
    path('redirect/', get_redirct),
    path('set_cookie/', set_cookie),
    path('get_cookie/', get_cookie),
    path('set_session/', set_session),
    path('get_session/', get_session),
]
