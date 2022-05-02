from django.db import models

# Create your models here.


# Create your models

# Create your models here.
class Position(models.Model):
    title=models.CharField(max_length=20)
    
    def __str__(self):
        return self.title
    


class Library(models.Model):
    stu_id=models.IntegerField(primary_key=True)
    stu_name=models.CharField(max_length=60)
    Book_name=models.ForeignKey(Position,on_delete=models.CASCADE,null=True)
    issue_date=models.DateTimeField(auto_now_add=True)
    return_date=models.DateTimeField(auto_now_add=True)
    