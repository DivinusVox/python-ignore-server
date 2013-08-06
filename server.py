#/usr/bin/env python
import socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 443))
    s.listen(5)
except socket.error:
    print 'Failed to bind to socket for port 443'
    exit()

print '-- Now ignoring on port 443...'

while True:
    conn, address = s.accept()
    conn.close()
