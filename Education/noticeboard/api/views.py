from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from noticeboard.models import NoticeBoard
from .serializers import NoticeBoardSerializer
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

@api_view(http_method_names=['GET','POST',])
# @permission_classes([IsAuthenticated])
def noticeboard_view(request):
    if request.method == 'GET':
        return noticeboard_view_get(request)
    elif request.method == 'POST':
        return noticeboard_view_post(request)

def noticeboard_view_get(request):
    try:
        name_of_organisation = request.query_params.get('name_of_organisation','')
        data = NoticeBoard.objects.filter(name_of_organisation__icontains=name_of_organisation)
        serializer = NoticeBoardSerializer(data,many=True)
        return Response(data=serializer.data)
    except ObjectDoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

def noticeboard_view_post(request):
    enteredBy = request.user
    hdata = NoticeBoard(enteredBy=enteredBy)
    serializer = NoticeBoardSerializer(hdata, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=['GET','PUT','DELETE'])
def noticeboard_detail_view(request, slug):
    print(slug)
    try:
        hdata = NoticeBoard.objects.get(name_of_organisation=slug)
        print(hdata)
        if request.method == 'GET':
            return noticeboard_detail_view_get(request, slug, hdata)
        elif request.method == 'PUT':
            return noticeboard_detail_view_put(request, slug, hdata)
        elif request.method == 'DELETE':
            return noticeboard_detail_view_delete(request, slug, hdata)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

def noticeboard_detail_view_get(request, slug, hdata):
    print("In get")
    serializer = NoticeBoardSerializer(hdata)
    print(serializer.data)
    return Response(serializer.data)

def noticeboard_detail_view_put(request, slug, hdata):
    serializer = NoticeBoardSerializer(hdata, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

def noticeboard_detail_view_delete(request, slug, hdata):
    delresult = hdata.delete()
    data = {'message': 'error during deletion'}
    if delresult[0] == 1:
        data = {'message' : 'succesfully deleted'}
    return Response(data)
    