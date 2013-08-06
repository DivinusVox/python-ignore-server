#!/usr/bin/env python
import argparse
import socket

parser = argparse.ArgumentParser(description='Basic socket server which \
        ignores traffic on the specified port.')
parser.add_argument('--port', '-p',
                    metavar='port',
                    required=True,
                    type=int,
                    help='int specifying binding port')

args = parser.parse_args()

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', args.port))
    s.listen(5)
except socket.error:
    print 'Failed to bind to socket for port {}'.format(args.port)
    print 'Try:\n sudo ./server.py -p {}'.format(args.port)
    exit()

print '-- Now ignoring on port {}...'.format(args.port)

while True:
    conn, address = s.accept()
    conn.close()
