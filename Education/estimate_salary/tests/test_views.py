from django.test import SimpleTestCase,TestCase,Client
from django.urls import reverse,resolve
from estimate_salary.views import estimatesalary
from estimate_salary.api.views import salary_list_view,salary_detail_view,salary_detail_view_delete,salary_detail_view_get,salary_detail_view_put,get_estimates_view
from estimate_salary.models import salary_data,query
import json

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_url = reverse('salary_list_view')
        self.detail_url = reverse('salary_detail_view',args = ['1'])
        self.estimate_url = reverse('get_estimates_view')
        self.p1 = salary_data.objects.create(
            id=1,
            experience= 41,
            job_location= "urban",
            score= 69,
            subject= "English",
            salary=47859
        )

    def test_salarylist_GET(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code,200)
    
    def test_salarydetail_GET(self):
        response = self.client.get(self.detail_url)
        self.assertEquals(response.status_code,200)

    def test_salarylist_POST(self):
        response = self.client.post(self.list_url,{
            "experience": 15,
            "job_location": "urban",
            "score": 66,
            "subject": "Mathematics",
            "salary": 240504

        })
        self.assertEquals(response.status_code,200)

    def test_estimatesalary_POST(self):
        response = self.client.post(self.estimate_url,{
            "experience": 15,
            "job_location": "urban",
            "score": 66,
            "subject": "Mathematics",
            "salary": 240504

        })
        self.assertEquals(response.status_code,200)
    
    def test_salarylist_delete(self):
        salary_data.objects.create(
            id=6,
            experience= 41,
            job_location= "semi-urban",
            score= 70,
            subject= "English",
            salary=90000
        )
        response = self.client.delete(self.list_url,json.dumps({
            'id':6
        }))
        self.assertEquals(response.status_code,405)


        

