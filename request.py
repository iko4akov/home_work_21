from utils import all_locations


class Request:
    def __init__(self, text: str, all_location: list = all_locations):
        self.text = text.lower().split()
        self.all_location = all_location

    def get_req_data(self) -> dict:
        req_data = self._parser_request()
        request = self._get_product_from(req_data)
        return request

    def _get_product_from(self, request: dict) -> dict:
        for i in range(len(self.text)):
            if self.text[i] in self.get_items(request['from'])['items'].keys():
                request['product'] = self.text[i].lower()
        return request

    def _parser_request(self) -> dict:
        req_data = {}
        for i in range(len(self.text)):
            if self.text[i] == "в" or self.text[i] == "на":
                req_data['to'] = self.text[i + 1].lower()

            if self.text[i].isdigit():
                req_data['amount'] = int(self.text[i])

            if self.text[i] == "со" or self.text[i] == "из":
                req_data["from"] = self.text[i + 1].lower()
        return req_data

    def get_items(self, location: str) -> dict:
        """Получение спловаря с товарами в определенной локации"""
        for loc in self.all_location:
            if loc['name'] == location:
                return loc
