from django import forms
from .models import SchoolData

class schoolsForm(forms.ModelForm):
    class Meta:
        model = SchoolData
        fields = ['location','typeOfSchool']

class addSchool(forms.ModelForm):
    class Meta:
        model = SchoolData
        fields = ['location','sid','name','strength','typeOfSchool','adress','achievements','capacity','contactInfo','enteredBy']

class getSchool(forms.ModelForm):
    class Meta:
        model = SchoolData
        fields = ['sid']
