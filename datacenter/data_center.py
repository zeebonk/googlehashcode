class NoSpaceAvailableError(Exception):
    pass


class DataCenter(object):
    def __init__(self, rows, slots):
        self.rows = [[None] * slots for i in xrange(rows)]

    def get(self, row_index, slot_index):
        return self.rows[row_index][slot_index]

    def has_required_space(self, row_index, slot_index, server):
        for i in xrange(server.size):
            if self.get(row_index, slot_index + i):
                return False
        return True

    def set(self, row_index, slot_index, server):
        if not self.has_required_space(row_index, slot_index, server):
            raise NoSpaceAvailableError("At row %d slot %d" % (row_index, slot_index + 1))
        # Set server at all required slots
        for i in xrange(server.size):
            self.rows[row_index][slot_index + i] = server
            server.row_index = row_index
            server.slot_index = slot_index
