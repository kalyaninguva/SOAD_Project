from django.test import SimpleTestCase
from estimate_salary.forms import SalaryDataForm,QueryDataForm

def TestForms(SimpleTestCase):

    def salary_data_form(self):
        form = SalaryDataForm(data = {
            'experience': 41,
            'job_location': "urban",
            'score': 69,
            'subject': "English",
            'salary':47859
        })
        self.assertTrue(form.is_valid())
    
    def query_data_form(self):
        form = SalaryDataForm(data={})

        self.assertFalse(form.is_valid())
