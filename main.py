from request import Request


def go():
    text = input("Введите предложение: ")
    while text.lower().strip() != 'стоп':
        req = Request(text)

        request_dict = req.get_req_data()

        from_data: dict = req.get_items(request_dict['from'])
        to_data: dict = req.get_items(request_dict['to'])

        try:
            product = request_dict["product"]
        except KeyError:
            print(f'нет такого товара в {from_data["name"]}')

        try:
            amount = request_dict['amount']
        except KeyError:
            print(f'не указано количество товара')

        from_obj = from_data['class']
        to_obj = to_data['class']

        if from_obj.remove(product, amount):
            if to_obj.add(product, amount):
                print(f"Нужное количество есть на {request_dict['from']}")
                print(f"Курьер забрал {amount} {product} со {request_dict['from']}a")
                print(f"Курьер везет {amount} {product} со {request_dict.get('from')}а в {request_dict.get('to')}")
                print(f"Курьер доставил {amount} {product} в {request_dict.get('to')}")
            else:
                return print(f"В {to_data['name']} недостаточно места, попобуйте что то другое")
        else:
            return print(f'{from_data["name"]} нет в(на) {from_data["name"]}, попробуйте заказать меньше')

        print(f"На {from_data['name']}е хранится:\n" + "\n".join(
            f"{item[0]}: {item[1]}" for item in from_obj.items.items()))
        print(f"В {to_data['name']}е хранится:\n" + "\n".join(f"{item[0]}: {item[1]}" for item in to_obj.items.items()))

        text = input("Введите предложение: ")


if __name__ == '__main__':
    go()
