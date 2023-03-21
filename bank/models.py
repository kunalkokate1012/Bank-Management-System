from django.db import models

# Create your models here.
class User(models.Model):
    id=models.AutoField
    name=models.CharField(max_length=50,default="")
    email=models.CharField(max_length=100,default="")
    balance=models.IntegerField(default=0)
class Transiction(models.Model):
    id=models.AutoField
    from_user=models.CharField(max_length=50,default=0)
    to_user=models.CharField(max_length=50,default=0)
    ammount=models.IntegerField(default=0)
    date=models.DateField(default=2021-1-1)