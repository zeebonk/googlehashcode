from random import shuffle


def magic(data_center, servers, pool_count):
    servers = sorted(servers, key=lambda s: s.capacity/s.size)

    row_indexes = [0] * len(data_center.rows)
    pool_i = 0
    rows_copy = [pair for pair in enumerate(data_center.rows)]
    shuffle(rows_copy)

    while True:
        l = len(servers)
        for row_index, row in rows_copy:
            for server in servers:
                if data_center.has_required_space(row_index, row_indexes[row_index], server):
                    data_center.set(row_index, row_indexes[row_index], server)
                    row_indexes[row_index] += server.size
                    servers.remove(server)

                    if pool_i < pool_count:
                        server.pool = pool_i
                    else:
                        server.pool = pool_i % pool_count
                    pool_i += 1

                    break
            else:
                row_indexes[row_index] += 1
        if len(servers) == l:
            break
