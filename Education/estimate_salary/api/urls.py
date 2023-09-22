from django.urls import include, path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('salarydata',views.salary_list_view, name="salary_list_view"),
    path('getestimates',views.get_estimates_view,name="get_estimates_view"),
    path('salarydata/<slug:slug>',views.salary_detail_view, name="salary_detail_view"),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),    
]