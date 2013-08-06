#!/usr/bin/env python
import SocketServer

class IgnoreHandler(SocketServer.BaseRequestHandler):
    """
    Handler to ignore incoming requests.
    """
    def handle(self):
        self.request.close()

if __name__ == '__main__':
    HOST = ''
    PORT = 9999

    server = SocketServer.TCPServer((HOST, PORT), IgnoreHandler)
    server.serve_forever()
