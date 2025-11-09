from django import forms
from django.forms import ModelForm
from TheLab.models import Category, Note, Priority, Task, SubTask

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Category Name"}),
        }

class PriorityForm(ModelForm):
    class Meta:
        model = Priority
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Priority Name"}),
            "level": forms.NumberInput(attrs={"class": "form-control"}),
        }

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Task Title"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "priority": forms.Select(attrs={"class": "form-control"}),
            "deadline": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-control"}),
        }

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = "__all__"
        widgets = {
            "task": forms.Select(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }

class SubTaskForm(ModelForm):
    class Meta:
        model = SubTask
        fields = "__all__"
        widgets = {
            "task": forms.Select(attrs={"class": "form-control"}),
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Subtask Title"}),
            "status": forms.Select(attrs={"class": "form-control"}),
        }
