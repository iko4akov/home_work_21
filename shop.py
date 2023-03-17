from store import Store


class Shop(Store):
    def __init__(self, items: dict, capacity=20):
        super().__init__(items, capacity)

    def add(self, product: str, count: int):

        if count <= self.get_free_space and product in self.items:
            self.items[product] += count
            return True
        elif count <= self.get_free_space and product not in self.items and self.get_unique_items_count <= 4:
            self.items[product] = count
            return True

    def remove(self, name: str, count: int):
        if name in self.items:
            new_count = self.capacity - self.get_free_space - count
            if new_count >= 0:
                self.items[name] -= count
        else:
            return print(f"В магазине нет столько товара, осталось товара: {self.capacity - self.get_free_space}")
