from django.contrib import admin
from .models import ParentOrganization, Company, Job, Candidate, Application, User, Token

admin.site.register(ParentOrganization)
admin.site.register(Company)
admin.site.register(Job)
admin.site.register(Candidate)
admin.site.register(Application)
admin.site.register(User)
admin.site.register(Token)
