from django.db import models
from django.db.models.fields import IntegerField
from django.db.models.fields.files import ImageField

# Create your models here.
class Practice(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to="images")
    age=models.IntegerField(primary_key=True)