from django.urls import path,include
from . import views

urlpatterns = [
    path('api/',include('estimate_salary.api.urls')),
    path('estimatesalary/',views.estimatesalary,name='estimatesalary')
]