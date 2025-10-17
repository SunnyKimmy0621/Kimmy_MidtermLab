from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
    path('notes/', views.note_list, name='note_list'),
    path('subtasks/', views.subtask_list, name='subtask_list'),
    path('categories/', views.category_list, name='category_list'),
    path('priorities/', views.priority_list, name='priority_list'),
]


