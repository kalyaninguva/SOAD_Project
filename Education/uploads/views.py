from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from uploads.forms import PostForm
from .models import Upload_Notes
from django.contrib.auth.decorators import login_required
import requests

@login_required
def uploads(request):
    if request.method == 'POST':
        print(request.POST)
        details = PostForm(request.POST, request.FILES)
        details.instance.author = request.user
        if details.is_valid():
            post = details.save(commit=False)
            post.save()
            url = 'https://safenote.co/api/file'
            f = "."+ post.notes_file.url
            myfiles = {'file': open(f, 'rb')}
            data = {'lifetime':100,'read_count':10}
            x = requests.post(url, files=myfiles,data=data)
            x = x.text
            x = x.split(",")[-1]
            x = x[8:-2]
            post.file_url = x
            post.save()
            print(post.file_url)
            return redirect('Upload')
        else:
            return HttpResponse("Form is wrongly filled!")
    else:
        return render(request, 'uploads/upload.html')

@login_required
def myfiles(request):
    notes = Upload_Notes.objects.filter(author=request.user)
    context = {
        'notes': notes,
    }
    return render(request, 'uploads/myfiles.html', context)

@login_required
def searchnotes(request):
    notes = Upload_Notes.objects.filter()
    first_name_query = request.GET.get('first_name')
    last_name_query = request.GET.get('last_name')
    school_name_query = request.GET.get('school_name') 
    subject_query = request.GET.get('subject')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')

    if first_name_query != '' and first_name_query is not None:
        notes = notes.filter(
            first_name__icontains=first_name_query)

    if last_name_query != '' and last_name_query is not None:
        notes = notes.filter(
            last_name__icontains=last_name_query)

    if school_name_query != '' and school_name_query is not None:
        notes = notes.filter(
            school_name__icontains=school_name_query)
    
    if subject_query != '' and subject_query is not None:
        notes = notes.filter(
            subject__icontains=subject_query)

    if date_min != '' and date_min is not None:
        notes = notes.filter(date__gte=date_min)

    if date_max != '' and date_max is not None:
        notes = notes.filter(date__lt=date_max)
    context = {
        'notes': notes,
    }
    return render(request, 'uploads/search.html', context)


@login_required
def delete_notes(request, pk):
    if request.method == 'POST':
        file = Upload_Notes.objects.get(id=pk)
        file.delete()
    return redirect('Files')