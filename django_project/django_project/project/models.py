from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ToDo(models.Model):
    PRIORITY_CHOICES = [
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
        ('C', 'Cricital')
    ]
    title = models.CharField(max_length=30)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
