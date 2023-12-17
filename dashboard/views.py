from django.http import JsonResponse, HttpResponse
from web3util.web3util import *
from web3util.math import printDollar
import asyncio

def dashboardHeader(request):
    if 'address' not in request.GET:
        return HttpResponse(status=400)
    address = request.GET['address']
    data = {
        "Net": printDollar(1230000),
        "nAPY": "29.04%",
        "cLTV": "70%",
        "HF": "100%",
    }
    return JsonResponse(data)

def headerBorrow(request):
    if 'address' not in request.GET:
        return HttpResponse(status=400)
    address = request.GET['address']
    data = {
        'balance': printDollar(1740000),
        'APY': '29.04%',
        'BPU': '30.00%',
    }
    return JsonResponse(data)

def headerSupply(request):
    if 'address' not in request.GET:
        return HttpResponse(status=400)
    address = request.GET['address']
    data = {
        'balance': printDollar(2340000),
        'APY': '28.45%',
        'COL': printDollar(1230000),
    }
    return JsonResponse(data)

def supply(request):
    if 'address' not in request.GET:
        return HttpResponse(status=400)
    address = request.GET['address']
    data = [
        {
            'name': 'DAI',
            'desc': 'DAI Token',
            'token': 'DAI',
            'balance': printDollar(2340000),
            'ctype': 'Open',
            'APY': '28.33%',
            'COL': printDollar(5640000),
         } 
    ] * 5
    return JsonResponse(data, safe=False)

def borrow(request):
    if 'address' not in request.GET:
        return HttpResponse(status=400)
    address = request.GET['address']
    data = [
        {
            'asset': 'DAI',
            'desc': 'DAI Token',
            'token': 'DAI',
            'DEBT': printDollar(5670000),
            'ctype': 'Open',
            'APY': '28.33%', 
        } 
    ] * 5
    return JsonResponse(data, safe=False)

def assetsToSupply(request):
    if 'address' not in request.GET:
        return HttpResponse(status=400)
    address = request.GET['address']
    data = [
        {
            'asset': 'DAI',
            'desc': 'DAI Token',
            'token': 'DAI',
            'balance': printDollar(7190000),
            'ctype': 'Open',
            'APY': '28.33%', 
        } 
    ] * 5
    return JsonResponse(data, safe=False)

def assetsToBorrow(request):
    if 'address' not in request.GET:
        return HttpResponse(status=400)
    address = request.GET['address']
    data = [
        {
            'asset': 'DAI',
            'desc': 'DAI Token',
            'token': 'DAI',
            'AV': printDollar(5670000),
            'ctype': 'Open',
            'APY': '28.33%', 
        } 
    ] * 5
    return JsonResponse(data, safe=False)

def actionSupply(request):
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

def actionWithdraw(request):
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

def actionBorrow(request):
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

def actionRepay(request):
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

