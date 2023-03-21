from storage import Storage
from shop import Shop
from store import Store
from utils import items_storage, items_shop

class Request:
    all_location = [Storage, Shop, Store]
    def __init__(self, text: str):
        self.text = text.split()

    # @property
    def get_req_data(self) -> dict:
        # создание запроса в виде словаря
        req_data = self._parser_request()
        return req_data

    def _parser_request(self):
        req_data = {}
        for i in range(len(self.text)):

            if self.text[i] == "со" or self.text[i] == "из":
                req_data["from"] = self.text[i + 1]

            if self.text[i] == "в":
                req_data['to'] = self.text[i + 1]

            if self.text[i] in items_storage.keys():
                req_data['product'] = self.text[i]

            if self.text[i].isdigit():
                req_data['amount'] = int(self.text[i])
        return req_data


    def from_obj(self):
        """Создание объекта нужного класса из которого забирается продукт"""
        for obj in self.all_location:
            if self._parser_request()['from'] == obj.name:
                from_object = obj(items_storage)
                return from_object

    def to_obj(self):
        for obj in self.all_location:
            if self._parser_request()['to'] == obj.name:
                to_object = obj(items_shop)
                return to_object
