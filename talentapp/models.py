from django.db import models
import uuid

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

class Candidate(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    resume = models.TextField()
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Interviewed', 'Interviewed'),
        ('Rejected', 'Rejected'),
        ('Hired', 'Hired'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Applied')

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    source = models.TextField()
    date_applied = models.DateTimeField(auto_now_add=True)
    review = models.TextField(blank=True)
    is_hired = models.BooleanField(default=False)

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

class Token(models.Model):
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    is_used = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.token)
