market_kinds = [
    "dai",
    "usdt",
    "wbtc",
    "weth",
]

supply_apy = 28.09

market_config = [
    {"dai": {
        "type": "Open",
        "LTV": 75,
        "supply": 3,
        "borrow": 7,
        "private": 11,
    }},
    {"usdt": {
        "type": "Isolated",
        "LTV": 75,
        "supply": 4,
        "borrow": 8,
        "private": 12,
    }},
    {"wbtc": {
        "type": "Open",
        "LTV": 70,
        "supply": 5,
        "borrow": 9,
        "private": 13,
    }},
    {"weth": {
        "type": "Open",
        "LTV": 75,
        "supply": 6,
        "borrow": 10,
        "private": 14,
    }},
]

