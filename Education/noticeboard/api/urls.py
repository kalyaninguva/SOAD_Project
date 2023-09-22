from django.urls import include, path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('noticeboarddata',views.noticeboard_view, name="noticeboard_view"),
    path('noticeboarddata/<slug:slug>',views.noticeboard_detail_view, name="noticeboard_detail_view"),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),    
]