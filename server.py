#!/usr/bin/env python
import argparse
import datetime
import signal
import socket
import SocketServer

class IgnoreHandler(SocketServer.BaseRequestHandler):
    """
    Handler to ignore incoming requests.
    """
    def handle(self):
        if self.server.verbose:
            print('{} - From: {}'.format(datetime.datetime.now().time(), 
                                   self.request.getpeername()[0]))
        self.request.close()


def main():
    parser = argparse.ArgumentParser(
            description="Basic socket server which ignores traffic on the \
            specified port.")
    parser.add_argument('--port', '-p',
                        metavar='port',
                        required=True,
                        type=int,
                        help='Numeral value of the port to bind.')
    parser.add_argument('--verbose', '-v',
                        action='store_true',
                        help='Verbose output.')
    args = parser.parse_args()

    HOST = ''
    PORT = args.port

    try:
        server = SocketServer.TCPServer((HOST, PORT), IgnoreHandler)
        if args.verbose: server.verbose = True
    except socket.error as e:
        print('Unable to bind socket {}'.format(PORT))
        print('ERROR: {}'.format(e[1]))
        exit()

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()


if __name__ == '__main__':
    main()
