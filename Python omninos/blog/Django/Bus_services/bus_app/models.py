from django.db import models

# Create your models here.
class Position(models.Model):
    title=models.CharField(max_length=20)
    
    def __str__(self):
        return self.title
    


class Bus(models.Model):
    passenger_name=models.CharField(max_length=20)
    passenger_id=models.CharField(max_length=20)
    bus_name=models.ForeignKey(Position,on_delete=models.CASCADE,null=True)
    where=models.CharField(max_length=50)
    to=models.CharField(max_length=30)
    