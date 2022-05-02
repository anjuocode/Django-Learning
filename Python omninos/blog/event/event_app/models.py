from multiprocessing import Event
from tokenize import Name
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE


# Create your models here.
#family
class Family(models.Model):
    Event_type=models.CharField(max_length=100)
    Desc=models.TextField(max_length=1000)
    Image=models.ImageField(upload_to="Family_images")
    Food=models.CharField(max_length=100)
    Decorations=models.CharField(max_length=1000)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default="")
#charity
class Charity(models.Model):
    Event_type=models.CharField(max_length=100)
    Desc=models.TextField(max_length=1000)
    Image=models.ImageField(upload_to="Family_images")
    Food=models.CharField(max_length=100)
    Decorations=models.CharField(max_length=1000)
    CG=models.CharField(max_length=1000)
    Sponcer=models.CharField(max_length=1000)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default="")
    
#business
class Business(models.Model):
    Event_type=models.CharField(max_length=100)
    Desc=models.TextField(max_length=1000)
    Image=models.ImageField(upload_to="Family_images")
    Food=models.CharField(max_length=100)
    Publicity=models.CharField(max_length=1000)

#culture
class Culture(models.Model):
    Event_type=models.CharField(max_length=100)
    Desc=models.TextField(max_length=1000)
    Image=models.ImageField(upload_to="Family_images")
    Food=models.CharField(max_length=100)
    CG=models.CharField(max_length=1000)
    user=models.ForeignKey(User,on_delete=models.CASCADE,default="")
#Book
class Bookevent(models.Model):
    Name=models.CharField(max_length=100)
    Mobile=models.CharField(max_length=12)
    Location=models.CharField(max_length=100)
    Email=models.EmailField(default="")
    People=models.IntegerField(default="")
    Date=models.DateField()
    Event=models.CharField(max_length=100)
    Food=models.CharField(max_length=100)
    Address=models.CharField(max_length=400)
    Message=models.CharField(max_length=400)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.Event
#Contact_us
class Contact_us(models.Model):
    Name=models.CharField(max_length=100)
    Mobile=models.CharField(max_length=12)
    Email=models.CharField(max_length=50)
    Message=models.TextField(max_length=1400)



    