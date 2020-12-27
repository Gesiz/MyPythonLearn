from django.urls import path
from book.views import index
# 在子应用中定义子应用的路由

# urlpatterns = [] 固定写法
#http://127.0.0.1:8000/book/index/
# index/

urlpatterns = [
    # path('index/',index),
    # path('',index),
    #
    path('index/',index),


]