from request import Request
from storage import Storage
from store import Store
from shop import Shop


items = {
    "собачки": 1,
    "cherry": 1,
    "коробки": 1,
    "oil": 1,
    "печеньки": 5
}


def go():
    print(items)
    store = Store(items, 200)
    # Ввод команды
    text = input("введите предложение: ")
    # Создание обьекта запроса
    request = Request(text, items)
    # создание запроса в виде словаря
    req_data = request.parser_request()
    # получение имени продукта и количества
    product = req_data["product"]
    amount = req_data.get('amount')
    # создание объктов откуда и куда


    if from_obj.remove(product, amount) <= items[product]:
        print(f"Нужное количество есть на {req_data['from']}")
        print(f"Курьер забрал {amount} {product} со {req_data['from']}a")
        print(f"Курьер везет {amount} {product} со {req_data.get('from')}а в {req_data.get('to')}")
        print(f"Курьер доставил {amount} {product} в {req_data.get('to')}")
    # from_obj.remove(product, amount)
    return items

print(go())
