from django.contrib import admin
from .models import Department, Job, Organization, Employee, OrgMember

admin.site.register(Department)
admin.site.register(Job)
admin.site.register(Organization)

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


