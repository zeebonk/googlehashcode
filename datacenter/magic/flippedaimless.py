from random import shuffle, randint

def magic(data_center, servers, pool_count):
    shuffle(servers)

    s = servers[:]
    i = 0

    for row_index, slot_index in data_center.slot_indexes:
        for server in s:
            if data_center.has_required_space(row_index, slot_index, server):
                data_center.set(row_index, slot_index, server)

                if i < pool_count:
                    server.pool = i+1
                else:
                    server.pool = randint(1, pool_count)
                i+= 1
                s.remove(server)
                break
