from django.http import JsonResponse, HttpResponse
from web3util.web3util import *
from web3util.vesting import *
from web3util.private import *
from web3util.math import *

first_epoch = datetime.datetime(2023, 11, 7, 0, 0, 0)

def ATEHeader(request):
    if 'address' not in request.GET:
        return HttpResponse(status=400)
    address = request.GET['address']
    ate = balance(address, 'ate')
    xate = balance(address, 'xate')
    data = {
        'xATE': {
            'balance': printDollar(wei2Dollar(ate, 'ate')),
            'balanceD': printDollar(wei2Dollar(ate, 'ate')),
        },
        'ATE': {
            'balance': printDollar(wei2Dollar(xate, 'xate')),
            'balanceD': printDollar(wei2Dollar(xate, 'xate')),
        }
    }
    return JsonResponse(data)

def listVesting(request):
    if 'address' not in request.GET:
        return HttpResponse(status=400)
    address = request.GET['address']
    vesting = Vesting(address)
    data = list()

    for vest in vesting.vestings:
        data.append(
            {
                'xKZA': round(vest.xATE_vesting, 2),
                'KZA': round(vest.ATE_output, 2),
                'etime': printETime(vest.saved_at),
            } 
        )
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

