from django.urls import path
from . import views

app_name = 'teachers'

urlpatterns = [
    path('', views.teacher_list, name='teacher_list'),
    path('<int:pk>/', views.teacher_detail, name='teacher_detail'),
    path('create/', views.teacher_create, name='teacher_create'),
    path('<int:pk>/delete/', views.teacher_delete, name='teacher_delete'),
]
