from django.forms import ModelForm
from .models import salary_data,query


class SalaryDataForm(ModelForm):
    class Meta:
        model = salary_data
        fields = ['experience','job_location','score','subject','salary']

class QueryDataForm(ModelForm):
    class Meta:
        model = query
        fields =  ['experience','job_location','score','subject']