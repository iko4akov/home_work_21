from shop import Shop
from storage import Storage
from request import Request

items = {
    "собачки": 23,
    "cherry": 1,
    "коробки": 1,
    "oil": 1,
    "печеньки": 5
}

items_shop = {
    "oil": 1,
    "печеньки": 5,
    "собачки": 5

}


class Utils:

    def __init__(self, items: dict, items_shop: dict):
        self.items = items
        self.items_shop = items_shop
        self.text = self.get_text

    @property
    def get_text(self) -> str:
        """Ввод команды от пользователя"""
        text = input("введите предложение: ")
        return text

    @property
    def obj_request(self) -> Request:
        # Создание обьекта запроса
        request = Request(self.text, self.items)
        return request

    @property
    def get_req_data(self) -> dict:
        # создание запроса в виде словаря
        req_data = self.obj_request.parser_request()
        return req_data

    def get_from(self, data: dict) -> Storage or Shop:
        if data["from"].startswith("скла"):
            storage = Storage(self.items)
            return storage

        if data["from"].startswith("магаз"):
            shop = Shop(self.items_shop)
            return shop

    def get_to(self, data: dict) -> Storage or Shop:
        if data["to"].startswith("скла"):
            storage = Storage(self.items)
            return storage

        if data["to"].startswith("магаз"):
            shop = Shop(self.items_shop)
            return shop
