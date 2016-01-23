class Server(object):
    UNAVAILABLE = 0

    def __init__(self, size, capacity):
        self.size = size
        self.capacity = capacity
        self.pool = None
        self.row_index = None
        self.slot_index = None


class UnavailableSlot(object):
    def __init__(self):
        self.size = 1
        self.row_index = None
        self.slot_index = None

    def __nonzero__(self):
        return False
