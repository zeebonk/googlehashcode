from collections import defaultdict
from sys import maxint


class NoSpaceAvailableError(Exception):
    pass


class DataCenter(object):
    def __init__(self, rows, slots):
        self.rows = [[None] * slots for i in xrange(rows)]

    @property
    def slot_indexes(self):
        slot_indexes = list()
        for row_index, row in enumerate(self.rows):
            for slot_index in range(len(row)):
                slot_indexes.append((row_index, slot_index))
        return slot_indexes

    def get(self, row_index, slot_index):
        return self.rows[row_index][slot_index]

    def has_required_space(self, row_index, slot_index, server):
        for i in xrange(server.size if server else 1):
            if self.get(row_index, slot_index + i):
                return False
        return True

    def set(self, row_index, slot_index, server):
        if not self.has_required_space(row_index, slot_index, server):
            raise NoSpaceAvailableError("At row %d slot %d" % (row_index, slot_index + 1))

        for i in xrange(server.size if server else 1):
            self.rows[row_index][slot_index + i] = server
            server.row_index = row_index
            server.slot_index = slot_index

    @property
    def servers(self):
        servers = set()
        for row in self.rows:
            for slot in row:
                if slot:
                    servers.add(slot)
        return servers

    def get_score(self):
        pools = defaultdict(list)
        for server in self.servers:
            if server.pool:
                pools[server.pool].append(server)

        min_guaranteed_capacity = maxint
        for pool, servers in pools.iteritems():
            for row_index, row in enumerate(self.rows):
                capacity = 0
                for server in servers:
                    if server.row_index != row_index:
                        capacity += server.capacity
                min_guaranteed_capacity = min(min_guaranteed_capacity, capacity)

        return min_guaranteed_capacity
