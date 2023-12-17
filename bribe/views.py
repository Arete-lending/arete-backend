from django.http import JsonResponse, HttpResponse
from web3util.web3util import *
from web3util.math import *

def bribeContent(request):
    data = [
        {
            'asset': 'DAI',
            'desc': 'DAI Token',
            'token': 'DAI',
            'TV': '3.24' + ' ' + 'xATE',
            'TVP': '4.45%',
            'TB': printDollar(2.33),
            'TBC': '44.13' + ' ' + 'xATE',
            'B&I': printDollar(234824),
            'VAPR': '23.13%',
         } 
    ] * 5
    return JsonResponse(data, safe=False)

def actionBribe(request):
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

