from store import Store


class Storage(Store):
    def __init__(self, items: dict, capacity=100):
        super().__init__(items, capacity)
