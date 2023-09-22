from django.forms import ModelForm
from .models import NoticeBoard

class NoticeBoardDataForm(ModelForm):
    class Meta:
        model = NoticeBoard
        fields = ['name_of_organisation','date','title','notice_text','name','designation']

class Notices(ModelForm):
    class Meta:
        model = NoticeBoard
        fields = ['name_of_organisation']