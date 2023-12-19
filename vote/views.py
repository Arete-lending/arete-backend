from django.http import JsonResponse, HttpResponse
from web3util.web3util import *
from web3util.math import *
from web3util.private import *
from web3util.actions import *

def voteHeader(request):
    if 'address' not in request.GET:
        return HttpResponse(status=400)
    address = request.GET['address']

    private = PrivateInfo(address)

    data = {
        "TVP": printDollar(private.my_total_voting_power),
        "TR": printDollar(private.total_rewards),
        "MR": printDollar(private.my_rewards),
        "VPU": str(round(private.my_vote_power_used, 2)) + "%",
    }
    return JsonResponse(data)

def voteContent(request):
    if 'address' not in request.GET:
        return HttpResponse(status=400)
    address = request.GET['address']

    private = PrivateInfo(address)

    data = list()

    for (asset, private) in zip(private.assets, private.privates):
        data.append(
            {
                'asset': asset.name,
                'desc': asset.description,
                'token': asset.token,
                'TV': str(round(asset.total_votes, 2)) + ' ' + 'xATE',
                'bribes': str(round(asset.total_bribes, 2)) + ' ' + 'xATE',
                'B&I': str(round(asset.bribe_n_interest, 2)) + ' ' + 'xATE',
                'VAPR': str(round(asset.voting_apr, 2)) + '%',
                'MV': str(round(private.vote, 2)) + ' ' + 'xATE',
                'MVP': str(round(private.vote/asset.total_votes*100)) + '%',
            }
        )
    return JsonResponse(data, safe=False)

def actionVote(request):
    if 'address' not in request.GET:
        return HttpResponse(status=400)
    address = request.GET['address']
    if 'asset' not in request.GET:
        return HttpResponse(status=400)
    asset = request.GET['asset']
    if 'balance' not in request.GET:
        return HttpResponse(status=400)
    balance = float(request.GET['balance'])
    actVote(address, asset, balance)
    return HttpResponse(status=200)

