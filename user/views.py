from django.http import JsonResponse, HttpResponse
from web3util.asset import *
from web3util.private import *
from web3util.vesting import *
from web3util.web3util import *
from web3util.oracle import *

def index(request):
    dai = Asset('dai')
    link = Asset('link')
    usdc = Asset('usdc')
    wbtc = Asset('wbtc')
    weth = Asset('weth')
    usdt = Asset('usdt')
    return JsonResponse([
        dai.print(),
        link.print(),
        usdc.print(),
        wbtc.print(),
        weth.print(),
        usdt.print()
    ], safe=False)

def init(request):
    # For mocking Oracle & sufficient Pool fluidity
    pin = 1000000
    test_wallet = '0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC'
    for (key, val) in initial_oracle.items():
        if key == 'vesting':
            addr = abi.accounts[10][0]
            burn(addr, 'xate', balance(addr, 'xate'))
            mint(addr, 'xate', int(val))
            continue
        addr = assetAddress(key)[0]
        burn(addr, key, balance(addr, key))
        mint(addr, key, int(val))
        burn(test_wallet, key, balance(test_wallet, key))
        mint(test_wallet, key, toWei(pin, key))
    return JsonResponse({})

def isWallet(request):
    if 'address' not in request.GET:
        return HttpResponse(status=400)
    address = request.GET['address']
    if isAddress(address):
        return HttpResponse(status=204)
    return HttpResponse(status=404)
