from django.contrib import admin
from django.urls import path, include
from TheLab.views import (
    HomePageView,
    CategoryList, NoteList, PriorityList, SubtaskList, TaskList,
    CategoryCreateView, NoteCreateView, PriorityCreateView, SubtaskCreateView, TaskCreateView,
    CategoryUpdateView, NoteUpdateView, PriorityUpdateView, SubtaskUpdateView, TaskUpdateView,
    CategoryDeleteView, NoteDeleteView, PriorityDeleteView, SubtaskDeleteView, TaskDeleteView
)
from TheLab import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('', login_required(HomePageView.as_view()), name='home'),
    path('', include('pwa.urls')),

    # LIST VIEWS
    path('category_list/', CategoryList.as_view(), name='category-list'),
    path('note_list/', NoteList.as_view(), name='note-list'),
    path('priority_list/', PriorityList.as_view(), name='priority-list'),
    path('subtask_list/', SubtaskList.as_view(), name='subtask-list'),
    path('task_list/', TaskList.as_view(), name='task-list'),

    # CREATE VIEWS
    path('category_list/add/', CategoryCreateView.as_view(), name='category-add'),
    path('note_list/add/', NoteCreateView.as_view(), name='note-add'),
    path('priority_list/add/', PriorityCreateView.as_view(), name='priority-add'),
    path('subtask_list/add/', SubtaskCreateView.as_view(), name='subtask-add'),
    path('task_list/add/', TaskCreateView.as_view(), name='task-add'),

    # UPDATE VIEWS
    path('category_list/<pk>/edit/', CategoryUpdateView.as_view(), name='category-update'),
    path('note_list/<pk>/edit/', NoteUpdateView.as_view(), name='note-update'),
    path('priority_list/<pk>/edit/', PriorityUpdateView.as_view(), name='priority-update'),
    path('subtask_list/<pk>/edit/', SubtaskUpdateView.as_view(), name='subtask-update'),
    path('task_list/<pk>/edit/', TaskUpdateView.as_view(), name='task-update'),

    # DELETE VIEWS
    path('category_list/<pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    path('note_list/<pk>/delete/', NoteDeleteView.as_view(), name='note-delete'),
    path('priority_list/<pk>/delete/', PriorityDeleteView.as_view(), name='priority-delete'),
    path('subtask_list/<pk>/delete/', SubtaskDeleteView.as_view(), name='subtask-delete'),
    path('task_list/<pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
]
