from warehouse import Warehouse


class Simulator:
    @classmethod
    def from_file(cls, path):
        with open(path) as f:
            rows, columns, drones, turns, max_payloud = map(int, f.readline().split())
            product_count = int(f.readline())
            product_weights = map(int, f.readline().split())

            warehouse_count = int(f.readline())
            for i in range(warehouse_count):
                r, c = map(int, f.readline().split())
                products = map(int, f.readline().split())
                Warehouse(r, c, products)

            order_count = int(f.readline())
            for i in range(order_count):
                pass
