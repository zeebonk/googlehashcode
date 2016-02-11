from collections import Counter, defaultdict


class Drone:
    def __init__(self, id, max_payload, r, c):
        self.id = id
        self.weight = 0
        self.max_payload = max_payload
        self.r = r
        self.c = c

        self.storage = defaultdict(Counter)

    def has_storage(self):
        for key in self.storage.keys():
            if sum(self.storage[key].values()) > 0:
                return True
        return False
