from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User,Student,Administrator
from django.db import transaction
# from django.contrib.auth.forms import User

class StudentSignUpForm(forms.ModelForm):
    username = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    password1 = forms.CharField(label=("Password"),widget=forms.PasswordInput)
    password2 = forms.CharField(label=("Password"),widget=forms.PasswordInput)
    email = forms.EmailField(required=True)
    age = forms.IntegerField(required=True)
    gender = forms.CharField(required=True)
    phone_no = forms.IntegerField(required=True)
    standard = forms.IntegerField(required=True)
    school_name = forms.CharField(required=True)
    

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','age','gender','phone_no','standard','school_name','password1','password2')

    @transaction.atomic
    def data_save(self,user):
        student = Student.objects.create(user=user)
        student.age = self.cleaned_data.get('age')
        student.gender = self.cleaned_data.get('gender')
        student.phone_no = self.cleaned_data.get('phone_no')
        student.school_name = self.cleaned_data.get('school_name')
        student.standard = self.cleaned_data.get('standard')
        student.save()
        return user

class AdministratorSignUpForm(forms.ModelForm):
    username = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    password1 = forms.CharField(label=("Password"),widget=forms.PasswordInput)
    password2 = forms.CharField(label=("Confirm Password"),widget=forms.PasswordInput)
    email = forms.EmailField(required=True)
    phone_no = forms.CharField(required=True)
    school_name = forms.CharField(required=True)
    upload = forms.FileField(required=False)
    established_year = forms.IntegerField(required=True)

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2','phone_no','school_name','upload','established_year')

    @transaction.atomic
    def data_save(self,user):
        administrator = Administrator.objects.create(user=user)
        administrator.phone_no = self.cleaned_data.get('phone_no')
        administrator.school_name  = self.cleaned_data.get('school_name')
        administrator.upload = self.cleaned_data.get('upload')
        administrator.established_year = self.cleaned_data.get('established_year')
        administrator.save()
        return user

class LoginForm(forms.ModelForm):
    username = forms.CharField(required=True)
    password1 = forms.CharField(label=("Password"),widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username','password1')

class EditStudentProfileForm(forms.ModelForm):
    username = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone_no = forms.CharField(required=True)
    standard = forms.IntegerField(required=True)
    school_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','phone_no','standard','school_name')

class EditAdministratorProfileForm(forms.ModelForm):
    username = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone_no = forms.CharField(required=True)
    school_name = forms.CharField(required=True)
    upload = forms.FileField(required=False)

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','phone_no','school_name','upload')