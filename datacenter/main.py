import importlib
import sys

from data_center import DataCenter
from server import Server, UnavailableSlot
from cStringIO import StringIO


def load_from_file(f):
    rows_count, slots_per_row, unavailable_count, pool_count, server_count = map(int, f.readline().split())
    data_center = DataCenter(rows_count, slots_per_row)
    for i in xrange(unavailable_count):
        row_id, slot_id = map(int, f.readline().split())
        data_center.set(row_id, slot_id, UnavailableSlot())
    servers = [map(int, f.readline().split()) for i in xrange(server_count)]
    servers = [Server(i, size, capacity) for i, (size, capacity) in enumerate(servers)]
    f.seek(0)
    return rows_count, slots_per_row, unavailable_count, pool_count, server_count, servers, data_center


if __name__ == "__main__":
    if len(sys.argv) < 4:
        quit("Usage - python %s file magic iterations" % sys.argv[0])

    iterations = int(sys.argv[3])
    input_file = StringIO(open(sys.argv[1]).read())
    magic = importlib.import_module('magic.' + sys.argv[2]).magic

    max_score = 0
    for i in xrange(iterations):
        rows_count, slots_per_row, unavailable_count, pool_count, server_count, servers, data_center = load_from_file(input_file)

        magic(data_center, servers[:], pool_count)

        score, pool = data_center.get_score()
        if score > max_score:
            print "Score", score
            data_center.show(pool)
            max_score = score
