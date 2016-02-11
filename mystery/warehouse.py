from collections import Counter


class Warehouse:
    def __init__(self, id, r, c, products):
        self.id = id
        self.r = r
        self.c = c

        self.products = Counter(products)
