from django.urls import path
from . import views # 추가

app_name = 'articles'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('greeting/', views.greeting, name='greeting'),
    path('greeting1/', views.greeting1, name='greeting1'),
    path('dinner/', views.dinner, name='dinner'),
    path('dtl-practice/', views.dtl_practice),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('hello/<str:name>/', views.hello, name='hello'), # path('hello/<str:name>/', view.hello)
]