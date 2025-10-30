from django.core.management.base import BaseCommand
from faker import Faker
from TheLab.models import Priority, Category, Task, SubTask, Note
import random
from django.utils import timezone


class Command(BaseCommand):
    help = 'Create initial test data for TheLab Task System'

    def handle(self, *args, **kwargs):
        self.create_priorities()
        self.create_categories()
        self.create_tasks(30)        # generate 30 tasks
        self.create_subtasks(60)     # generate 60 subtasks
        self.create_notes(50)        # generate 50 notes

        self.stdout.write(self.style.SUCCESS("✅ Initial data created successfully."))

    def create_priorities(self):
        priorities = ["High", "Medium", "Low"]
        for p in priorities:
            Priority.objects.get_or_create(name=p)
        self.stdout.write(self.style.SUCCESS("→ Priorities loaded."))

    def create_categories(self):
        fake = Faker()
        for _ in range(8):
            Category.objects.get_or_create(name=fake.word().title())
        self.stdout.write(self.style.SUCCESS("→ Categories loaded."))

    def create_tasks(self, count):
        fake = Faker()
        statuses = ["pending", "in_progress", "completed"]
        categories = list(Category.objects.all())
        priorities = list(Priority.objects.all())

        for _ in range(count):
            Task.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.paragraph(),
                deadline=fake.date_time_between(start_date="now", end_date="+30d", tzinfo=timezone.get_current_timezone()),
                status=random.choice(statuses),
                category=random.choice(categories),
                priority=random.choice(priorities),
            )
        self.stdout.write(self.style.SUCCESS("→ Tasks created."))

    def create_subtasks(self, count):
        fake = Faker()
        statuses = ["pending", "in_progress", "completed"]
        tasks = list(Task.objects.all())

        if not tasks:
            self.stdout.write(self.style.WARNING("No tasks found — skipping subtasks."))
            return

        for _ in range(count):
            SubTask.objects.create(
                parent_task=random.choice(tasks),
                title=fake.sentence(nb_words=3),
                status=random.choice(statuses),
            )
        self.stdout.write(self.style.SUCCESS("→ Subtasks created."))

    def create_notes(self, count):
        fake = Faker()
        tasks = list(Task.objects.all())

        if not tasks:
            self.stdout.write(self.style.WARNING("No tasks found — skipping notes."))
            return

        for _ in range(count):
            Note.objects.create(
                task=random.choice(tasks),
                content=fake.paragraph(),
            )
        self.stdout.write(self.style.SUCCESS("→ Notes created."))
