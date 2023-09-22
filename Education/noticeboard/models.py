from django.db import models
from accounts.models import User

# Create your models here.

class NoticeBoard(models.Model):
    name_of_organisation = models.CharField(max_length=50)
    date = models.DateField()
    title = models.CharField(max_length=50)
    notice_text = models.CharField(max_length=50)
    name = models.CharField(max_length=1000)
    designation = models.CharField(max_length=50)
    enteredBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
