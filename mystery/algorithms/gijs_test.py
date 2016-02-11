from simulator import Simulator


def find_load(simulator, drone):
    for order in simulator.orders:
        for product_id, product_count in order.products.items():
            for warehouse in simulator.warehouses:
                if warehouse.products[product_id] > 0:
                    return (drone, order, warehouse, product_id, min(warehouse.products[product_id], product_count))
    return None


def algorithm(simulator, args):
    for drone in simulator.free_drones[:]:
        if drone.has_storage():
            order_id = list(drone.storage.keys())[0]
            product_id = list(drone.storage[order_id].keys())[0]
            product_count = drone.storage[order_id][product_id]
            order = list(filter(lambda o: o.id == order_id, simulator.orders))[0]
            simulator.deliver(drone, order, product_id, 1)
        else:
            load = find_load(simulator, drone)
            if not load:
                simulator.wait(drone, 100000000000)
            simulator.load(*load)
