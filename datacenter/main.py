import sys
from datacenter import DataCenter
from server import Server


if __name__ == "__main__":
    if len(sys.argv) < 2:
        quit("Usage - python %s input_file" % sys.argv[0])

    try:
        with open(sys.argv[1]) as f:
            rows, slots_per_row, unavailable, pools, servers = map(int, f.readline().split())
            data_center = DataCenter(rows, slots_per_row)

            for i in range(unavailable):
                row_id, slot_id = map(int, f.readline().split())
                data_center.set(row_id, slot_id, Server.UNAVAILABLE)
            
            for i in range(servers):
                size, capacity = map(int, f.readline().split())
                server = Server(size, capacity)
    except IOError as e:
        quit("Input file error: %s" % e.args[-1])
    except (ValueError, TypeError):
        quit("Error processing file")
