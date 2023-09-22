from .models import Locality,Person
from django import forms
class LocalityForm(forms.ModelForm):
    class Meta:
        model=Locality
        fields=['Locality','schoolname']

        


class PersonForm(forms.ModelForm):
    class Meta:
        model=Person
        fields=['first_name','last_name','youremail','phonenumber','classandsection','guardian_name','fee_type','amount']        
        
      
