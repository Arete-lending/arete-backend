from django.http import JsonResponse, HttpResponse
from web3util.web3util import *
from market.market import market_config
from web3util.math import *
from web3util.asset import *

market_names = ['dai', 'link', 'usdc', 'wbtc', 'weth', 'usdt']


def marketHeader(request):
    assets = list()
    for market in market_names:
        assets.append(Asset(market))

    tvl = sum([
        token2Dollar(asset.total_supplied, asset.token)
        for asset in assets
    ])
    tb = sum([
        token2Dollar(asset.total_borrowed, asset.token)
        for asset in assets
    ])

    data = {
        "TVL": printDollar(tvl),
        "TB": printDollar(tb),
        "TA": printDollar(tvl-tb)
    }
    return JsonResponse(data)

def market(request):
    data = list()
    for market in market_names:
        asset = Asset(market)
        data.append(asset.print())
    return JsonResponse(data, safe=False)

