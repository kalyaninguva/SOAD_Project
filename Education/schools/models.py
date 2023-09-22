from django.db import models
from accounts.models import User
# from django.contrib.auth.models import User

# Create your models here.

class SchoolData(models.Model):
    location = models.CharField(max_length=50)
    sid = models.IntegerField()
    name = models.CharField(max_length=60)
    strength = models.IntegerField()
    typeOfSchool = models.CharField(max_length=50)
    adress = models.CharField(max_length=100)
    achievements = models.CharField(max_length=50)
    capacity = models.IntegerField()
    contactInfo = models.IntegerField()
    enteredBy = models.ForeignKey(User,on_delete=models.SET_NULL,null = True)