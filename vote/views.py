from django.http import JsonResponse, HttpResponse
from web3util.web3util import *
from web3util.math import *

def voteHeader(request):
    if 'address' not in request.GET:
        return HttpResponse(status=400)
    address = request.GET['address']
    data = {
        "TVP": 3.45,
        "TR": printDollar(215000),
        "MR": printDollar(204),
        "VPU": "0%",
    }
    return JsonResponse(data)

def voteContent(request):
    if 'address' not in request.GET:
        return HttpResponse(status=400)
    address = request.GET['address']
    data = [
        {
            'asset': 'DAI',
            'desc': 'DAI Token',
            'token': 'DAI',
            'TV': '53.12' + ' ' + 'ATE',
            'bribes': '34.60' + ' ' + 'xATE',
            'B&I': '36.01' + ' ' + 'xATE',
            'VAPR': str(round(36.01/34.60*100, 2)) + '%',
            'MV': '0.34' + ' ' + 'ATE',
            'MVP': str(round(0.34/53.12*100)) + '%',
        }
    ] * 5
    return JsonResponse(data, safe=False)

def actionVote(request):
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

