class Simulator:
    @classmethod
    def from_file(cls, path):
        with open(path) as f:
            rows, columns, drones, turns, max_payloud = map(int, f.readline().split())
            product_count = int(f.readline())
            product_weights = map(int, f.readline().split())

