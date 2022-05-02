from django.db import models
from django.db.models.base import Model

# Create your models here.

class student(models.Model):
    name=models.CharField(max_length=20)
    father=models.CharField(max_length=20)