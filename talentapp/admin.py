# filo_project/talentapp/admin.py

from django.contrib import admin
from .models import ParentOrganization, Company, JobRequisition

class CompanyInline(admin.StackedInline):  # Define Inline for Company model
    model = Company
    extra = 1  # Number of empty forms to display

@admin.register(ParentOrganization)
class ParentOrganizationAdmin(admin.ModelAdmin):
    list_display = ['name', 'user']
    inlines = [CompanyInline]  # Add CompanyInline to the ParentOrganizationAdmin

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent_organization']

@admin.register(JobRequisition)
class JobRequisitionAdmin(admin.ModelAdmin):
    list_display = ['title', 'company']
