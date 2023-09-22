from django.test import SimpleTestCase,TestCase,Client
from django.urls import reverse,resolve
from estimate_salary.views import estimatesalary
from estimate_salary.api.views import salary_list_view,salary_detail_view,salary_detail_view_delete,salary_detail_view_get,salary_detail_view_put,get_estimates_view
from estimate_salary.models import salary_data,query
import json
class TestModels(TestCase):

    def setUp(self):
        self.p1 = salary_data.objects.create(
            id=1,
            experience= 41,
            job_location= "urban",
            score= 69,
            subject= "English",
            salary=47859
        )

    def instance_created(self):
        self.assertEquals(self.p1.id,1)   
