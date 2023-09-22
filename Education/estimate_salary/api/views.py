from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from estimate_salary.models import salary_data
from .serializers import SalaryDataSerializer
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from sklearn import linear_model
from accounts.models import User,Student,Administrator


@api_view(http_method_names=['GET','POST',])
def salary_list_view(request):
    if request.user.is_admin:
        if request.method == 'GET':
            return salary_list_view_get(request)
        elif request.method == 'POST':
            return salary_list_view_post(request)
    else:
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

def salary_list_view_get(request):
    try:
        data = salary_data.objects.all()
        serializer = SalaryDataSerializer(data,many=True)
        return Response(data=serializer.data)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

def salary_list_view_post(request):
    
    serializer = SalaryDataSerializer(data=request.data,many = True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def get_estimates_view(request):
    subjects_map = {'Mathematics':1,'Science':2,'Social':3,'English':4,'Hindi':5,'Telugu':6}
    loc_map={'urban':1,'semi-urban':2,'rural':3}
    locations=['urban','semi-urban','rural']
    subjects=['Mathematics','Science','Social','English','Hindi','Telugu']
    data = request.data
    print('********************************')
    print(data['subject'])
    print(type(data['experience']))
    print(data['score'])
    print(data['job_location'])
    import pickle   
    if (data['job_location'] in locations) and (data['subject'] in subjects) and (int(data['experience'])<=50 and int(data['experience'])>=0) and int(data['score'])<=100 :
        x=[[int(data['experience']),loc_map[data['job_location']],int(data['score']),subjects_map[data['subject']]]]
        regressor = pickle.load(open('C:\\Users\\NITHISH KUMAR\\Desktop\\finalized_model.sav','rb'))
        prediction = regressor.predict(x)
        pred = {'salary':prediction}
        return Response(pred)
    else:
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

@api_view(http_method_names=['GET','PUT','DELETE'])
def salary_detail_view(request,slug):
    try:
        hdata = salary_data.objects.get(id=slug)
        if request.method == 'GET':
            return salary_detail_view_get(request, slug, hdata)
        elif request.method == 'PUT':
            return salary_detail_view_put(request, slug, hdata)
        elif request.method == 'DELETE':
            return salary_detail_view_delete(request, slug, hdata)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

def salary_detail_view_get(request,slug,hdata):
    serializer=SalaryDataSerializer(hdata)
    return Response(serializer.data)
def salary_detail_view_put(request,slug,hdata):
    serializer = SalaryDataSerializer(hdata, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
def salary_detail_view_delete(request,slug,hdata):
    delresult = hdata.delete()
    data = {'message': 'error during deletion'}
    if delresult[0] == 1:
        data = {'message' : 'succesfully deleted'}
    return Response(data)