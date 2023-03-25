from storage import Storage


class Shop(Storage):
    name = "магазин"


    def __init__(self, items: dict, capacity=20):
        super().__init__(items, capacity)


    def add(self, product: str, count: int):

        if count <= self.get_free_space and product in self.items:
            self.items[product] += count
            return True
        elif count <= self.get_free_space and product not in self.items and self._get_unique_items_count <= 4:
            self.items[product] = count
            return True

    def remove(self, product: str, amount: int):
        if product in self.items:
            new_count = self.capacity - self.get_free_space - amount
            if new_count >= 0:
                self.items[product] -= amount
                return True
