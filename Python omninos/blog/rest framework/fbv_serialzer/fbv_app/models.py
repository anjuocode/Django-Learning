from django.db import models

# Create your models here.
class Student(models.Model):
    Id=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=30)
    Marks=models.IntegerField()
    def __str__(self) :
        return self.Name