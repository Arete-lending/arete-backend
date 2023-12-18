from web3util.web3util import *
from web3util.math import *
from web3util.asset import *
import datetime

class Vesting:

    def __init__(self, address: str): 
        self.w3 = None
        self.vestings = []

        info = self.getInformationOfToken()
        infos = self.getInfos(info)
        for info in infos:
            self.vestings.append(VestingIter(info))
        
    def getInformationOfToken(self):
        asset_info = abi.accounts[10]
        self.asset = asset_info[0]
        self.private = asset_info[1]
        self.w3 = getProvider(self.asset)
        return balance(self.asset, 'xate')

    def getInfos(self, info: int):
        infos = list()
        if info == 0: return infos
        while info >= 10 ** 26:
            infos.append(info % (10 ** 26))
            info = info / (10 ** 26)
        infos.append(info)
        return infos

class VestingIter:
    xATE_vesting = 0
    ATE_output = 0
    saved_at = datetime.datetime(2023, 11, 7, 0, 0, 0)

    def __init__(self, info: int):
        acc = [26, 20, 14, 0]
        self.getVesting(self.cut(info, acc[0], acc[1]))
        self.getOutput(self.cut(info, acc[1], acc[2]))
        self.getSavedAt(self.cut(info, acc[2], acc[3]))

    def datecut(self, info: int, u: int, d: int):
        uu = 10 ** u
        dd = 10 ** d
        diff = 10 ** (u - d)
        ret = (info // dd) - (info // uu) * diff
        if ret == 0: return 1
        return ret

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

    def getVesting(self, val):
        self.xATE_vesting = self.sixCount(val)

    def getOutput(self, val):
        self.ATE_output = self.sixCount(val)

    def getSavedAt(self, val):
        self.saved_at = datetime.datetime(
            self.datecut(val, 14, 10),
            self.datecut(val, 10, 8),
            self.datecut(val, 8, 6),
            self.datecut(val, 6, 4),
            self.datecut(val, 4, 2),
            self.datecut(val, 2, 0)
        )

    def print(self):
        data = {
            'vesting': self.xATE_vesting,
            'output': self.ATE_output,
            'elapsedTime': printETime(self.saved_at),
        } 
        return data

