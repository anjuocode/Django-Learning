from django.db import models

# Create your models here.
class Position(models.Model):
    title=models.CharField(max_length=20)
    def __str__(self):
        return self.title
class Shop(models.Model):
    name=models.CharField(max_length=20)
    services=models.ForeignKey(Position,on_delete=models.CASCADE,null=True)

