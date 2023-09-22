from django.contrib import admin
from django.urls import path
from payments import views
urlpatterns = [
    path('findSchools/',views.home,name = 'payment_home'),
    path('paynow/', views.paynow),
    path('payment/', views.payment, name="payment"),
    path('response/', views.response,name='response'),
    path('findschool/', views.findschool, name="findschool"),
    path('filldetails/', views.filldetails, name="filldetails"),
]