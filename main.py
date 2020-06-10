# first you need to import os module
import os
from http.server import HTTPServer, CGIHTTPRequestHandler

# The server must be created under the current directory
os.chdir('.')
# as an http server it should listen to port 80 or 8080
# creating object
server_object = HTTPServer(server_address=('', 80), RequestHandlerClass=CGIHTTPRequestHandler)
# finally starting the web server
server_object.serve_forever()

