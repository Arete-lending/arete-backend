from django.http import JsonResponse
from web3util.wallet import test
import asyncio

def index(request):
    res = {
        "test": "content"
    }
    return JsonResponse(res)


def getWallet(request):
    asyncio.run(test())
    return JsonResponse({})
