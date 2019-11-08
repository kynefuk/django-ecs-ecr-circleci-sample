from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.TodoListView.as_view(), name='list'),
    path('create/', views.TodoCreateView.as_view(), name='create'),
]
