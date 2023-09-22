from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_administrator = models.BooleanField(default=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    age = models.IntegerField(null=True,blank=True)
    gender = models.CharField(max_length=10,null=True,blank=True)
    phone_no = models.CharField(max_length=20,null=True,blank=True)
    school_name = models.CharField(max_length=50,null=True,blank=True)
    standard = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.user.username

class Administrator(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    phone_no = models.CharField(max_length=20,null=True,blank=True)
    school_name  = models.CharField(max_length=50,null=True,blank=True)
    upload = models.FileField(upload_to='files/certificates', default="Unnamed File")
    established_year = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.user.username