# TheLab/admin.py
from django.contrib import admin
from .models import Priority, Category, Task, Note, SubTask

@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "deadline", "priority", "category", "created_at")
    list_filter = ("status", "priority", "category")
    search_fields = ("title", "description")
    date_hierarchy = "deadline"   
    ordering = ("-created_at",)

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("task", "created_at")
    search_fields = ("content",)
    list_filter = ("created_at",)

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ("title", "parent_task", "status", "created_at")
    list_filter = ("status",)
    search_fields = ("title",)



