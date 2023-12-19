from django.http import JsonResponse, HttpResponse
from web3util.web3util import *
from web3util.vesting import *
from web3util.private import *
from web3util.actions import *
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
            'balance': printDollar(toToken(ate, 'ate'))[1:],
            'balanceD': printDollar(wei2Dollar(ate, 'ate')),
        },
        'ATE': {
            'balance': printDollar(toToken(xate, 'xate'))[1:],
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

    for idx, vest in enumerate(vesting.vestings):
        data.append(
            {
                'index': idx,
                'xKZA': printDollar(token2Dollar(vest.xATE_vesting, 'xate')),
                'KZA': printDollar(token2Dollar(vest.ATE_output, 'ate')),
                'etime': printETime(vest.saved_at),
            } 
        )
    return JsonResponse(data, safe=False)

def actionForge(request):
    if 'address' not in request.GET:
        return HttpResponse(status=400)
    address = request.GET['address']
    if 'balance' not in request.GET:
        return HttpResponse(status=400)
    balance = float(request.GET['balance'])
    actForge(address, balance)
    return HttpResponse(status=200)

def actionExtract(request):
    if 'address' not in request.GET:
        return HttpResponse(status=400)
    address = request.GET['address']
    if 'index' not in request.GET:
        return HttpResponse(status=400)
    index = request.GET['index']
    index = int(request.GET['index'])
    actExtract(address, index)
    return HttpResponse(status=200)

