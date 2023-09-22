from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import SchoolDataSerializer
from schools.models import SchoolData
from schools.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render,redirect

@api_view(http_method_names=['GET','POST'])
# @permission_classes([IsAuthenticated])
def school_list_view(request):
    if request.method == 'GET':
        return school_list_view_get(request)
    elif request.method == 'POST':
        return school_list_view_post(request)

def school_list_view_get(request):
    try:
        location = request.query_params.get('location','')
        typeOfSchool = request.query_params.get('typeOfSchool','')
        data = SchoolData.objects.filter(location__icontains=location,typeOfSchool__icontains=typeOfSchool)
        serializer = SchoolDataSerializer(data,many = True)  
        return Response(data=serializer.data)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

def school_list_view_post(request):
    user = User.objects.get(username = request.user.username)
    enteredBy = user
    sdata = SchoolData(enteredBy=enteredBy)
    serializer = SchoolDataSerializer(sdata,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=['GET','PUT','DELETE'])
def schools_detail_view(request,slug):
    try:
        sdata = SchoolData.objects.get(sid = slug)
        if request.method == 'GET':
            return schools_detail_view_get(request,slug,sdata)
        elif request.method == 'PUT':
            return schools_detail_view_put(request,slug,sdata)
        elif request.method == 'DELETE':
            return schools_detail_view_delete(request,slug,sdata)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

def schools_detail_view_get(request,slug,sdata):
    serializer = SchoolDataSerializer(sdata)
    return Response(serializer.data)

def schools_detail_view_put(request,slug,sdata):
    serializer = SchoolDataSerializer(sdata,data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

def schools_detail_view_delete(request,slug,sdata):
    delresult = sdata.delete()
    data = {'message' : 'error during deletion'}
    if delresult[0]==1:
        data = {'message' : 'Successfully Deleted'}
    return Response(data)