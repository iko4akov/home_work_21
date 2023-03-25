from utils import all_locations

class Request:

    def __init__(self, text: str, all_location=all_locations):
        self.text = text.split()
        self.all_location = all_location

    def get_req_data(self) -> dict:
        # создание запроса в виде словаря
        req_data = self._parser_request()
        return req_data

    def _parser_request(self):
        req_data = {}
        for i in range(len(self.text)):

            if self.text[i] == "со" or self.text[i] == "из":
                req_data["from"] = self.text[i+1]

            if self.text[i] == "в":
                req_data['to'] = self.text[i + 1]

            from_location = req_data['from']
            if self.text[i] in self.get_items(from_location)['items'].keys():
                req_data['product'] = self.text[i]

            if self.text[i].isdigit():
                req_data['amount'] = int(self.text[i])
        return req_data

    def get_items(self, location: str) -> dict:
        """Получение спловаря с товарами в определенной локации"""
        for loc in self.all_location:
            if loc['name'] == location:
                return loc
