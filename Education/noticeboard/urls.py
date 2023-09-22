from django.urls import include, path
from . import views

urlpatterns = [
    path('index',views.index_view, name="index_view"),
    path('api/', include('noticeboard.api.urls')),
    path('getNotices',views.noticeLists,name = 'notice_list'),
    path('noticeResults',views.notices,name = 'notice_results'),
]