from abc import ABC, abstractmethod

class AbcStore(ABC):
    def __init__(self, items: dict, capacity: int):
        self.items = items
        self.capacity = capacity

    @property
    @abstractmethod
    def add(self, name: str, count: int):
        """ Увеличивает количесто в items товара product на количесто count"""
        pass

    @property
    @abstractmethod
    def remove(self, product: str, count: int):
        """ Уменьшает количесто в items товара product на количесто count"""
        pass

    @property
    @abstractmethod
    def get_free_space(self) -> int:
        " Возвращает количество свобоных мест"
        pass

    @property
    @abstractmethod
    def get_items(self) -> dict:
        """Возвращиет items"""
        pass

    @property
    @abstractmethod
    def get_unique_items_count(self) -> int:
        "Возвращает количество уникальных товаров"
        pass
