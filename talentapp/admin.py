# filo_project/talentapp/admin.py

from django.contrib import admin
from .models import ParentOrganization, Company, Job, Application

admin.site.register(ParentOrganization)
admin.site.register(Company)
admin.site.register(Job)
admin.site.register(Application)
