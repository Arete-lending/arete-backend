from django.http import JsonResponse, HttpResponse
from web3util.web3util import *
from web3util.math import printDollar
from web3util.private import PrivateInfo
from web3util.oracle import *
from web3util.asset import *
from web3util.actions import *
from market.views import market_names

def dashboardHeader(request):
    if 'address' not in request.GET:
        return HttpResponse(status=400)
    address = request.GET['address']

    private = PrivateInfo(address)

    data = {
        "Net": printDollar(private.supplied),
        "nAPY": str(round(private.supply_apy, 2)) + "%" if private.supply_apy != 0 else '--',
        "cLTV": str(round(private.ltv, 2)) + "%" if private.ltv != 0 else '--',
        "HF": str(private.health_factor) + "%" if private.supplied != 0 else '--',
    }
    return JsonResponse(data)

def headerBorrow(request):
    if 'address' not in request.GET:
        return HttpResponse(status=400)
    address = request.GET['address']

    private = PrivateInfo(address)

    data = {
        'balance': printDollar(private.borrowed),
        'APY': str(round(private.borrow_apy, 2)) + "%" if private.borrow_apy != 0 else '--',
        'BPU': str(round(private.borrow_power_used, 2)) + "%" if private.borrow_power_used != 0 else '--',
    }
    return JsonResponse(data)

def headerSupply(request):
    if 'address' not in request.GET:
        return HttpResponse(status=400)
    address = request.GET['address']

    private = PrivateInfo(address)

    data = {
        'balance': printDollar(private.supplied),
        'APY': str(round(private.supply_apy, 2)) + "%" if private.supply_apy != 0 else '--',
        'COL': printDollar(private.collateral),
    }
    return JsonResponse(data)

def supply(request):
    if 'address' not in request.GET:
        return HttpResponse(status=400)
    address = request.GET['address']
    
    private = PrivateInfo(address)
    
    data = list()
    for (asset, private) in zip(private.assets, private.privates):
        if private.supply_balance == 0: continue
        balance = token2Dollar(private.supply_balance, asset.token)
        data.append(
            {
                'name': asset.name,
                'desc': asset.description,
                'token': asset.token,
                'balance': printDollar(balance),
                'ctype': asset.collateral_type,
                'APY': str(round(asset.supply_apy, 2)) + "%",
                'COL': printDollar(balance * asset.LTV / 100),
            } 
        )
    return JsonResponse(data, safe=False)

def borrow(request):
    if 'address' not in request.GET:
        return HttpResponse(status=400)
    address = request.GET['address']
    
    private = PrivateInfo(address)

    data = list()
    for (asset, private) in zip(private.assets, private.privates):
        if private.borrow_balance == 0: continue
        balance = token2Dollar(private.borrow_balance, asset.token)
        data.append(
            {
                'asset': private.name,
                'desc': private.description,
                'token': private.token,
                'DEBT': printDollar(balance),
                'ctype': asset.collateral_type,
                'APY': str(round(asset.borrow_apy, 2)) + "%", 
            } 
        )
    return JsonResponse(data, safe=False)

def assetsToSupply(request):
    if 'address' not in request.GET:
        return HttpResponse(status=400)
    address = request.GET['address']

    data = list()

    for market in market_names:
        bal = balance(address, market)
        if bal == 0: continue
        now = Asset(market)
        data.append(
            {
                'asset': now.name,
                'desc': now.description,
                'token': now.token,
                'balance': printDollar(wei2Dollar(bal, now.token)),
                'ctype': now.collateral_type,
                'APY': str(round(now.supply_apy, 2)) + "%",
            }
        )
    return JsonResponse(data, safe=False)

def assetsToBorrow(request):
    if 'address' not in request.GET:
        return HttpResponse(status=400)
    address = request.GET['address']

    data = list()
    private = PrivateInfo(address)

    for (asset, private) in zip(private.assets, private.privates):
        bal = token2Dollar((private.supply_balance * asset.LTV / 100) - private.borrow_balance, private.token)
        if bal <= 0: continue
        data.append(
            {
                'asset': asset.name,
                'desc': asset.description,
                'token': asset.token,
                'AV': printDollar(bal),
                'ctype': asset.collateral_type,
                'APY': str(round(asset.borrow_apy, 2)) + "%",
            }
        )
    return JsonResponse(data, safe=False)

def actionSupply(request):
    if 'address' not in request.GET:
        return HttpResponse(status=400)
    address = request.GET['address']
    if 'asset' not in request.GET:
        return HttpResponse(status=400)
    asset = request.GET['asset']
    if 'balance' not in request.GET:
        return HttpResponse(status=400)
    balance = float(request.GET['balance'])
    actSupply(address, asset, balance)
    return HttpResponse(status=200)

def actionWithdraw(request):
    if 'address' not in request.GET:
        return HttpResponse(status=400)
    address = request.GET['address']
    if 'asset' not in request.GET:
        return HttpResponse(status=400)
    asset = request.GET['asset']
    if 'balance' not in request.GET:
        return HttpResponse(status=400)
    balance = float(request.GET['balance'])
    actWithdraw(address, asset, balance)
    return HttpResponse(status=200)

def actionBorrow(request):
    if 'address' not in request.GET:
        return HttpResponse(status=400)
    address = request.GET['address']
    if 'asset' not in request.GET:
        return HttpResponse(status=400)
    asset = request.GET['asset']
    if 'balance' not in request.GET:
        return HttpResponse(status=400)
    balance = float(request.GET['balance'])
    actBorrow(address, asset, balance)
    return HttpResponse(status=200)

def actionRepay(request):
    if 'address' not in request.GET:
        return HttpResponse(status=400)
    address = request.GET['address']
    if 'asset' not in request.GET:
        return HttpResponse(status=400)
    asset = request.GET['asset']
    if 'balance' not in request.GET:
        return HttpResponse(status=400)
    balance = float(request.GET['balance'])
    actRepay(address, asset, balance)
    return HttpResponse(status=200)

