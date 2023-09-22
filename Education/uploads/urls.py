from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('upload', views.uploads, name='Upload'),
    path('search/', views.searchnotes, name='Search'),
    path('files/', views.myfiles, name='Files'),
    path('files/media/files/notes/<int:pk>/',
         views.delete_notes, name='delete_notes'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
