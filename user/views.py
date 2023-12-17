from django.http import JsonResponse, HttpResponse
from web3util.web3util import *
import asyncio

def index(request):
    res = {
        "test": "content"
    }
    return JsonResponse(res)

def isWallet(request):
    if 'address' not in request.GET:
        return HttpResponse(status=400)
    address = request.GET['address']
    if isAddress(address):
        return HttpResponse(status=204)
    return HttpResponse(status=404)
