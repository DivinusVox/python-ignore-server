#!/usr/bin/env python
import argparse
import socket
import SocketServer

class IgnoreHandler(SocketServer.BaseRequestHandler):
    """
    Handler to ignore incoming requests.
    """
    def handle(self):
        self.request.close()


def main():
    parser = argparse.ArgumentParser(
            description="Basic socket server which ignores traffic on the \
            specified port.")
    parser.add_argument('--port', '-p',
                        metavar='port',
                        required=True,
                        type=int,
                        help='Numeral value of the port to bind')
    args = parser.parse_args()

    HOST = ''
    PORT = args.port

    try:
        server = SocketServer.TCPServer((HOST, PORT), IgnoreHandler)
    except socket.error as e:
        print('Unable to bind socket {}'.format(PORT))
        print('ERROR: {}'.format(e[1]))
        exit()

    server.serve_forever()


if __name__ == '__main__':
    main()
