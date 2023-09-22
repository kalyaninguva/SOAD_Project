from django.contrib import admin
from .models import User,Student,Administrator
# Register your models here.

admin.site.register(User)
admin.site.register(Administrator)
admin.site.register(Student)
