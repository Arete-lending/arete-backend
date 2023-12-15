import asyncio

async def test():
    from web3 import Web3
    w3 = Web3(Web3.HTTPProvider("http://220.75.195.192:22212/"))
    usdc = "0x2D8553F9ddA85A9B3259F6Bf26911364B85556F5"
    account = "0xE5904695748fe4A84b40b3fc79De2277660BD1D3"
    key = "0x23c601ae397441f3ef6f1075dcb0031ff17fb079837beadaf3c84d96c6f3e569"
    metamask = "0x92561F28Ec438Ee9831D00D1D59fbDC981b762b2"
    
    nonce = w3.eth.get_transaction_count(account)

    trnx = {
        "from": account,
        "to": metamask,
        "value": 1000000000000000000,
        "nonce": nonce,
        "gas": 200000,
        "gasPrice": 1000000
    }
    stx = w3.eth.account.sign_transaction(trnx, key)
    print(stx)
    tx_hash = w3.eth.send_raw_transaction(stx.rawTransaction)
    print(w3.to_hex(tx_hash))

    print(w3.eth.get_balance(account, 'latest'))
    print(w3.eth.get_balance(metamask, 'latest'))

    # execute contract fucntion
    #nonce = w3.eth.get_transaction_count(account, 'latest')
    #contract = w3.eth.contract(address=oracle, abi=abi)
    #assetPrice = contract.functions.getAssetPrice(usdc).call()
    #print(assetPrice)
