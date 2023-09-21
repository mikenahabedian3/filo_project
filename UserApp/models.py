# filo_project/UserApp/models.py 


from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ROLE_CHOICES = [
        ('ADMIN', 'Admin'),
        ('HR', 'Talent Acquisition/HR'),
        ('JOB_SEEKER', 'Job Seeker')
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

class UniqueLink(models.Model):
    token = models.CharField(max_length=100, unique=True)
    is_used = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
