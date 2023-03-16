from store import Store
from storage import Storage
from shop import Shop

text = "Доставить 3 печеньки из склад в магазин"

class Request:
    all_cls = [Storage, Shop, Store]
    def __init__(self, text):
        self.text = text.split()
        self.f = self.text[4]
        self.amount = self.text[1]
        self.to = self.text[6]
        self.product = self.text[3]

    def get_req(self):
        req = {}
        req["from"] = self.f
        req["amount"] = self.amount
        req["to"] = self.to
        req["product"] = self.product
        return req



    # def get_request(self):
    #     req = {}
    #     a = self.text.split()
    #     req["f"]=a[4]
    #     req["amount"]=a[1]
    #     req["to"] = a[6]
    #     req["product"] = a[3]
    #
    #     return req

req = Request(text)

print(req.get_req())




