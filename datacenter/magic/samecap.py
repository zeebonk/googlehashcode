from random import shuffle
from sys import maxint


def magic(data_center, servers, pool_count):
    # Make pools of equal capacity
    pools = [[] for i in xrange(pool_count)]
    while servers:
        shuffle(pools)
        max_cap = None
        for i, pool in enumerate(pools):
            if i == 0:
                biggest_server = sorted(servers, key=lambda s: s.capacity)[-1]
                pool.append(biggest_server)
                servers.remove(biggest_server)
                max_cap = max(sum(s.capacity for s in pool) for pool in pools)
            else:
                pool_cap = sum(s.capacity for s in pool)
                best_diff = 1000000000
                best_diff_server = None
                for server in servers:
                    diff = abs(max_cap - (pool_cap + server.capacity))
                    if diff < best_diff:
                        best_diff = diff
                        best_diff_server = server
                if best_diff_server:
                    servers.remove(best_diff_server)
                    pool.append(best_diff_server)

    # Distribute distribute servers HERE
