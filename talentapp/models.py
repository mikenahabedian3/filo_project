from django.db import models
from UserApp.models import Candidate

class ParentOrganization(models.Model):
    name = models.CharField(max_length=255)

class Company(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    parent_organization = models.ForeignKey(ParentOrganization, on_delete=models.CASCADE)

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    source = models.TextField()
    date_applied = models.DateTimeField(auto_now_add=True)
    review = models.TextField(blank=True)
    is_hired = models.BooleanField(default=False)
