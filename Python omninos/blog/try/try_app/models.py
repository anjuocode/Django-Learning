from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=50)
    img=models.ImageField(upload_to="images")
    desc=models.CharField(max_length=1500)
    pub_date=models.DateTimeField(auto_now_add=True)