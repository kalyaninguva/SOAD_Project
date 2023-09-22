from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('accounts.urls')),
    path('',include('uploads.urls')),
    path('',include('payments.urls')),
    path('',include('estimate_salary.urls')),
    path('',views.homeView,name = 'home'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_URL)