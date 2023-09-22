from django import forms
from django.forms import ModelForm

from uploads.models import Upload_Notes


class PostForm(ModelForm):
    class Meta:
        model = Upload_Notes
        fields = ['first_name', 'last_name', 'subject', 'school_name',
                  'remarks', 'date', 'notes_file','file_url']
