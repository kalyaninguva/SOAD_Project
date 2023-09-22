from django.db import models

# Create your models here.
from accounts.models import User
from django.db import models
from django.utils import timezone

#model for files


class Upload_Notes(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    first_name = models.CharField(max_length=25, blank=False, null=False)
    last_name = models.CharField(max_length=25, blank=False, null=False)
    subject = models.CharField(max_length=25, blank=False, null=False)
    school_name = models.CharField(max_length=50, blank=False, null=False)
    remarks = models.CharField(max_length=50, blank=False, null=False)
    date = models.DateField(default=timezone.now)
    notes_file = models.FileField(
        upload_to='files/notes', default="Unnamed File")
    file_url = models.CharField(max_length=100, blank=True, null=True)

    # def delete(self, *args, **kwargs):
    #     self.notes_file.delete()
    #     super().delete(*args, **kwargs)

    def delete_not_file(self, *args, **kwargs):
        super().delete(*args, **kwargs)
