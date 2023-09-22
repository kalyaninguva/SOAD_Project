from django.test import SimpleTestCase
from schools.forms import schoolsForm,addSchool,getSchool

class TestForms(SimpleTestCase):

    def test_schools_form_valid_data(self):
        form = schoolsForm(data={
                "location": "Bombay",
                "sid": 10101,
                "name": "BrainTech",
                "strength": 30000,
                "typeOfSchool": "Primary",
                "adress": "MGBS",
                "achievements": "Top School",
                "capacity": 2000,
                "contactInfo": 121176321,
                "enteredBy": "Nithish"
        })

        self.assertTrue(form.is_valid())

        def test_schools_form_no_data(self):
            form = schoolsForm(data={})

            self.assertFalse(form.is_valid())
            self.assertEquals(len(form.errors),10)

