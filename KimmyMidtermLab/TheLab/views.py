from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.utils import timezone
from TheLab.models import Category, Note, Priority, Task, SubTask
from TheLab.forms import CategoryForm, NoteForm, PriorityForm, SubTaskForm, TaskForm

class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            "total_task": Task.objects.count(),
            "total_note": Note.objects.count(),
            "total_subtask": SubTask.objects.count(),
            "total_category": Category.objects.count(),
            "total_priority": Priority.objects.count(),
        })

        today = timezone.now().date()
        context["near_deadline_tasks"] = Task.objects.filter(
            deadline__gte=today,
            deadline__lte=today + timezone.timedelta(days=7)
        ).order_by("deadline")

        context["recent_tasks"] = Task.objects.order_by("-created_at")[:5]
        return context


class SearchableSortableListView(ListView):
    search_fields = []
    ordering_fields = []
    default_order = "id"

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get("q")

        if query and self.search_fields:
            q_objects = Q()
            for field in self.search_fields:
                q_objects |= Q(**{f"{field}__icontains": query})
            qs = qs.filter(q_objects)

        sort_by = self.request.GET.get("sort_by")
        if sort_by in self.ordering_fields:
            qs = qs.order_by(sort_by)
        else:
            qs = qs.order_by(self.default_order)

        return qs


class CategoryList(SearchableSortableListView):
    model = Category
    context_object_name = "category"
    template_name = "category_list.html"
    paginate_by = 5
    search_fields = ["name"]
    ordering_fields = ["name", "-name"]
    default_order = "name"


class NoteList(SearchableSortableListView):
    model = Note
    context_object_name = "note"
    template_name = "note_list.html"
    paginate_by = 5
    search_fields = ["task", "content"]
    ordering_fields = ["task", "-task", "content", "-content"]
    default_order = "task"


class PriorityList(SearchableSortableListView):
    model = Priority
    context_object_name = "priority"
    template_name = "priority_list.html"
    paginate_by = 5
    search_fields = ["name"]
    ordering_fields = ["name", "-name"]
    default_order = "name"


class SubtaskList(SearchableSortableListView):
    model = SubTask
    context_object_name = "subtask"
    template_name = "subtask_list.html"
    paginate_by = 5
    search_fields = ["task__title", "title", "status"]
    ordering_fields = ["task", "title", "status", "-task", "-title", "-status"]
    default_order = "title"


class TaskList(SearchableSortableListView):
    model = Task
    context_object_name = "task"
    template_name = "task_list.html"
    paginate_by = 5
    search_fields = ["title", "description", "deadline", "status"]
    ordering_fields = ["title", "deadline", "status", "-title", "-deadline", "-status"]
    default_order = "title"


# Create Views
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')

class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')

class PriorityCreateView(CreateView):
    model = Priority
    form_class = PriorityForm
    template_name = 'priority_form.html'
    success_url = reverse_lazy('priority-list')

class SubtaskCreateView(CreateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = 'subtask_form.html'
    success_url = reverse_lazy('subtask-list')

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')


# Update Views
class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')

class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')

class PriorityUpdateView(UpdateView):
    model = Priority
    form_class = PriorityForm
    template_name = 'priority_form.html'
    success_url = reverse_lazy('priority-list')

class SubtaskUpdateView(UpdateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = 'subtask_form.html'
    success_url = reverse_lazy('subtask-list')

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')


# Delete Views
class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_del.html'
    success_url = reverse_lazy('category-list')

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'note_del.html'
    success_url = reverse_lazy('note-list')

class PriorityDeleteView(DeleteView):
    model = Priority
    template_name = 'priority_del.html'
    success_url = reverse_lazy('priority-list')

class SubtaskDeleteView(DeleteView):
    model = SubTask
    template_name = 'subtask_del.html'
    success_url = reverse_lazy('subtask-list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_del.html'
    success_url = reverse_lazy('task-list')