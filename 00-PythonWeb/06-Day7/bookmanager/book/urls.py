from django.urls import path
from book.views import test, JDLogin,CenterView

urlpatterns = [
    path('test/', test),
    path('jd/', JDLogin.as_view()),
    path('center/',CenterView.as_view()),
]
