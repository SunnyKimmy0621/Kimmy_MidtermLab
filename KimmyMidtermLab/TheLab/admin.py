from django.contrib import admin
from .models import Department, Job, Organization, Employee, OrgMember

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name', 'created_at', 'updated_at')
    search_fields = ('department_name',)
    list_filter = ('created_at',)

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('job_name', 'department')
    search_fields = ('job_name', 'department__department_name')
    list_filter = ('department',)

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'description')
    search_fields = ('name', 'description')
    list_filter = ('department',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("employee_id", "lastname","firstname", "middlename",)
    search_fields = ("lastname", "firstname",)

@admin.register(OrgMember)
class OrgMemberAdmin(admin.ModelAdmin):
    list_display = ("employee", "organization", "get_member_program", "date_joined",)
    search_fields = ("employee__lastname", "employee__firstname",)

    def get_member_program(self, obj):
        return obj.employee.job if obj.employee else None
    get_member_program.short_description = "Job"


