from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import NoticeBoardDataForm,Notices
from noticeboard.models import NoticeBoard
import requests
from requests.exceptions import RequestException

# @login_required(login_url='login_view')
def index_view(request):
    form = Notices(request.POST)
    data = NoticeBoard.objects.all()
    if request.method == 'POST':
        form = NoticeBoardDataForm(request.POST)
        if form.is_valid():
            hdata = form.save(commit=False)
            hdata.enteredBy = request.user
            hdata.save()
            return render(request,'noticeboard/index.html',{'data':data})
    return render(request,'noticeboard/index.html')

def noticeLists(request):
    data = NoticeBoard.objects.all()
    return render(request,'noticeboard/index.html',{'data':data})

def notices(request):
    form = Notices(request.POST)
    if request.method == "POST":
        if form.is_valid():
            name_of_organisation = form.cleaned_data['name_of_organisation']
            print(name_of_organisation)
            r = requests.get('http://127.0.0.1:8000/api/noticeboarddata?name_of_organisation=' + name_of_organisation)
            data = r.json()
            print(data)
            return render(request,'noticeboard/index.html',{'data':data})
    else:
        return render(request,'noticeboard/notices.html',{'form':form})