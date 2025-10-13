from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from TheLab.models import Organization, Department, Job, Employee, OrgMember
from TheLab.forms import DepartmentForm, JobForm, EmployeeForm, OrganizationForm, OrgMemberForm

class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = "home.html"

# Department
class DepartmentListView(ListView):
    model = Department
    context_object_name = 'department_list'
    template_name = "dept_list.html"

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
