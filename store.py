from abc import ABC


class Store(ABC):
    def __init__(self, items: dict, capacity: int):
        self.items = items
        self.capacity = capacity


    def add(self, name: str, count: int):
        new_count = self.capacity - self.get_free_space + count
        if new_count <= self.capacity:
            self.items[name] += count
        else:
            return print(F"На складе нет столько места, осталось мест: {self.get_free_space}")


    def remove(self, name: str, count: int):
        new_count = self.capacity - self.get_free_space - count
        if new_count >= 0:
            self.items[name] -= count
        else:
            return print(f"На складе нет столько товара, осталось товара: {self.capacity - self.get_free_space}")


    @property
    def get_free_space(self) -> int:
        return self.capacity - sum(quantity for quantity in self.items.values())


    @property
    def get_items(self) -> str:
        return "\n".join([f"{item}: {self.items[item]}" for item in self.items])


    @property
    def get_unique_items_count(self) -> int:
        return len(self.items)







