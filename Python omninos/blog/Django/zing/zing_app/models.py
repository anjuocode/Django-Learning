from django.db import models

# Create your models here.
class Zing(models.Model):
    name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    id=models.IntegerField(primary_key=True)
    branch=models.CharField(max_length=20)