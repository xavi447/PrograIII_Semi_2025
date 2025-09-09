from http.server import HTTPServer, SimpleHTTPRequestHandler
port = 3000
class miServidor(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"
            return SimpleHTTPRequestHandler.do_GET(self)

print("servidor ejecutandose")
server= HTTPServer(("localhost",port),miServidor)
server.serve_forever()