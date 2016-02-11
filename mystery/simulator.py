from order import Order
from warehouse import Warehouse


class Simulator:
    def __init__(self, path, algorithm):
        self.algorithm = algorithm
        self.warehouses = []
        self.orders = []
        self.busy_drones = []
        self.free_drones = []

        with open(path) as f:
            self.rows, self.columns, self.drone_count, self.turns, self.max_payloud = map(int, f.readline().split())
            product_count = int(f.readline())
            product_weights = map(int, f.readline().split())

            warehouse_count = int(f.readline())
            for i in range(warehouse_count):
                r, c = map(int, f.readline().split())
                products = map(int, f.readline().split())

                self.warehouses.append(Warehouse(r, c, products))

            order_count = int(f.readline())
            for i in range(order_count):
                r, c = map(int, f.readline().split())
                product_count = int(f.readline())
                products = map(int, f.readline().split())

                self.orders.append(Order(r, c, products))

    		self.free_drones = range(self.drone_count)

    def simulate(self, args):
        i = 0
        while i < self.turns and self.orders:
            i += 1

            new_busy_drones = []
            for drone, turns in busy_drones:
            	turns -= 1
            	if turns == 0:
            		self.free_drones.append(drone)
        		else:
        			new_busy_drones.append(drone, turns)
			self.busy_drones = new_busy_drones

            self.algorithm(self, args)
            if self.free_drones:
            	raise Exception("All drones must be assigned to a task")
