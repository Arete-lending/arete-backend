from web3util.web3util import *
from web3util.math import *
from web3util.oracle import *
import datetime

asset_info_idx = [1, 2, 4, 4, 6, 4, 6, 6, 6, 4, 6, 6, 6]
asset_info_acc = [0]
for info_idx in reversed(asset_info_idx):
    asset_info_acc = [info_idx+asset_info_acc[0]] + asset_info_acc

class Asset:
    w3 = None
    asset = ""
    private = ""
    name = "BASE"
    description = "base token"
    token = "BASE"
    collateral_type = "Open"
    LTV = 0
    supply_apy = 0
    token_incentives = 0
    base_apy = 0
    total_supplied = 0
    borrow_apy = 0
    total_borrowed = 0
    available = 0

    total_votes = 0
    total_bribes = 0
    bribe_n_interest = 0
    voting_apr = 0

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
        self.getCollateralType(self.cut(info, asset_info_acc[0], asset_info_acc[1]))
        self.getLTV(self.cut(info, asset_info_acc[1], asset_info_acc[2]))
        self.getTokenIncentives(self.cut(info, asset_info_acc[2], asset_info_acc[3]))
        self.getBaseApy(self.cut(info, asset_info_acc[3], asset_info_acc[4]))
        self.supply_apy = self.token_incentives + self.base_apy
        self.getTotalSupplied(self.cut(info, asset_info_acc[4], asset_info_acc[5]))
        self.getBorrowApy(self.cut(info, asset_info_acc[5], asset_info_acc[6]))
        self.getTotalBorrowed(self.cut(info, asset_info_acc[6], asset_info_acc[7]))
        self.getTotalVotes(self.cut(info, asset_info_acc[7], asset_info_acc[8]))
        self.getTotalBribes(self.cut(info, asset_info_acc[8], asset_info_acc[9]))
        self.bribe_n_interest = self.total_bribes + self.total_bribes * self.voting_apr / 100
        self.getVotingApr(self.cut(info, asset_info_acc[9], asset_info_acc[10]))

    def cut(self, info: int, u: int, d: int):
        uu = 10 ** u
        dd = 10 ** d
        diff = 10 ** (u - d)
        return (info // dd) - (info // uu) * diff

    def getCollateralType(self, val):
        if val == 1: self.collateral_type = "Open"
        else: self.collateral_type = "Isolated"

    def getLTV(self, val):
        self.LTV = val

    def getTokenIncentives(self, val):
        self.token_incentives = val / 100

    def getBaseApy(self, val):
        self.base_apy = val / 100

    def sixCount(self, val):
        cnt = val // (10 ** 5)
        val = val % (10 ** 5) / 100
        val = val * (10 ** (cnt * 3))
        return val

    def getTotalSupplied(self, val):
        self.total_supplied = self.sixCount(val)

    def getBorrowApy(self, val):
        self.borrow_apy = val / 100

    def getTotalBorrowed(self, val):
        self.total_borrowed = self.sixCount(val)

    def getTotalVotes(self, val):
        self.total_votes = self.sixCount(val)

    def getTotalBribes(self, val):
        self.total_bribes = self.sixCount(val)

    def getVotingApr(self, val):
        self.voting_apr = val / 100

    def print(self):
        data = {
            'name': self.name,
            'desc': self.description,
            'token': self.token,
            'ctype': self.collateral_type,
            'LTV': "{0:.2f}".format(self.LTV) + "%",
            'sAPY': "{0:.2f}".format(self.token_incentives + self.base_apy) + "%",
            'sFST': "{0:.2f}".format(self.token_incentives) + "%",
            'sSND': "{0:.2f}".format(self.base_apy) + "%",
            'TS': printDollar(token2Dollar(self.total_supplied, self.token)),
            'TSC': printToken(self.total_supplied, self.token),
            'bAPY': "{0:.2f}".format(self.borrow_apy) + "%",
            'TB': printDollar(token2Dollar(self.total_borrowed, self.token)),
            'TBC': printToken(self.total_borrowed, self.token),
            'AV': printDollar(token2Dollar(self.total_supplied - self.total_borrowed, self.token)),
            'AVC': printToken(self.total_supplied - self.total_borrowed, self.token),
        } 
        return data
