from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .forms import StudentSignUpForm,AdministratorSignUpForm,EditAdministratorProfileForm,EditStudentProfileForm
from django.http import HttpResponse
from .models import User,Student,Administrator
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def register(request):
    return render(request,'accounts/register.html')

def student_register(request):
    uservalue = ""
    passwordvalue1 = ""
    passwordvalue2 = ""
    form = StudentSignUpForm(request.POST)   
    if request.method == 'POST':
        print(request.POST)
        if form.is_valid():
            print("It is a valid Form")
            uservalue = form.cleaned_data.get('username')
            passwordvalue1= form.cleaned_data.get("password1")
            passwordvalue2= form.cleaned_data.get("password2")
            if passwordvalue1 == passwordvalue2:
                try:
                    user= User.objects.get(username=uservalue)
                    context= {'form': form, 'error':'The username you entered has already been taken. Please try another username.'}
                    return render(request, 'accounts/student_register.html', context)
                except :
                    user= User.objects.create_user(username = uservalue, password= passwordvalue1)
                    user.first_name = form.cleaned_data['first_name']
                    user.last_name = form.cleaned_data['last_name']
                    user.email = form.cleaned_data['email']
                    user.is_student = True
                    user.save()
                    form.data_save(user)
                    return redirect('login')
            else:
                context= {'form': form, 'error':'The passwords that you provided don\'t match'}
                return render(request, 'accounts/register.html', context)
        else:
            return redirect('student_register')
    else:
        context= {'form': form}
        return render(request, 'accounts/student_register.html', context)

def administrator_register(request):
    uservalue = ""
    passwordvalue1 = ""
    passwordvalue2 = ""
    form = AdministratorSignUpForm(request.POST)   
    if request.method == 'POST':
        if form.is_valid():
            print("Form is valid")
            uservalue = form.cleaned_data.get('username')
            passwordvalue1= form.cleaned_data.get("password1")
            passwordvalue2= form.cleaned_data.get("password2")
            if passwordvalue1 == passwordvalue2:
                try:
                    user= User.objects.get(username=uservalue)
                    # context= {'form': form, 'error':'Invalid Email Adress'}
                    # return render(request, 'accounts/student_register.html', context)
                    return HttpResponse('User Name has already taken')
                except :
                    user= User.objects.create_user(username = uservalue, password= passwordvalue1)
                    user.first_name = form.cleaned_data['first_name']
                    user.last_name = form.cleaned_data['last_name']
                    user.email = form.cleaned_data['email']
                    user.is_administrator = True
                    user.save()
                    form.data_save(user)
                    return redirect('login')
            else:
                # context= {'form': form, 'error':'The passwords that you provided don\'t match'}
                # return render(request, 'accounts/register.html', context)
                return HttpResponse('Passwords doesn not matched')
        else:
            # return redirect('student_register')
            print(request.POST)
            print(form.cleaned_data)
            return HttpResponse('Form is not Valid')
    else:
        context= {'form': form}
        return render(request, 'accounts/administrator_register.html', context)

def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('home')
            else:
                return redirect('login')
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            # messages.error(request, 'Invalid Credentials Given..!!') 
            return redirect('login')
    else:
        return render(request, 'accounts/login.html', {})

def logoutView(request):
    logout(request)
    return redirect('home')

def view_profile(request):
    if not request.user.is_authenticated:
	    return HttpResponse('You are not logged in!')
    user = User.objects.get(username = request.user.username)
    # print(user.is_student)
    if user.is_student:
        is_student = True
        print('I am a Student')
        student = Student.objects.get(user = user)
        return render(request, 'accounts/profile.html', {'user':user, 'is_student':is_student,'student':student})
    else:
        is_student = False
        administrator = Administrator.objects.get(user=user)
        print(is_student)
        print(user)
        return render(request, 'accounts/profile.html', {'user':user, 'is_student':is_student,'administrator':administrator})

def edit_profile(request):
    if not request.user.is_authenticated:
        return HttpResponse('You are not logged in')
    user = User.objects.get(username = request.user.username)
    if request.method == 'POST':
        form = EditStudentProfileForm(request.POST)
        if user.is_student:
            is_student = True
            if form.is_valid():
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.email = form.cleaned_data['email']
                student = Student.objects.get(user = user)
                student.phone_no = form.cleaned_data.get('phone_no')
                student.school_name = form.cleaned_data.get('school_name')
                student.standard = form.cleaned_data.get('standard')
                student.save()
                return render(request, 'accounts/profile.html', {'user':user, 'is_student':is_student,'student':student})
        elif user.is_administrator:
            is_administrator = True
            form = EditAdministratorProfileForm(request.POST)
            if form.is_valid():
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.email = form.cleaned_data['email']
                administrator = Administrator.objects.get(user=user)
                administrator.phone_no = form.cleaned_data.get('phone_no')
                administrator.school_name  = form.cleaned_data.get('school_name')
                administrator.upload = form.cleaned_data.get('upload')
                administrator.save()
                return render(request, 'accounts/profile.html', {'user':user, 'is_student':is_student,'student':student})

            

