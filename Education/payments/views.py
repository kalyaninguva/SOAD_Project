from django.shortcuts import render

# Create your views here.
from . import Checksum
from django.shortcuts import render,redirect
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from payments.utils import VerifyPaytmResponse
import requests
from .models import Locality,Person
from .forms import LocalityForm,PersonForm

def home(request):
    return render(request,"payments/home.html")


def paynow(request):
    if request.method == 'POST':
        amount = request.POST['amount']
    return HttpResponse("<html><a href='http://localhost:8000/payment'>PayNow</html>")    

def findschool(request):
     form=LocalityForm()
     if request.method=='POST':
         form=LocalityForm(request.POST)
         if form.is_valid():
             form.save()
             return redirect('filldetails')
     context={'form':form}
     return render(request,"payments/findschool.html",context)

def filldetails(request):
     form=PersonForm()
     if request.method=='POST':
         form=PersonForm(request.POST)
         if form.is_valid():
             obj=form.save(commit=False)
             obj.Locality=Locality.objects.last()
             obj.save()
             return redirect('payment')

     context={'form':form}
     return render(request,"payments/filldetails.html",context)

def payment(request):
    order_id = Checksum.__id_generator__()
    obj=Person.objects.last()
    bill_amount = obj.amount
    data_dict = {
        'MID': settings.PAYTM_MERCHANT_ID,
        'INDUSTRY_TYPE_ID': settings.PAYTM_INDUSTRY_TYPE_ID,
        'WEBSITE': settings.PAYTM_WEBSITE,
        'CHANNEL_ID': settings.PAYTM_CHANNEL_ID,
        'CALLBACK_URL': settings.PAYTM_CALLBACK_URL,
        'MOBILE_NO': obj.phonenumber,
        'EMAIL': obj.youremail,
        'TXN_AMOUNT': obj.amount,
        'CUST_ID':str(obj.id),
        'ORDER_ID':order_id,
    } # This data should ideally come from database
    data_dict['CHECKSUMHASH'] = Checksum.generate_checksum(data_dict, settings.PAYTM_MERCHANT_KEY)
    context = {
        'payment_url': settings.PAYTM_PAYMENT_GATEWAY_URL,
        'comany_name': settings.PAYTM_COMPANY_NAME,
        'data_dict': data_dict
    }
    return render(request, 'payments/payment.html', context)


@csrf_exempt
def response(request):
    resp = VerifyPaytmResponse(request)
    if resp['verified']:
        # save success details to db; details in resp['paytm']
        # return HttpResponse("<center><h1>Transaction Successful</h1><center>", status=200)
        return render(request,"payments/finalResponse.html")
       # return redirect('response')
    else:
        # check what happened; details in resp['paytm']
        return HttpResponse("<center><h1>Transaction Failed</h1><center>", status=400)