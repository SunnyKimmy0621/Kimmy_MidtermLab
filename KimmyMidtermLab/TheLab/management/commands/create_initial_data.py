from django.core.management.base import BaseCommand
from faker import Faker
from TheLab.models import Department, Job, Organization, Employee, OrgMember 

class Command(BaseCommand):
    help = 'Create initial data for the application'

    def handle(self, *args, **kwargs):
        self.create_organization(10)
        self.create_employees(50)
        self.create_membership(10)

    def create_organization(self, count):
        fake = Faker()
        for _ in range(count):
            words = [fake.word() for _ in range(2)]  # two random words
            organization_name = ' '.join(words)
            Organization.objects.create(
                name=organization_name.title(),
                department=Department.objects.order_by('?').first(),
                description=fake.sentence()
            )
        self.stdout.write(self.style.SUCCESS(
            'Initial data for organizations created successfully.'
        ))

    def create_employees(self, count):
        fake = Faker('en_PH')
        for _ in range(count):
            Employee.objects.create(
                employee_id=f"{fake.random_int(2020, 2025)}-{fake.random_int(1, 8)}-{fake.random_number(digits=4)}",
                lastname=fake.last_name(),
                firstname=fake.first_name(),
                middlename=fake.last_name(),
                job=Job.objects.order_by('?').first(),
            )
        self.stdout.write(self.style.SUCCESS(
            'Initial data for employees created successfully.'
        ))

    def create_membership(self, count):
        fake = Faker()
        for _ in range(count):
            OrgMember.objects.create(
                employee=Employee.objects.order_by('?').first(),
                organization=Organization.objects.order_by('?').first(),
                date_joined=fake.date_between(start_date="-2y", end_date="today"),
            )
        self.stdout.write(self.style.SUCCESS(
            'Initial data for employee organization memberships created successfully.'
        ))
