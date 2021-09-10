from django.urls import path
from . import views

app_name = 'board'
# board/ +
urlpatterns = [
    path('create/', views.create, name='create'),#board/create/
    path('', views.index, name='index'),#board/
    path('<int:question_pk>/', views.detail, name='detail'),#board/<int>/
    path('<int:question_pk>/update/', views.update, name='update'),#board/<int>/update/
    path('<int:question_pk>/delete/', views.delete, name='delete'),#board/<int>/delete/
]
