from django.test import SimpleTestCase
from django.urls import reverse,resolve
from schools.views import postSchool,schoolsList,getSchoolbyId,updateSchool,deleteSchool

class TestUrls(SimpleTestCase):

    def test_post_url_is_resolved(self):
        url = reverse('post_school')
        print(resolve(url))
        self.assertEquals(resolve(url).func,postSchool)

    def test_list_url_is_resolved(self):
        url = reverse('schools_list')
        print(resolve(url))
        self.assertEquals(resolve(url).func,schoolsList)

    def test_getid_url_is_resolved(self):
        url = reverse('get_school')
        print(resolve(url))
        self.assertEquals(resolve(url).func,getSchoolbyId)

    def test_update_url_is_resolved(self):
        url = reverse('update_school')
        print(resolve(url))
        self.assertEquals(resolve(url).func,updateSchool)

    def test_delete_url_is_resolved(self):
        url = reverse('delete_school')
        print(resolve(url))
        self.assertEquals(resolve(url).func,deleteSchool)