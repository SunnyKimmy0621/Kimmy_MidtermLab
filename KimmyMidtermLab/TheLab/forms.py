from django.forms import ModelForm
from django import forms
from .models import Organization, Department, Job, Employee, OrgMember

class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = "__all__"

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class OrgMemberForm(forms.ModelForm):
    class Meta:
        model = OrgMember
        fields = '__all__'