from django.shortcuts import render, get_object_or_404
from .models import Task, Note, SubTask, Priority, Category

def dashboard(request):
    tasks = Task.objects.all()
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(status='completed').count()
    pending_tasks = tasks.filter(status='pending').count()
    in_progress_tasks = tasks.filter(status='in_progress').count()

    return render(request, 'TheLab/dashboard.html', {
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'in_progress_tasks': in_progress_tasks,
        'tasks': tasks,
    })

def task_list(request):
    tasks = Task.objects.select_related('priority', 'category').all()
    return render(request, 'TheLab/task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    notes = Note.objects.filter(task=task)
    subtasks = SubTask.objects.filter(parent_task=task)
    return render(request, 'TheLab/task_detail.html', {
        'task': task,
        'notes': notes,
        'subtasks': subtasks
    })

def note_list(request):
    notes = Note.objects.all()
    return render(request, 'TheLab/note_list.html', {'notes': notes})

def subtask_list(request):
    subtasks = SubTask.objects.select_related('parent_task').all()
    return render(request, 'TheLab/subtask_list.html', {'subtasks': subtasks})

def dashboard(request):
    return render(request, 'dashboard.html')

def task_list(request):
    return render(request, 'task_list.html')

def task_detail(request, pk):
    return render(request, 'task_detail.html')

def note_list(request):
    return render(request, 'note_list.html')

def subtask_list(request):
    return render(request, 'subtask_list.html')

def category_list(request):
    return render(request, 'category_list.html')

def priority_list(request):
    return render(request, 'priority_list.html')

