import os, http.server, socketserver

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
PORT = int(os.environ.get('PORT', 8080))
handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(('', PORT), handler) as httpd:
    print(f'Serving at http://localhost:{PORT}')
    httpd.serve_forever()
