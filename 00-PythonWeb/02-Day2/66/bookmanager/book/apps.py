from django.apps import AppConfig

# 在此是子应用的配置 这个配置只对子应用起作用
class BookConfig(AppConfig):
    name = 'book'
    verbose_name = '书籍'
