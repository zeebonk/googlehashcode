import sys
from itertools import cycle

with open(sys.argv[1]) as f:
    rows, columns, drone_count, turns, max_payloud = map(int, f.readline().split())
    product_count = int(f.readline())
    product_weights = map(int, f.readline().split())

    warehouses = []
    warehouse_count = int(f.readline())
    for i in range(warehouse_count):
        r, c = map(int, f.readline().split())
        products = list(map(int, f.readline().split()))

        warehouses.append((r, c, products))

    orders = []
    order_count = int(f.readline())
    for i in range(order_count):
        r, c = map(int, f.readline().split())
        product_count = int(f.readline())
        products = list(map(int, f.readline().split()))

        orders.append((i, r, c, products))


drones = cycle(range(drone_count))
i = 0
commands = []
for o, order in enumerate(orders):
    for item in order[3]:
        drone = next(drones)
        for w, warehouse in enumerate(warehouses):
            if warehouse[2][item] > 1:
                warehouse[2][item] -= 1

                commands.append("%d L %d %d %d" % (drone, w, item, 1))
                commands.append("%d D %d %d %d" % (drone, o, item, 1))
                i+=2
                break

print(i)
for command in commands:
    print(command)
