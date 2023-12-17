from django.http import JsonResponse, HttpResponse
from web3util.web3util import *
from market.market import market_config
from web3util.math import *

def marketHeader(request):
    data = {
        "TVL": printDollar(22390000),
        "TB": printDollar(9090000),
        "TA": printDollar(13300000)
    }
    return JsonResponse(data)

def market(request):
    data = [
        {
            'name': 'DAI',
            'desc': 'DAI Token',
            'token': 'DAI',
            'ctype': 'Open',
            'LTV': '70.00%',
            'sAPY': '28.33%',
            'sFST': '0.13%',
            'sSND': '28.02%',
            'TS': printDollar(7190000),
            'TSC': '171.72' + ' ' + 'DAI',
            'bAPY': '1.80%',
            'TB': printDollar(1440000),
            'TBC': '34.37' + ' ' + 'DAI',
            'AV': printDollar(5670000),
            'AVC': '135.45' + ' ' + 'DAI',
         } 
    ] * 5
    return JsonResponse(data, safe=False)

