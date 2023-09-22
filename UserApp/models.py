# filo_project/UserApp/models.py 


from django.db import models
from django.contrib.auth.models import User
import uuid

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20)

class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resume = models.TextField()
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Interviewed', 'Interviewed'),
        ('Rejected', 'Rejected'),
        ('Hired', 'Hired'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Applied')

class Token(models.Model):
    token = models.UUIDField(default=uuid.uuid4, unique=True)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    is_used = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
