from request import Request
from exaptions import NotAmount, NotInListProduct


def go():
    while True:

        text = input("Введите предложение:")

        if text.lower().strip() == "стоп":
            break

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

        try:
            from_obj.remove(product=product, amount=amount)
            if to_obj.add(product, amount):
                print(f"Нужное количество есть на {request_dict['from']}")
                print(f"Курьер забрал {amount} {product} со {request_dict['from']}a")
                print(f"Курьер везет {amount} {product} со {request_dict.get('from')}а в {request_dict.get('to')}")
                print(f"Курьер доставил {amount} {product} в {request_dict.get('to')}")
            else:
                return print(f"В {to_data['name']} недостаточно места, попробуйте что то другое")

        except (NotAmount, NotInListProduct) as error:
            print(error.message)

        print(f"На {from_data['name']}е хранится:\n" + "\n".join(
            f"{item[0]}: {item[1]}" for item in from_obj.items.items()))
        print(f"В {to_data['name']}е хранится:\n" + "\n".join(f"{item[0]}: {item[1]}" for item in to_obj.items.items()))

if __name__ == '__main__':
    go()
