from request import Request
from storage import Storage
from store import Store
from shop import Shop
from utils import Utils, items, items_shop



def go():
    utilite = Utils(items, items_shop)

    # создание запроса в виде словаря
    req_data = utilite.get_req_data
    # получение имени продукта и количества
    product = req_data["product"]
    amount = req_data.get('amount')
    # создание объктов откуда и куда
    from_obj = utilite.get_from(req_data)

    to_obj = utilite.get_to(req_data)

    if from_obj.remove(product, amount):
        if to_obj.add(product, amount):
            print(f"Нужное количество есть на {req_data['from']}")
            print(f"Курьер забрал {amount} {product} со {req_data['from']}a")
            print(f"Курьер везет {amount} {product} со {req_data.get('from')}а в {req_data.get('to')}")
            print(f"Курьер доставил {amount} {product} в {req_data.get('to')}")

        else:
            return print("В магазин недостаточно места, попобуйте что то другое")
    else:
        return print('Не хватает на складе, попробуйте заказать меньше')

    print( "В склад хранится:\n"+"\n".join(f"{item}" for item in items.items()))
    print( "В магазине хранится:\n"+"\n".join(f"{item}" for item in items_shop.items()))


go()
