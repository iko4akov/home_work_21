from store import Store


class Storage(Store):
    def __init__(self, items: dict, capacity=100):
        super().__init__(items, capacity)


# items = {
#     "apple": 1,
#     "cherry": 1,
#     "fruit": 1,
#     "oil": 1,
#     "печеньки": 5
# }
#
# storage = Storage(items)
#
# stoage.add("apple", 1)
# stoage.remove("oil", 1)
#
# print(stoage.get_free_space)
# print(stoage.get_items)
# print(stoage.get_unique_items_count)
