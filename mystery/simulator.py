from warehouse import Warehouse


class Simulator:
    def __init__(self, path):
        self.warehouses = []
        self.orders = []

        with open(path) as f:
            self.rows, self.columns, self.drones, self.turns, self.max_payloud = map(int, f.readline().split())
            product_count = int(f.readline())
            product_weights = map(int, f.readline().split())

            warehouse_count = int(f.readline())
            for i in range(warehouse_count):
                r, c = map(int, f.readline().split())
                products = map(int, f.readline().split())
                Warehouse(r, c, products)

            order_count = int(f.readline())
            for i in range(order_count):
                r, c = map(int, f.readline().split())
                product_count = int(f.readline())
                products = map(int, f.readline().split())
