# Arete-backend

DeFi Lending Protocol with ve(3, 3) tokenomics

## Endpoint

https://api.aretelending.xyz

## Test Account

`0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC`

## API Spec

|  TAB    |                             URI                              |Method|                Description                  |
|---------|--------------------------------------------------------------|------|---------------------------------------------|
|user     |`/user/check?address=???`                                     |`GET` |주소가 유효한지 확인 (204 / 404)             |
|market   |`/market/header`                                              |`GET` |Market Header 내용                           |
|market   |`/market/content`                                             |`GET` |Market Content 내용                          |
|dashboard|`/dashboard/header?address=???`                               |`GET` |대시보드 header 정보                         |
|dashboard|`/dashboard/header/supply?address=???`                        |`GET` |My Supplies tab 헤더 정보                    |
|dashboard|`/dashboard/header/borrow?address=???`                        |`GET` |My Borrows tab 헤더 정보                     |
|dashboard|`/dashboard/supply?address=???`                               |`GET` |My Supplies tab detail                       |
|dashboard|`/dashboard/borrow?address=???`                               |`GET` |My Borrows tab detail                        |
|dashboard|`/dashboard/asset/supply?address=???`                         |`GET` |Assets to Supply tab detail                  |
|dashboard|`/dashboard/asset/borrow?address=???`                         |`GET` |Assets to Borrow tab detail                  |
|dashboard|`/dashboard/action/supply?address=???&asset=???&balance=???`  |`GET` |Supply action                                |
|dashboard|`/dashboard/action/withdraw?address=???&asset=???&balance=???`|`GET` |Withdraw action                              |
|dashboard|`/dashboard/action/borrow?address=???&asset=???&balance=???`  |`GET` |Borrow action                                |
|dashboard|`/dashboard/action/repay?address=???&asset=???&balance=???`   |`GET` |Repay action                                 |
|ate      |`/ate/header?address=???`                                     |`GET` |xATE tab header                              |
|ate      |`/ate/vesting?address=???`                                    |`GET` |contents of "Extract ATE" table              |
|ate      |`/ate/action/forge?address=???&balance=???`                   |`GET` |Forge action                                 |
|ate      |`/ate/action/extract?address=???&index=???`                   |`GET` |Extract action                               |
|vote     |`/vote/header?address=???`                                    |`GET` |Vote tab header & Vote Power Used information|
|vote     |`/vote/content?address=???`                                   |`GET` |Vote tab table content                       |
|vote     |`/vote/action/vote?address=???&asset=???&balance=???`         |`GET` |Vote table action                            |
|bribe    |`/bribe/content?address=???`                                  |`GET` |Bribe tab table Content                      |
|bribe    |`/bribe/action/bribe?address=???&asset=???&balance=???`       |`GET` |Bribe action                                 |

## TODO List

- [x] Supply Action
- [x] Withdraw Action
- [x] Borrow Action
- [x] Repay Action
- [x] Forge Action
- [x] Extract Action (+ redesign)
- [x] Vote Action
- [x] Bribe Action
- [x] Dollar to Token (and Wei) function
- [x] Dollar to xATE in xATE tab
- [ ] Dealing with unauthorized wallet
