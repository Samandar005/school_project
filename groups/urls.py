from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('', views.group_list, name='group_list'),
    path('<int:pk>/', views.group_detail, name='group_detail'),
    path('create/', views.group_create, name='group_create'),
    path('<int:pk>/delete/', views.group_delete, name='group_delete'),
]
