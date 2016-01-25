from __future__ import print_function
from collections import defaultdict
from sys import maxint
from server import Server, UnavailableSlot
from itertools import cycle


class DataCenter(object):
    def __init__(self, rows, slots):
        self.slots = slots
        self.rows = [[None] * slots for i in xrange(rows)]

    @property
    def slot_indexes(self):
        for row_index, row in enumerate(self.rows):
            for slot_index in range(len(row)):
                yield (row_index, slot_index)

    def get(self, row_index, slot_index):
        return self.rows[row_index][slot_index]

    def has_required_space(self, row_index, slot_index, server):
        if slot_index + server.size > self.slots:
            return False
        for i in xrange(server.size):
            if self.get(row_index, slot_index + i):
                return False
        return True

    def set(self, row_index, slot_index, server):
        if not self.has_required_space(row_index, slot_index, server):
            return False

        for i in xrange(server.size):
            self.rows[row_index][slot_index + i] = server
            server.row_index = row_index
            server.slot_index = slot_index

        return True

    @property
    def servers(self):
        servers = set()
        for row in self.rows:
            for slot in row:
                if isinstance(slot, Server):
                    servers.add(slot)
        return servers

    def get_score(self):
        pools = defaultdict(list)
        for server in self.servers:
            if server.pool:
                pools[server.pool].append(server)

        min_guaranteed_capacity = maxint
        p = -1
        for pool, servers in pools.iteritems():
            for row_index, row in enumerate(self.rows):
                capacity = 0
                for server in servers:
                    if server.row_index != row_index:
                        capacity += server.capacity
                if capacity < min_guaranteed_capacity:
                    p = server.pool
                min_guaranteed_capacity = min(min_guaranteed_capacity, capacity)

        return min_guaranteed_capacity, p

    def show(self, pool):
        end = "\033[1;m"
        color_iterator = cycle(['\033[1;43m', '\033[1;44m'])
        for row in self.rows:
            server = None
            color = color_iterator.next()
            for slot in row:
                if isinstance(slot, UnavailableSlot):
                    print("\033[1;41m  %s" % end, end='')
                elif isinstance(slot, Server):
                    if slot != server:
                        color = color_iterator.next()
                        print("%s%2d%s" % (color, slot.pool, end), end='')
                    else:
                        print("%s  %s" % (color, end), end='')
                    server = slot
                else:
                    print("%s  %s" % ("\033[1;42m", end), end='')
            i = 0
            for s in row:
                if isinstance(s, Server):  # and s.pool == pool:
                    i += s.capacity / float(s.size)
            # i = sum([s.capacity if isinstance(s, Server) and s.pool == pool else 0 for s in row])
            print(" %3d" % i)
