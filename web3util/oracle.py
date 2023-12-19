# There is no Oracle service in the testnet.
# Thus we need to mock oracle by this function
#
# Feel free to change these functions if you want
# to use actual API for more realistic mocking.
# However, the danger from the liquidation is already
# examined by the test codes, and we don't have to
# care about it in the demo session.

def toToken(wei: int, token: str):
    token = token.lower()
    factor = {
        'dai': 0.0000000000000000001,
        'link': 0.0000000000000000001, 
        'usdc': 0.0000001,
        'wbtc': 0.000000001,
        'weth': 0.0000000000000000001,
        'usdt': 0.0000001,
        'ate': 0.0000000000000000001,
        'xate': 0.001,
    }
    return wei * factor[token]

def toWei(amount: int, token: str):
    token = token.lower()
    factor = {
        'dai': 1000000000000000000,
        'link': 1000000000000000000, 
        'usdc': 1000000,
        'wbtc': 100000000,
        'weth': 1000000000000000000,
        'usdt': 1000000,
        'ate': 1000000000000000000,
        'xate': 100,
    }
    return amount * factor[token]

def token2Dollar(amount: int, token: str):
    token = token.lower()
    factor = {
        'dai': 1.0,
        'link': 14.24,
        'usdc': 1.0,
        'wbtc': 41709.57,
        'weth': 2199.02,
        'usdt': 1.0,
        'ate': 13.23,
        'xate': 5.45,
    }
    return amount * factor[token]

def wei2Dollar(wei: int, token: str):
    token = token.lower()
    return token2Dollar(toToken(wei, token), token)

initial_oracle = {
    'dai': '0750105245220014602781650810034560019600398111111101010000000',
    'link': '0750108245211472704701039750009120008600154111111101010000000',
    'usdc': '1750201245220053403442003650945120118740223111111101010000000',
    'wbtc': '1700026245201850201650033961003111001330108111111101010000000',
    'weth': '1700024245207945101240178831001530965110144111111101010000000',
    'usdt': '0750158245220044203052002660008650004320523111111111111000000',
    'ate': '0',
    'xate': '200100000000000000',
    'vesting': '00034500072320231217233017',
}

