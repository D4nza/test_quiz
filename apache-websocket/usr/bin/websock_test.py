#!/usr/bin/python

import sys
from websocket import create_connection, _exceptions

def test(sock, msg):
    sock.send(msg)
    data = sock.recv()
    return msg == data
    
if len(sys.argv) == 3:
    n, m = int(sys.argv[1]), int(sys.argv[2])
    try:
        ws = create_connection("ws://localhost/echo")
    except _exceptions.WebSocketBadStatusException:
	print 'Cannot connect socket'
	sys.exit(2)
    ws.close()
    for i in range(n):
	ws = create_connection("ws://localhost/echo")
	for j in range(m):
	    assert test(ws, 'hello'), 'Not passed'
	ws.close()
    print 'Passed'
    sys.exit(0)
else:
    print "usage: %s n m" % sys.argv[0]
    sys.exit(2)

