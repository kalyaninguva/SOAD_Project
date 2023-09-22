from django.urls import path,include
from . import views

urlpatterns = [
    path('api/', include('schools.api.urls')),
    path('',include('mainapp.urls')),
    path('newSchool',views.postSchool,name = 'post_school'),
    path('results',views.schoolsList,name = 'schools_list'),
    path('getschool',views.getSchoolbyId,name = 'get_school'),
    path('updateschool',views.updateSchool,name = 'update_school'),
    path('deleteschool',views.deleteSchool,name = 'delete_school'),
]
