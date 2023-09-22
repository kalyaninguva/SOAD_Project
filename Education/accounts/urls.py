from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/',views.register,name = 'register'),
    path('student_register/',views.student_register,name = 'student_register'),
    path('administrator_register/',views.administrator_register,name = 'administrator_register'),    
    path('login/',views.loginView,name = 'login'),
    path('logout/',views.logoutView,name = 'logout'),
    path('view_profile/',views.view_profile,name = 'view_profile'),
    path('edit_profile/',views.edit_profile,name = 'edit_profile'),
    # path('',include('mainapp.urls')),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_URL)