from random import shuffle


def magic(data_center, servers, pool_count):
    servers = sorted(servers, key=lambda s: s.capacity / s.size)
    row_indexes = [0] * len(data_center.rows)
    pool_index = 0
    rows_copy = [pair for pair in enumerate(data_center.rows)]
    shuffle(rows_copy)
    placed_server = True

    while placed_server:
        placed_server = False
        for row_index, row in rows_copy:
            for server in servers:
                if data_center.set(row_index, row_indexes[row_index], server):
                    row_indexes[row_index] += server.size
                    servers.remove(server)
                    placed_server = True
                    if pool_index < pool_count:
                        server.pool = pool_index
                    else:
                        server.pool = pool_index % pool_count
                    pool_index += 1
                    break
            else:
                row_indexes[row_index] += 1
