from django.http import JsonResponse, HttpResponse
from web3util.web3util import *
from web3util.math import *
from web3util.private import *
from web3util.oracle import *

def bribeContent(request):
    if 'address' not in request.GET:
        return HttpResponse(status=400)
    address = request.GET['address']

    private = PrivateInfo(address)

    data = list()

    vt = sum([asset.total_votes for asset in private.assets])

    for asset in private.assets:
        data.append(
            {
                'asset': asset.name,
                'desc': asset.description,
                'token': asset.token,
                'TV': str(round(asset.total_votes, 2)) + ' ' + 'xATE',
                'TVP': str(round(asset.total_votes/vt*100, 2))+ '%',
                'TB': printDollar(token2Dollar(asset.total_bribes, 'xate')),
                'TBC': str(round(asset.total_bribes, 2)) + ' ' + 'xATE',
                'B&I': printDollar(asset.bribe_n_interest),
                'VAPR': str(round(asset.voting_apr, 2)) + '%',
            } 
        )
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

