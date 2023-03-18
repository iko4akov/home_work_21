from storage import Storage
from shop import Shop
from store import Store


class Request:
    all_location = [Storage, Shop, Store]
    def __init__(self, text: str, items: dict):
        self.all_cls = [Storage, Shop, Store]
        self.items = items
        self.text = text.split()
        self.data = self.parser_request()

    def parser_request(self):
        req_data = {}
        for i in range(len(self.text)):

            if self.text[i] == "со" or self.text[i] == "из":
                req_data["from"] = self.text[i + 1]

            if self.text[i] == "в":
                req_data['to'] = self.text[i + 1]

            if self.text[i] in self.items.keys():
                req_data['product'] = self.text[i]

            if self.text[i].isdigit():
                req_data['amount'] = int(self.text[i])

        if "to" not in req_data:
            if req_data["from"].startswith("скла"):
                req_data['to'] = "магазин"

            if req_data["from"].startswith("магаз"):
                req_data['to'] = "склад"

        if "from" not in req_data:
            if req_data["to"].startswith("скла"):
                req_data['from'] = "магазин"

            if req_data["to"].startswith("магаз"):
                req_data['from'] = "склад"

        return req_data
