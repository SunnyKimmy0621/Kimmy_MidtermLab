from django.urls import path
from .views import (
    HomePageView,
    LoginPageView,
    CategoryList, NoteList, PriorityList, SubtaskList, TaskList,
    CategoryCreateView, NoteCreateView, PriorityCreateView, SubtaskCreateView, TaskCreateView,
    CategoryUpdateView, NoteUpdateView, PriorityUpdateView, SubtaskUpdateView, TaskUpdateView,
    CategoryDeleteView, NoteDeleteView, PriorityDeleteView, SubtaskDeleteView, TaskDeleteView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='dashboard'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('categories/', CategoryList.as_view(), name='category'),
    path('notes/', NoteList.as_view(), name='note-list'),
    path('priorities/', PriorityList.as_view(), name='priority-list'),
    path('subtasks/', SubtaskList.as_view(), name='subtask-list'),
    path('tasks/', TaskList.as_view(), name='task-list'),

    path('categories/add/', CategoryCreateView.as_view(), name='category-add'),
    path('notes/add/', NoteCreateView.as_view(), name='note-add'),
    path('priorities/add/', PriorityCreateView.as_view(), name='priority-add'),
    path('subtasks/add/', SubtaskCreateView.as_view(), name='subtask-add'),
    path('tasks/add/', TaskCreateView.as_view(), name='task-add'),

    path('categories/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category-edit'),
    path('notes/<int:pk>/edit/', NoteUpdateView.as_view(), name='note-edit'),
    path('priorities/<int:pk>/edit/', PriorityUpdateView.as_view(), name='priority-edit'),
    path('subtasks/<int:pk>/edit/', SubtaskUpdateView.as_view(), name='subtask-edit'),
    path('tasks/<int:pk>/edit/', TaskUpdateView.as_view(), name='task-edit'),

    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    path('notes/<int:pk>/delete/', NoteDeleteView.as_view(), name='note-delete'),
    path('priorities/<int:pk>/delete/', PriorityDeleteView.as_view(), name='priority-delete'),
    path('subtasks/<int:pk>/delete/', SubtaskDeleteView.as_view(), name='subtask-delete'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
]