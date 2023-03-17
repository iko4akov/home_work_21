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
        # else:
        #     return print(f"В магазине нет столько места, осталось мест: {self.get_free_space},"
        #                  f"\nесли эта цифра ---> {self.get_unique_items_count} == 5,\n"
        #                  f"то количество уникальных товаров не может быть больше 5")

    def remove(self, name: str, count: int):
        if name in self.items:
            new_count = self.capacity - self.get_free_space - count
            if new_count >= 0:
                self.items[name] -= count
        else:
            return print(f"В магазине нет столько товара, осталось товара: {self.capacity-self.get_free_space}")



# items = {
#     "apple": 1,
#     "cherry": 1,
#     "fruit": 1,
#     "oil": 1
# }

# shop = Shop(items)
#
# shop.add("apple", 1)
# shop.add("tiers", 1)
#
#
# shop.remove("oil", 1)

# print(shop.get_free_space)
# print(shop.get_items)
# print(shop.get_unique_items_count)
