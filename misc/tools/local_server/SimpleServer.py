import SimpleHTTPServer
import SocketServer
import logging
import cgi

PORT = 8080
IP   = "192.168.178.37"

class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        logging.error(self.headers)
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        logging.error(self.headers)
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })
        for item in form.list:
            logging.error(item)
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)


Handler = ServerHandler

httpd = SocketServer.TCPServer((IP, PORT), Handler)

print "serving at IP", IP
print "serving at port", PORT
httpd.serve_forever()
