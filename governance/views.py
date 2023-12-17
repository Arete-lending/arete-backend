from django.http import JsonResponse, HttpResponse
from web3util.web3util import *
from web3util.math import *

first_epoch = datetime.date(2023, 11, 7)

def ATEHeader(request):
    if 'address' not in request.GET:
        return HttpResponse(status=400)
    address = request.GET['address']
    data = {
        'xATE': {
            'balance': 1.23,
            'balacneD': printDollar(14500),
        },
        'ATE': {
            'balance': 2.34,
            'balanceD': printDollar(5630),
        }
    }
    return JsonResponse(data)

def listVesting(request):
    if 'address' not in request.GET:
        return HttpResponse(status=400)
    address = request.GET['address']
    data = [
        {
            'xKZA': 3.46,
            'KZA': 21.69,
            'etime': printETime(first_epoch),
        } 
    ] * 5
    return JsonResponse(data, safe=False)

def actionForge(request):
    if 'address' not in request.GET:
        return HttpResponse(status=400)
    address = request.GET['address']
    if 'assest' not in request.GET:
        return HttpResponse(status=400)
    asset = request.GET['asset']
    if 'balance' not in request.GET:
        return HttpResponse(status=400)
    balance = request.GET['balance']
    return HttpResponse(status=200)

def actionExtract(request):
    if 'address' not in request.GET:
        return HttpResponse(status=400)
    address = request.GET['address']
    if 'assest' not in request.GET:
        return HttpResponse(status=400)
    asset = request.GET['asset']
    if 'balance' not in request.GET:
        return HttpResponse(status=400)
    balance = request.GET['balance']
    return HttpResponse(status=200)

