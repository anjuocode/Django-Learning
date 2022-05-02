from django.db import models

# Create your models here.
class Flights(models.Model):
    Name=models.CharField(max_length=30)
    Mobile=models.IntegerField()
    From=models.CharField(max_length=100)
    To=models.CharField(max_length=100)
    Departure=models.DateField()
    Return=models.DateField()
    
    
