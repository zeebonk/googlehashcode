from math import sqrt, ceil
from order import Order
from warehouse import Warehouse
from drone import Drone


class Simulator:
    def __init__(self, path, algorithm):
        self.algorithm = algorithm
        self.warehouses = []
        self.orders = []
        self.busy_drones = []
        self.free_drones = []

        self.commands = []

        with open(path) as f:
            self.rows, self.columns, self.drone_count, self.turns, self.max_payload = map(int, f.readline().split())
            # print(self.rows, self.columns, self.drone_count, self.turns, self.max_payload)
            product_count = int(f.readline())
            self.product_weights = list(map(int, f.readline().split()))

            warehouse_count = int(f.readline())
            for i in range(warehouse_count):
                r, c = list(map(int, f.readline().split()))
                products = list(map(int, f.readline().split()))

                self.warehouses.append(Warehouse(i, r, c, products))

            order_count = int(f.readline())
            for i in range(order_count):
                r, c = list(map(int, f.readline().split()))
                product_count = int(f.readline())
                products = list(map(int, f.readline().split()))

                self.orders.append(Order(i, r, c, products))

            for i in range(self.drone_count):
                self.free_drones.append(Drone(i, self.max_payload, self.warehouses[0].r, self.warehouses[0].c))

    def simulate(self, args):
        self.i = -1
        while self.i < self.turns - 1 and self.orders:
            self.i += 1
            print(self.i)

            # Update busy drone state
            new_busy_drones = []
            for drone, turns in self.busy_drones:
                turns -= 1
                if turns == 0:
                    self.free_drones.append(drone)
                else:
                    new_busy_drones.append((drone, turns))
            self.busy_drones = new_busy_drones

            self.algorithm(self, args)

            if self.free_drones:
                raise Exception("All drones must be assigned to a task")

    def load(self, drone, order, warehouse, product_id, product_count):
        if drone not in self.free_drones:
            raise Exception("Can only command free drones")

        if warehouse.products[product_id] < product_count:
            raise Exception("Not enough products in warehouse")

        if order.products[product_id] < product_count:
            raise Exception("Not enoug products in order")

        order.products[product_id] -= product_count

        drone.storage[order.id][product_id] += product_count
        drone.weight = self.product_weights[product_id] * product_count

        if drone.weight > self.max_payload:
            raise Exception("Drone overloaded")

        if drone.weight < 0:
            raise Exception("Drone negative load")

        turns = int(ceil(sqrt((drone.r - order.r)**2 + (warehouse.c - warehouse.c)**2)) + 1)

        drone.r = warehouse.r
        drone.c = warehouse.c
        self.free_drones.remove(drone)
        self.busy_drones.append((drone, turns))

        self.commands.append("%d L %d %d %d" % (drone.id, warehouse.id, product_id, product_count))

    def deliver(self, drone, order, product_id, product_count):
        if drone.storage[order.id][product_id] < product_count:
            raise Exception("Not enough products in drone")

        drone.storage[order.id][product_id] -= product_count

        turns = int(ceil(sqrt((drone.r - order.r)**2 + (drone.c - order.c)**2)) + 1)

        drone.r = order.r
        drone.c = order.c
        self.free_drones.remove(drone)
        self.busy_drones.append((drone, turns))

        self.commands.append("%d D %d %d %d" % (drone.id, order.id, product_id, product_count))

    def wait(self, drone, turns):
        if drone not in self.free_drones:
            raise Exception("Can only command free drones")

        turns = min(turns, self.turns - self.i)

        self.free_drones.remove(drone)
        self.busy_drones.append((drone, turns))

        self.commands.append("%d W %d" % (drone.id, turns))

    def get_output(self):
        lines = []
        lines.append(str(len(self.commands)))
        lines.extend(self.commands)
        return '\n'.join(lines)
