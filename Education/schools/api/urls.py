from django.urls import include, path
from . import views
# from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('school',views.school_list_view, name="school_list_view"),
    path('school/<slug:slug>',views.schools_detail_view, name="school_detail_view"),
    # path('api-token-auth/', obtain_auth_token, name='api_token_auth'),    
]