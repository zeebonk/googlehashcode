from collections import Counter


class Drone:
    def __init__(self, id, max_payloud, r, c):
        self.id = id
        self.max_payload = max_payloud
        self.r = r
        self.c = c

        self.storage = Counter()
