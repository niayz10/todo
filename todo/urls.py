from django.urls import path

from . import views


urlpatterns = [
    path('list/', views.list_todos, name='list_todos'),
    path('create/', views.create_todo, name='create-todo'),
    path('detail/<int:pk>/', views.todo_detail, name='todo-detail'),
    path('delete/<int:pk>/', views.delete_todo, name='delete-todo'),
    path('todo/<int:pk>/create_item/', views.create_items_of_todo, name='create-item'),
    path('todo/<int:pk>/items-list', views.items_list, name='items-list'),
]