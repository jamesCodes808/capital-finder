from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):


    def do_GET(self):
        s = self.path
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        return