from django.test import SimpleTestCase
from django.urls import reverse,resolve
from estimate_salary.views import estimatesalary
from estimate_salary.api.views import salary_list_view,salary_detail_view,salary_detail_view_delete,salary_detail_view_get,salary_detail_view_put,get_estimates_view

class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('estimatesalary')
        print(resolve(url))
        self.assertEquals(resolve(url).func,estimatesalary) 
    def test_api_url_resolved(self):
        url = reverse('salary_list_view')
        print(resolve(url))
        self.assertEquals(resolve(url).func,salary_list_view)
    def test_api_url_getestimates(self):
        url = reverse('get_estimates_view')
        print(resolve(url))
        self.assertEquals(resolve(url).func,get_estimates_view)
    def test_api_url_dataview(self):
        url = reverse('salary_detail_view',args=['some-slug'])
        print(resolve(url))
        self.assertEquals(resolve(url).func,salary_detail_view)