from __future__ import print_function
from sys import maxint
from itertools import cycle
from server import Server, UnavailableSlot

class Colors(object):
    END = '\033[1;m'
    HGREEN = '\033[1;42m'
    HRED = '\033[1;41m'
    HBROWN = '\033[1;43m'
    HBLUE = '\033[1;44m'

class DataCenter2(object):
    def __init__(self, rows, row_count, slot_count, pool_count):
        self.rows = rows
        self.row_count = row_count
        self.slot_count = slot_count
        self.pool_count = pool_count

        self.pools = [Pool(i) for i in range(pool_count)]

    def set(self, row_index, slot_index, server):
        if not self.has_required_space(row_index, slot_index, server):
            return False

        
        for i in xrange(server.size):
            self.rows[row_index][slot_index + i] = server

        server.row_index = row_index
        server.slot_index = slot_index

        return True

    def has_required_space(self, row_index, slot_index, server):
        if slot_index + server.size > self.slot_count:
            return False
        for i in xrange(server.size):
            if self.rows[row_index][slot_index + i]:
                return False
        return True

    def pool_with_lowest_minimum_capacity(self):
        lowest_mimimum_capacity, pool_id = min((pool.minimum_capacity(), pool.id) for pool in self.pools)

        return self.pools[pool_id]

    def get_score(self):
        score = maxint 

        for pool in self.pools:
            row_indexes = set(server.row_index for server in pool.servers)

            for row_index in row_indexes:
                min_cap = sum(server.capacity for server in pool.servers if server.row_index != row_index)
                if min_cap < score:
                    score = min_cap
                    print(pool.id)

                    #print(sum(server.capacity for server in pool.servers if server.row_index != row_index))
                    #print(sum(server.capacity for server in pool.servers if server.row_index == row_index))
                    #print(max(server.capacity for server in pool.servers))
                    #print("---")
        return score

    def show(self):
        color_iterator = cycle([Colors.HBROWN, Colors.HBLUE])
        ll = []
        for row in self.rows:
            server = None
            color = color_iterator.next()
            for slot in row:
                if isinstance(slot, UnavailableSlot):
                    print("%s  %s" % (Colors.HRED, Colors.END), end='')
                elif isinstance(slot, Server):
                    if slot != server:
                        color = color_iterator.next()
                        server = slot 
                        if server.pool == 35:
                            ll.append(server.capacity)
                            print("%s%2d%s" % ('', slot.pool, ''), end='')
                        else:
                            print("%s%2d%s" % (color, slot.pool, Colors.END), end='')
                    else:
                        if server.pool == 35:
                            print("  ", end='')
                        else:
                            print("%s  %s" % (color, Colors.END), end='')
                else:
                    print("%s  %s" % (Colors.HGREEN, Colors.END), end='')
            print()
        print(ll)

class Pool(object):
    def __init__(self, id):
        self.id = id
        self.servers = []

    def add(self, server):
        self.servers.append(server)

    def total_capacity(self):
        if not self.servers:
            return 0
        return sum(server.capacity for server in self.servers)

    def minimum_capacity(self):
        if not self.servers:
            return 0
        return sum(server.capacity for server in self.servers) - max(server.capacity for server in self.servers)

    def is_empty(self):
        return not self.servers

def magic(data_center, servers, pool_count):
    # Replace stupid DataCenter object with superior object
    data_center = DataCenter2(data_center.rows, len(data_center.rows), data_center.slots, pool_count)

    # Distribute servers to pool based on minimal capacity
    temp_servers = servers[:]
    while servers:
        for server in servers[:]:
            pool = next((pool for pool in data_center.pools if pool.is_empty()), False)
            if pool:
                pool.add(server)
                server.pool = pool.id
                servers.remove(server)
            else:
                pool = data_center.pool_with_lowest_minimum_capacity()
                pool.add(server)
                server.pool = pool.id
                servers.remove(server)

        #print(min(pool.total_capacity() for pool in data_center.pools))
        #print(max(pool.total_capacity() for pool in data_center.pools))
        #print(min(pool.minimum_capacity() for pool in data_center.pools))
        #print(max(pool.minimum_capacity() for pool in data_center.pools))
    # TODO: Optimize minimum capacity of pools

    # Distribute Servers over rows
    servers = temp_servers
    i = 0
    for server in servers:
        for row_id, row in enumerate(data_center.rows):
            for slot_id, slot in enumerate(row):
                #if isinstance(slot, Server) and slot.pool == server.pool:
                #    continue
                if data_center.has_required_space(row_id, slot_id, server):
                    data_center.set(row_id, slot_id, server)
                    break
            else:
                continue
            break
        else:
            i += 1
            continue

    print(data_center.get_score())
    data_center.show()





