from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_heading=models.CharField(max_length=150)
    blog_image=models.ImageField(upload_to="blog_images")
    blog_desc=models.CharField(max_length=1000)
    pub_date=models.DateTimeField(auto_now_add=True)
    publisher_name=models.CharField(max_length=50)