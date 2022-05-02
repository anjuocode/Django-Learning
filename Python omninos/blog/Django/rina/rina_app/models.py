from django.db import models

# Create your models here.
class Rina(models.Model):
    heading=models.CharField(max_length=100)
    image=models.ImageField(upload_to="images")
    desc=models.CharField(max_length=1000)
    pub_date=models.DateField(auto_now_add=True)