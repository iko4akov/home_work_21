from storage import Storage

class Store(Storage):
    def __init__(self, items: dict, capacity=100):
        super().__init__(items, capacity)
