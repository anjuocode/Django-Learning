from django.db import models

# Create your models here.
class student(models.Model):
    roll_no=models.CharField(max_length=10)
    name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    branch=models.CharField(max_length=20)
     

