from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from TheLab.models import Organization, Department, Job, Employee, OrgMember
from TheLab.forms import DepartmentForm, JobForm, EmployeeForm, OrganizationForm, OrgMemberForm
from django.utils import timezone
from django.db.models import Q
from TheLab.models import Organization
from TheLab.models import Department
from TheLab.models import Employee


def dashboard(request):
    # Count total organizations
    org_count = Organization.objects.count()

    # Count total programs
    department_count = Department.objects.count()

    employee_count = Employee.objects.count()

    context = {
        'org_count': org_count,
        'department_count': department_count,
        'employee_count': employee_count,
    }
    return render(request, 'dashboard.html', context)

class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Total counts
        context["total_employees"] = Employee.objects.count()
        context["total_departments"] = Department.objects.count()
        context["total_organizations"] = Organization.objects.count()

        # Employees joined this year
        today = timezone.now().date()
        employees_joined_this_year = (
            OrgMember.objects.filter(date_joined__year=today.year)
            .values("employee")
            .distinct()
            .count()
        )
        context["employees_joined_this_year"] = employees_joined_this_year

        return context

# Department
class DepartmentListView(ListView):
    model = Department
    context_object_name = 'department_list'
    template_name = "dept_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()

        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(department_name__icontains=query)
            )

        sort_by = self.request.GET.get('sort_by')
        if sort_by in ['department_name', '-department_name']:
            queryset = queryset.order_by(sort_by)

        return queryset

class DepartmentCreateView(CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = "dept_form.html"
    success_url = reverse_lazy('department-list')

class DepartmentUpdateView(UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = "dept_form.html"
    success_url = reverse_lazy('department-list')

class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = "dept_del.html"
    success_url = reverse_lazy('department-list')

# Job
class JobListView(ListView):
    model = Job
    context_object_name = 'joblist'
    template_name = "job_list.html"

    def get_ordering(self):
        allowed = ["job_name", "department__department_name"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "job_name"

class JobCreateView(CreateView):
    model = Job
    form_class = JobForm
    template_name = "job_form.html"
    success_url = reverse_lazy('job-list')

class JobUpdateView(UpdateView):
    model = Job
    form_class = JobForm
    template_name = "job_form.html"
    success_url = reverse_lazy('job-list')

class JobDeleteView(DeleteView):
    model = Job
    template_name = "job_del.html"
    success_url = reverse_lazy('job-list')

# Employee
class EmployeeListView(ListView):
    model = Employee
    context_object_name = 'employeelist'
    template_name = "emp_list.html"
    paginate_by = 5
    ordering = ["lastname", "firstname"]

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        sort_by = self.request.GET.get('sort', None)

        if query:
            qs = qs.filter(
                Q(firstname__icontains=query) |
                Q(lastname__icontains=query) |
                Q(job__job_title__icontains=query) 
            )

        allowed_sort = ["lastname", "firstname", "job"]
        if sort_by in allowed_sort:
            qs = qs.order_by(sort_by)

        return qs

class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = "emp_form.html"
    success_url = reverse_lazy('employee-list')

class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = "emp_form.html"
    success_url = reverse_lazy('employee-list')

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = "emp_del.html"
    success_url = reverse_lazy('employee-list')

# OrgMembers
class OrgMemberListView(ListView):
    model = OrgMember
    context_object_name = 'orgmemberlist'
    template_name = "orgmem_list.html"

    def get_queryset(self):
        queryset = OrgMember.objects.all()

        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(employee__firstname__icontains=query) |
                Q(employee__lastname__icontains=query) |
                Q(organization__organization_name__icontains=query)
            )

        sort_by = self.request.GET.get('sort_by')
        if sort_by:
            queryset = queryset.order_by(sort_by)

        return queryset

class OrgMemberCreateView(CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = "orgmember_form.html"
    success_url = reverse_lazy('orgmember-list')

class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = "orgmember_form.html"
    success_url = reverse_lazy('orgmember-list')

class OrgMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = "orgmember_del.html"
    success_url = reverse_lazy('orgmember-list')

# Organization
class OrganizationList (ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = "org_list.html"
    paginate_by = 5
    ordering = ["department__department_name","name"]
    
    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')
        sort_by = self.request.GET.get('sort_by')  

        if query:
            qs = qs.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
            )

        allowed_sort = ["name", "department__department_name"]
        if sort_by in allowed_sort:
            qs = qs.order_by(sort_by)

        return qs

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm   # ← remove the quotes
    template_name = "org_form.html"
    success_url = reverse_lazy('organization-list')

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')
