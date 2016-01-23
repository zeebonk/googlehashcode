import sys
import importlib
from data_center import DataCenter
from server import Server, UnavailableSlot


if __name__ == "__main__":
    if len(sys.argv) < 3:
        quit("Usage - python %s file magic" % sys.argv[0])

    with open(sys.argv[1]) as f:
        rows, slots_per_row, unavailable, pools, server_count = map(int, f.readline().split())

        data_center = DataCenter(rows, slots_per_row)
        servers = []

        # Read input
        for i in range(unavailable):
            row_id, slot_id = map(int, f.readline().split())
            data_center.set(row_id, slot_id, UnavailableSlot())

        for i in range(server_count):
            size, capacity = map(int, f.readline().split())
            servers.append(Server(i, size, capacity))

        # Magic
        lib = importlib.import_module(sys.argv[2])
        lib.magic(data_center, servers)

        # Print output
        print "Score", data_center.get_score()
        for server in sorted(servers, key=lambda s: s.id):
            if not server.pool:
                print 'x'
            else:
                print "%d %d %d" % (server.row_index, server.slot_index, server.pool)
