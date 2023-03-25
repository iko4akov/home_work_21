from request import Request

def go():
    text = input("введите предложение: ")
    req = Request(text)
    # создание запроса в виде словаря
    req_dict = req.get_req_data()

    # получение имени продукта и количества
    product = req_dict["product"]
    amount = req_dict['amount']

    from_data = req.get_items(req_dict['from'])

    to_data = req.get_items(req_dict['to'])


    from_obj = from_data['class']
    to_obj = to_data['class']

    if from_obj.remove(product=product, amount=amount):
        if to_obj.add(product, amount):
            print(f"Нужное количество есть на {req_dict['from']}")
            print(f"Курьер забрал {amount} {product} со {req_dict['from']}a")
            print(f"Курьер везет {amount} {product} со {req_dict.get('from')}а в {req_dict.get('to')}")
            print(f"Курьер доставил {amount} {product} в {req_dict.get('to')}")
        else:
            return print(f"В {to_data['to']} недостаточно места, попобуйте что то другое")
    else:
        return print(f' {from_data["name"]} нет в(на) {from_data["from"]}, попробуйте заказать меньше')

    print(f"На {from_data['name']}е хранится:\n" + "\n".join(f"{item[0]}: {item[1]}" for item in from_obj.items.items()))
    print(f"В {to_data['name']}е хранится:\n" + "\n".join(f"{item[0]}: {item[1]}" for item in to_obj.items.items()))

if __name__ == '__main__':
    go()
