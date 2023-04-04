from storage import Storage
from shop import Shop
from store import Store

items_storage = {
    "собачки": 25,
    "cherry": 1,
    "коробки": 1,
    "шина": 1,
}

items_shop = {
    "печеньки": 5,
    "собачки": 5,
    "масло": 1
}

items_store = {
    "печеньки": 1,
    "собачки": 1
}

all_locations = [
    {
        "name": "склад",
        "items": items_storage,
        "class": Storage(items_storage)
    },
    {
        "name": "ларек",
        "items": items_store,
        "class": Store(items_store)
    },
    {
        "name": "магазин",
        "items": items_shop,
        "class": Shop(items_shop)
    },
]
