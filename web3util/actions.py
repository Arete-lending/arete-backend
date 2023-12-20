from web3util.web3util import *
from web3util.json import *
from web3util.asset import *
from web3util.oracle import *
from web3util.vesting import *
from web3util.private import *
import datetime

def actSupply(address: str, token: str, balance: float):
    asset = Asset(token)
    burn(address, token, int(toWei(balance, token)))
    val = asset.total_supplied
    setPosition(getAsset(token), token, asset_info_acc[4], asset_info_acc[5], backToSix(val+balance))
    mint(address, 'ate', int(toWei(governanceCalc(balance), 'ate')))

def actWithdraw(address: str, token: str, balance: float):
    asset = Asset(token)
    mint(address, token, int(toWei(balance, token)))
    val = asset.total_supplied
    setPosition(getAsset(token), token, asset_info_acc[4], asset_info_acc[5], backToSix(val-balance))

def actBorrow(address: str, token: str, balance: float):
    asset = Asset(token)
    mint(address, token, int(toWei(balance, token)))
    val = asset.total_supplied
    setPosition(getAsset(token), token, asset_info_acc[4], asset_info_acc[5], backToSix(val-balance))

def actRepay(address: str, token: str, balance: float):
    asset = Asset(token)
    burn(address, token, int(toWei(balance, token)))
    val = asset.total_supplied
    setPosition(getAsset(token), token, asset_info_acc[4], asset_info_acc[5], backToSix(val+balance))

def actForge(address: str, amount: float):
    vesting = Vesting(address)
    if len(vesting.vestings) >= 3: return
    burn(address, 'ate', int(toWei(amount, 'ate')))
    asset = abi.accounts[10][0]
    val = balance(asset, 'xate')
    burn(asset, 'xate', val)
    mint(asset, 'xate', int(backTo20(val, int(amount/10), int(amount))))
    private = PrivateToken('xate')
    nextval = private.supply_balance + int(amount/10)
    setPosition(getAsset('xate'), 'xate', asset_info_acc[10], asset_info_acc[11], backToSix(nextval))

def actExtract(address: str, index: int):
    asset = abi.accounts[10][0]
    vesting = Vesting(address)
    outiter = vesting.vestings[index]
    tomint = outiter.ATE_output
    toburn = balance(asset, 'xate')
    d = pow(10, (index * 26))
    u = pow(10, ((index+1) * 26))
    bal = balance(asset, 'xate')
    nextbal = (bal % d) + (bal // u * d)
    burn(asset, 'xate', bal)
    mint(asset, 'xate', nextbal)
    mint(address, 'ate', int(toWei(tomint, 'ate')))

def actVote(address: str, token: str, amount: float):
    asset = Asset(token)
    private = PrivateToken(token)
    tv = asset.total_votes
    vapr = asset.voting_apr
    mv = private.vote
    burn(address, 'xate', int(toWei(amount, 'xate')))
    mv += amount
    vapr += 0.03
    tv += amount
    setPosition(getAsset(token), token, asset_info_acc[7], asset_info_acc[8], backToSix(tv))
    setPosition(getAsset(token), token, asset_info_acc[9], asset_info_acc[9], vapr*100)
    setPosition(getAsset(token), token, asset_info_acc[12], asset_info_acc[13], backToSix(mv))

def actBribe(address: str, token: str, amount: float):
    burn(address, 'xate', int(toWei(amount, 'xate')))
    asset = Asset(token)
    bal = asset.total_bribes
    print(bal)
    print(balance(getAsset(token), token))
    bal += amount
    print(bal)
    print(backToSix(bal))
    setPosition(getAsset(token), token, asset_info_acc[8], asset_info_acc[9], backToSix(bal))
    print(balance(getAsset(token), token))

##################################
#        Helper functions        #
##################################

def cut(info: int, u: int, d: int):
    uu = pow(10, u)
    dd = pow(10, d)
    diff = pow(10,u - d)
    return (info // dd) - (info // uu) * diff

def sixCount(val):
    val = int(val)
    cnt = val // (pow(10, 5))
    val = val % (pow(10, 5)) / 100
    val = val * pow(10, (cnt * 3))
    return int(val)

def backTo20(origin, vesting, output):
    now = datetime.datetime.now()
    datestr = now.strftime("%Y%m%d%H%M%S")
    return int((origin * (pow(10, 26))) + (backToSix(vesting) * (pow(10, 20)) + (backToSix(output) * (pow(10, 14)))) + int(datestr))

def backToSix(number):
    msb = 0
    if number >= 1000000000000:
        number = round(number / 1000000000000, 2)
        msb = 4
    elif number >= 1000000000:
        number = round(number / 1000000000, 2)
        msb = 3
    elif number >= 1000000:
        number = round(number / 1000000, 2)
        msb = 2
    elif number >= 1000:
        number = round(number / 1000, 2)
        msb = 1
    return msb * (pow(10, 5)) + number * 100

def setPosition(address: str, token: str, u: int, d: int, number: int):
    number = int(number)
    token = token.lower()
    uu = pow(10, u)
    dd = pow(10, d)
    bal = balance(address, token)
    toburn = ((bal // dd) * dd) - ((bal // uu) * uu)
    burn(address, token, toburn)
    tomint = int(number) * int(dd)
    mint(address, token, int(tomint))

def getAsset(token):
    return assetAddress(token)[0]

def governanceCalc(val):
    return val/100
