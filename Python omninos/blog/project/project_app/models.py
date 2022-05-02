from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Project(models.Model):
    heading=models.CharField(max_length=20)
    image=models.ImageField(upload_to="images")
    desc=models.CharField(max_length=1000)
    pub_date=models.DateTimeField(auto_now_add=True)