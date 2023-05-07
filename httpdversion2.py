from http.server import HTTPServer, BaseHTTPRequestHandler


class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/' :
            self.path = '/html/indez.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = open('404/404.html').read()
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))
        #print(self.path)





SERVER_HOST = "127.0.0.1"
SERVER_PORT  = 8080

httpd = HTTPServer((SERVER_HOST, SERVER_PORT), Serv)
httpd.serve_forever()