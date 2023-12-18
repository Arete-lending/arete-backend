import asyncio
from web3util.json import abi

async def test():
    from web3 import Web3

    w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545/"))
    account = "0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC"

    # contract
    conaddr = abi.json['USDC-TestnetMintableERC20-Aave']['address']
    mintabi = abi.json['USDC-TestnetMintableERC20-Aave']['abi']
    
    # execute contract fucntion
    contract = w3.eth.contract(address=conaddr, abi=mintabi)

    mintPrice = contract.functions.mint(account, 100000000000000000000).call()
    print(mintPrice)
    # assetPrice = contract.functions.supply(usdc, 10000000, account, 0).call()
    # print(assetPrice)

web3_provider_url = "http://127.0.0.1:8545/"

def getAccount(number: int):
    return abi.accounts[number][0]

def getPrivate(number: int):
    return abi.accounts[number][1]

def getAccountPrivate(number: int):
    return {
        'account': abi.accounts[number][0],
        'private': abi.accounts[number][1],
    }

def getNullAccount():
    return abi.accounts[19][0]

def findPrivate(account: str):
    for acc in abi.accounts:
        if account == acc[0]:
            return acc[1]
    return 'error'

def abiCandidate(token: str):
    abi_cand = {
        'dai': 'DAI-TestnetMintableERC20-Aave',
        'link': 'LINK-TestnetMintableERC20-Aave',
        'usdc': 'USDC-TestnetMintableERC20-Aave',
        'wbtc': 'WBTC-TestnetMintableERC20-Aave',
        'weth': 'WETH-TestnetMintableERC20-Aave',
        'usdt': 'USDT-TestnetMintableERC20-Aave',
        'ate': 'AAVE-TestnetMintableERC20-Aave',
        'xate': 'EURS-TestnetMintableERC20-Aave',
    }
    return abi_cand[token]

def tokenDescription(token: str):
    desc_cand = {
        'dai': 'DAI Token',
        'link': 'LINK Token',
        'usdc': 'USD Coin',
        'wbtc': 'Wrapped Bitcoin',
        'weth': 'Wrapped Ethereum Token',
        'usdt': 'Tether USD',
        'ate': 'ARETE Token',
        'xate': 'staked ARETE Token',
    }
    return desc_cand[token]

def assetAddress(token: str):
    addr_cand = {
        'dai': abi.accounts[18],
        'link': abi.accounts[17],
        'usdc': abi.accounts[16],
        'wbtc': abi.accounts[15],
        'weth': abi.accounts[14],
        'usdt': abi.accounts[13],
        'ate': abi.accounts[12],
        'xate': abi.accounts[11],
    }
    return addr_cand[token]

async def getProvider(account: str):
    from web3 import Web3
    w3 = Web3(Web3.HTTPProvider(web3_provider_url))
    w3.eth.default_account = account
    return w3

async def baseProvider():
    from web3 import Web3
    w3 = Web3(Web3.HTTPProvider(web3_provider_url))
    return w3

async def asyncMint(account: str, token: str, amount: int):
    w3 = await getProvider(account)

    contaddr = abi.json[abiCandidate(token.lower())]['address']
    mintabi = abi.json[abiCandidate(token.lower())]['abi']

    # execute contract function
    contract = w3.eth.contract(address=contaddr, abi=mintabi)
    
    nonce = w3.eth.get_transaction_count(account)
    chain_id = w3.eth.chain_id
    trnx_info = {"chainId": chain_id, "from": account, "nonce": nonce}
    call_fn = contract.functions.mint(account, amount).build_transaction(trnx_info)
    signed_tx = w3.eth.account.sign_transaction(call_fn, private_key=findPrivate(account))
    send_tx = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

    tx_receipt = w3.eth.wait_for_transaction_receipt(send_tx)
    return tx_receipt

async def asyncBurn(account: str, token: str, amount: int):
    w3 = await getProvider(account)

    contaddr = abi.json[abiCandidate(token.lower())]['address']
    burnabi = abi.json[abiCandidate(token.lower())]['abi']
    null = getNullAccount()

    # execute contract function
    contract = w3.eth.contract(address=contaddr, abi=burnabi)
    
    nonce = w3.eth.get_transaction_count(account)
    chain_id = w3.eth.chain_id
    trnx_info = {"chainId": chain_id, "from": account, "nonce": nonce}
    call_fn = contract.functions.transfer(null, amount).build_transaction(trnx_info)
    signed_tx = w3.eth.account.sign_transaction(call_fn, private_key=findPrivate(account))
    send_tx = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

    tx_receipt = w3.eth.wait_for_transaction_receipt(send_tx)
    return tx_receipt

async def asyncBalanceOf(account: str, token: str, res: list):
    w3 = await getProvider(account)

    contaddr = abi.json[abiCandidate(token.lower())]['address']
    balanceabi = abi.json[abiCandidate(token.lower())]['abi']
    
    # execute contract function
    contract = w3.eth.contract(address=contaddr, abi=balanceabi)

    res.append(contract.functions.balanceOf(account).call())

def mint(account, token, amount):
    asyncio.run(asyncMint(account, token, amount))

def burn(account, token, amount):
    asyncio.run(asyncBurn(account, token, amount))

def balance(account, token):
    res = list()
    asyncio.run(asyncBalanceOf(account, token, res))
    return res[0]

async def asyncIsAddress(address: str, ret: list):
    w3 = await baseProvider()
    ret.append(w3.is_address(address))

def isAddress(address):
    ret = list()
    asyncio.run(asyncIsAddress(address, ret))
    return ret[0]
