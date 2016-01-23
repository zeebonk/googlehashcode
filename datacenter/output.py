def print_output(servers):
    for server in servers:
        if not server.pool:
            print 'x'
        else:
            print "%d %d %d" % (server.row_index, server.slot_index, server.pool)
