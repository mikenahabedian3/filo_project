# filo_project/talentapp/models.py

from django.db import models
from django.contrib.auth.models import User

class ParentOrganization(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    # Other fields as needed
    # If you want to add more fields, you can do so here

class Company(models.Model):
    parent_organization = models.ForeignKey(ParentOrganization, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    # Other fields as needed
    # If you want to add more fields, you can do so here

class JobRequisition(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    # Other fields as needed
    # If you want to add more fields, you can do so here
