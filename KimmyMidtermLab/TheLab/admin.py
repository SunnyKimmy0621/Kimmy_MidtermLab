from django.contrib import admin
from .models import College, Program, Organization, Student, OrgMember

admin.site.register(College)
admin.site.register(Program)
admin.site.register(Organization)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "lastname","firstname", "middlename", "program")
    search_fields = ("lastname", "firstname",)

@admin.register(OrgMember)
class OrgMemberAdmin(admin.ModelAdmin):
    list_display = ("student", "organization", "get_member_program", "date_joined",)
    search_fields = ("student__lastname", "student__firstname",)

    def get_member_program(self, obj):
        # Access the student's program directly
        return obj.student.program if obj.student else None
    get_member_program.short_description = "Program"

