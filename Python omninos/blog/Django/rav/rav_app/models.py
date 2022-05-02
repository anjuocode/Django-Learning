from django.db import models

# Create your models here.
class Position(models.Model):
    title=models.CharField(max_length=20)
    def __str__(self):
        return self.title
    


class Rav(models.Model):
    name=models.CharField(max_length=20)
    salary=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    branch=models.CharField(max_length=30)
    position=models.ForeignKey(Position,on_delete=models.CASCADE,null=True)