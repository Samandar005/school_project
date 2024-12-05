from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.student_list, name='list'),
    path('list/', views.student_list, name='list'),
    path('create/', views.student_create, name='create'),
    path('detail/<int:pk>/', views.student_detail, name='detail'),
    path('<int:pk>/delete/', views.student_delete, name='delete'),
]
