from random import shuffle

def magic(data_center, servers):
    random.shuffle(servers)

    for server in servers:
        for row in range(len(data_center.rows)):
            for slot in range(data_center.slots):
                if data_center.has_required_space(row, slot, server):
                    data_center.set(row, slot, server)
                    break
            else:
                break
