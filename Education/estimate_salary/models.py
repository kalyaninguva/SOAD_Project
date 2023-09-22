from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class salary_data(models.Model):
    experience = models.IntegerField(null=False)
    job_location = models.CharField(null=False,max_length=15)
    score = models.IntegerField(null=False)
    subject = models.CharField(null=False,max_length=15)
    salary = models.IntegerField(null=False)

class query(models.Model):
    experience = models.IntegerField(null=False)
    job_location = models.CharField(null=False,max_length=15)
    score = models.IntegerField(null=False)
    subject = models.CharField(null=False,max_length=15)
    