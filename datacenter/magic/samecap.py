from random import shuffle
from sys import maxint


def magic(data_center, servers, pool_count):
    # Make pools of equal capacity
    pools = [[] for i in xrange(pool_count)]
    servers_copy = servers[:]
    while servers_copy:
        shuffle(pools)
        max_cap = None
        for i, pool in enumerate(pools):
            if i == 0:
                biggest_server = sorted(servers_copy, key=lambda s: s.capacity)[-1]
                biggest_server.pool = i
                pool.append(biggest_server)
                servers_copy.remove(biggest_server)
                max_cap = max(sum(s.capacity for s in pool) for pool in pools)
            else:
                pool_cap = sum(s.capacity for s in pool)
                best_diff = 1000000000
                best_diff_server = None
                for server in servers_copy:
                    diff = abs(max_cap - (pool_cap + server.capacity))
                    if diff < best_diff:
                        best_diff = diff
                        best_diff_server = server
                if best_diff_server:
                    best_diff_server.pool = i
                    pool.append(best_diff_server)
                    servers_copy.remove(best_diff_server)

    for row_index, row in enumerate(data_center.rows):
        for slot_index in xrange(len(row)):
            shuffle(pools)
            for pool in pools:
                for server in pool:
                    if data_center.set(row_index, slot_index, server):
                        pool.remove(server)
                        break

    for pool in pools:
        for server in pool:
            server.pool = None
