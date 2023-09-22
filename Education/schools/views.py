from django.shortcuts import render,redirect
from .forms import schoolsForm,addSchool,getSchool
from .models import SchoolData
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import requests
import json
# Create your views here.

def schoolsList(request):
    form = schoolsForm(request.POST)
    if request.method=="POST":
        if form.is_valid():
            location = form.cleaned_data['location']
            typeOfSchool = form.cleaned_data['typeOfSchool']
            r = requests.get('http://127.0.0.1:8000/api/school?location=' + location + '&typeOfSchool='+ typeOfSchool,auth = ('Nithish','nithish@123'))
            print(type(r))
            print(r)
            data = r.json()
            return render(request,'schools/results.html',{'data' : data})
    else:
        return render(request,'schools/schools.html')

# @login_required(login_url='login_view')
def postSchool(request):
    form = addSchool(request.POST)
    print(request.POST)
    if request.method=="POST":
        if form.is_valid():
            print('Form is Valid')
            r = requests.post('http://127.0.0.1:8000/api/school',data = request.POST)
            return HttpResponse('Posted Successfully')
        else:
            print("Not Valid")
    else:
        return render(request,'schools/schoolEntry.html',{'form' : form})

@login_required(login_url='login_view')
def getSchoolbyId(request):
    form = getSchool(request.POST)
    if request.method=="POST":
        if form.is_valid():
            id = form.cleaned_data['sid']
            r = requests.get('http://127.0.0.1:8000/api/school/'+str(id))
            school = r.json()
            data = []
            data.append(school)
            return render(request,'schools/results.html',{'data' : data})
    else:
        return render(request,'schools/getid.html')

def updateSchool(request):
    form = getSchool(request.POST)
    if request.method=="POST":
        if form.is_valid():
            id = form.cleaned_data['sid']
            print(type(id))
            print('http://127.0.0.1:8000/api/school/'+str(id))
            r = requests.put('http://127.0.0.1:8000/api/school/'+str(id),data = request.POST)
            school = r.json()
            data = []
            data.append(school)
            return render(request,'schools/results.html',{'data' : data})
    else:
        data = SchoolData.objects.get(sid = 10101)
        return render(request,'schools/getid.html',{'data' : data})

def deleteSchool(request):
    form = getSchool(request.POST)
    if request.method=="POST":
        if form.is_valid():
            id = form.cleaned_data['sid']
            r = requests.delete('http://127.0.0.1:8000/api/school/'+str(id))
            return HttpResponse('Deleted Successfully')
    else:
        return render(request,'schools/getid.html',{'form' : form})