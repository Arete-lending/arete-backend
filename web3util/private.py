from web3util.web3util import *
from web3util.math import *
from web3util.asset import *
from web3util.oracle import *
import datetime

class PrivateInfo:
    market_names = ['dai', 'link', 'usdc', 'wbtc', 'weth', 'usdt']
    privates = list()
    assets = list()

    supplied = 0
    borrowed = 0
    supply_apy = 0
    borrow_apy = 0
    ltv = 0
    health_factor = 100

    collateral = 0
    borrow_power_used = 0

    my_total_voting_power = 0
    my_vote_power_used = 0
    total_rewards = 0
    my_rewards = 0

    def __init__(self, account: str):
        for market in self.market_names:
            self.privates.append(PrivateToken(market))
            self.assets.append(Asset(market))

        # information about suppliment
        supplied_dollar = [
            token2Dollar(private.supply_balance, private.token)
            for private in self.privates
        ]
        self.supplied = sum(supplied_dollar)
        if self.supplied != 0:

            supply_apys = [asset.supply_apy for asset in self.assets]
            self.supply_apy = sum([a*b for (a, b) in zip(supplied_dollar, supply_apys)]) / self.supplied
            
            # LTV
            ltvs = [asset.LTV for asset in self.assets]
            self.ltv = sum([a*b for (a, b) in zip(supplied_dollar, ltvs)]) / self.supplied

        # information about borrowing
        borrowed_dollar = [
            token2Dollar(private.borrow_balance, private.token)
            for private in self.privates
        ]
        self.borrowed = sum(borrowed_dollar)
        if self.borrowed != 0:

            borrow_apys = [asset.borrow_apy for asset in self.assets]
            self.borrow_apy = sum([a*b for (a, b) in zip(borrowed_dollar, borrow_apys)]) / self.borrowed

        if self.ltv != 0:
            # collateral & borrow_power_used
            self.collateral = self.borrowed * 100 / self.ltv
        if self.supplied != 0:
            self.borrow_power_used = self.collateral / self.supplied * 100

        # voting
        ate = PrivateToken('ate')
        xate = PrivateToken('xate')
        self.my_total_voting_power = token2Dollar(ate.supply_balance, 'ate') + token2Dollar(xate.supply_balance, 'xate')

        total_votes = [token2Dollar(asset.total_votes, 'xate') for asset in self.assets]
        voting_aprs = [asset.voting_apr for asset in self.assets]
        my_votes = [token2Dollar(private.vote, 'xate') for private in self.privates]
        
        self.my_vote_power_used = sum(my_votes)/self.my_total_voting_power if self.my_total_voting_power != 0 else 0

        self.total_rewards = sum([vote * apr / 100 for (vote, apr) in zip(total_votes, voting_aprs)])

        self.my_rewards = sum([vote * apr / 100 for (vote, apr) in zip(my_votes, voting_aprs)])


class PrivateToken:
    w3 = None
    asset = ""
    private = ""
    name = "BASE"
    description = "base token"
    token = "BASE"
    supply_balance = 0
    borrow_balance = 0
    vote = 0

    def __init__(self, token: str): 
        self.name = token.upper()
        self.description = tokenDescription(token)
        self.token = token.upper()
        info = self.getInformationOfToken(token)
        self.getInformation(info)
        
    def getInformationOfToken(self, token: str):
        asset_info = assetAddress(token)
        self.asset = asset_info[0]
        self.private = asset_info[1]
        self.w3 = getProvider(self.asset)
        return balance(self.asset, token)

    def getInformation(self, info: int):
        self.getSupplyBalance(self.cut(info, asset_info_acc[10], asset_info_acc[11]))
        self.getBorrowBalance(self.cut(info, asset_info_acc[11], asset_info_acc[12]))
        self.getVote(self.cut(info, asset_info_acc[12], asset_info_acc[13]))

    def cut(self, info: int, u: int, d: int):
        uu = 10 ** u
        dd = 10 ** d
        diff = 10 ** (u - d)
        return (info // dd) - (info // uu) * diff

    def sixCount(self, val):
        cnt = val // (10 ** 5)
        val = val % (10 ** 5) / 100
        val = val * (10 ** (cnt * 3))
        return val

    def getSupplyBalance(self, val):
        self.supply_balance = self.sixCount(val)

    def getBorrowBalance(self, val):
        self.borrow_balance = self.sixCount(val)

    def getVote(self, val):
        self.vote = self.sixCount(val)

    def print(self):
        data = {
            'name': self.name,
            'desc': self.description,
            'token': self.token,
            'SB': self.supply_balance,
            'BB': self.borrow_balance,
            'vote': self.vote
        } 
        return data

