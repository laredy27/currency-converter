from http.server import HTTPServer, BaseHTTPRequestHandler
import router

class HTTPServerRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Serve GET requests"""
        self.respond(*router.route(self.path))
        pass

    def do_POST(self):
        """Serve POST requests"""
        content_len = int(self.headers.get('Content-Length'))
        buf = self.rfile.read(content_len)
        self.respond(*router.route(self.path, input=buf))
        return

    def respond(self, status_code, content):
        """Respond to http requests"""
        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(content.encode())
        return



def run(port):
    with HTTPServer(("", port), HTTPServerRequestHandler) as httpd:
        print("Http Server listening on port: ", port)
        httpd.serve_forever()