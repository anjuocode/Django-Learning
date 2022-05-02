from django.db import models

# Create your models here.
class Try(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    branch=models.CharField(max_length=30)