from django.shortcuts import render
from django_daraja.mpesa.core import MpesaClient
from django.http import HttpResponse
# Create your views here.
def index(request):
    cl = MpesaClient()
    phone_number = '0794774699'
    amount = 2
    account_reference  = 'reference'
    transaction_desc = 'Description'
    callback_urls = 'https://darajambili.herokuapp.com/express-payment';
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_urls)
    return HttpResponse(response)
def stk_push_callback(request):
    data = request.body
    return HttpResponse('STK Push in Django')