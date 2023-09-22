from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from .forms import *
from .models import  *
from estimate_salary.api.views import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail, send_mass_mail
import datetime
import requests

def estimatesalary(request):
    if request.method=="POST":
        r = requests.post('http://127.0.0.1:8000/api/getestimates', data=request.POST)
        data = r.json()
        return render(request,'estimate_salary/response.html',{'data' : data})
    else:
        return render(request,'estimate_salary/estimate.html')


