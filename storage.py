from abstr import AbcStore


class Storage(AbcStore):
    name = "склад"

    def __init__(self, items: dict, capacity=100):
        super().__init__(items, capacity)

    def add(self, product: str, amount: int) -> bool:
        new_count = self.capacity - self._get_free_space() + amount
        if new_count <= self.capacity:
            if product in self.items:
                self.items[product] += amount
                return True
            elif product not in self.items:
                self.items[product] = amount
                return True
            else:
                return False

    def remove(self, product: str, amount: int):
        new_count = self.items[product] - amount
        if new_count >= 0:
            self.items[product] -= amount
            return True

    def _get_free_space(self) -> int:
        " Возвращает количество свобоных мест"
        return self.capacity - sum(quantity for quantity in self._get_items().values())

    def _get_items(self) -> dict:
        """Возвращиет items"""
        return self.items

    @property
    def _get_unique_items_count(self) -> int:
        """Возвращает количество уникальных товаров"""
        return len(self.items)
