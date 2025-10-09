from django.db import models

# Base model for common fields
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Department(BaseModel):
    department_name = models.CharField(max_length=150)

    def __str__(self):
        return self.department_name

class Job(BaseModel):
    job_name = models.CharField(max_length=150)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.job_name

class Organization(BaseModel):
    name = models.CharField(max_length=250)
    department = models.ForeignKey(Department, null=True, blank=True, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Employee(BaseModel):
    employee_id = models.CharField(max_length=15)
    lastname = models.CharField(max_length=25)
    firstname = models.CharField(max_length=25)
    middlename = models.CharField(max_length=25, blank=True, null=True)
    Job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.lastname}, {self.firstname}"

class OrgMember(BaseModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    date_joined = models.DateField()

    def __str__(self):
        return f"{self.employee} - {self.organization}"

