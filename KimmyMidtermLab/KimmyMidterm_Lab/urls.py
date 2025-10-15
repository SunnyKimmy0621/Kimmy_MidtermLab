from django.contrib import admin
from django.urls import path
from django.urls import path, include
from TheLab.views import HomePageView, OrganizationList, OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView, DepartmentListView, DepartmentCreateView, DepartmentUpdateView, DepartmentDeleteView, JobListView, JobCreateView, JobUpdateView, JobDeleteView, EmployeeListView, EmployeeCreateView, EmployeeUpdateView, EmployeeDeleteView, OrgMemberListView, OrgMemberCreateView, OrgMemberUpdateView, OrgMemberDeleteView
from TheLab import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")), # allauth routes
    path('', include('TheLab.urls')),
    path('', views.HomePageView.as_view(), name='home'),

    #Organization URLs
    path('organization_list/', OrganizationList.as_view(), name='organization-list'), 
    path('organization_list/add/', OrganizationCreateView.as_view(), name='organization-add'),
    path('organization_list/<pk>/',OrganizationUpdateView.as_view(), name='organization-update'),
    path('organization_list/<pk>/delete/', OrganizationDeleteView.as_view(), name='organization-delete'),

    #Department URLs
    path('departments/', DepartmentListView.as_view(), name='department-list'),
    path('departments/add/', DepartmentCreateView.as_view(), name='department-add'),
    path('departments/<int:pk>/edit/', DepartmentUpdateView.as_view(), name='department-edit'),
    path('departments/<int:pk>/delete/', DepartmentDeleteView.as_view(), name='department-delete'),

    # Job URLs
    path('jobs/', JobListView.as_view(), name='job-list'),
    path('jobs/add/', JobCreateView.as_view(), name='job-add'),
    path('jobs/<int:pk>/edit/', JobUpdateView.as_view(), name='job-edit'),
    path('jobs/<int:pk>/delete', JobDeleteView.as_view(), name='job-delete'),

    # Employee URLs
    path('employees/', EmployeeListView.as_view(), name='employee-list'),
    path('employees/add/', EmployeeCreateView.as_view(), name='employee-add'),
    path('employees/<int:pk>/edit/', EmployeeUpdateView.as_view(), name='employee-edit'),
    path('employees/<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee-delete'),

    # OrgMember URLs
    path('orgmembers/', OrgMemberListView.as_view(), name='orgmember-list'),
    path('orgmembers/add/', OrgMemberCreateView.as_view(), name='orgmember-add'),
    path('orgmembers/<int:pk>/edit/', OrgMemberUpdateView.as_view(), name='orgmember-edit'),
    path('orgmembers/<int:pk>/delete/', OrgMemberDeleteView.as_view(), name='orgmember-delete'),
]

