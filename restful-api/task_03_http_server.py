#!/usr/bin/env python3
"""Simple HTTP server using http.server module.

This server handles:
- `/`        : Returns a plain text greeting.
- `/data`    : Returns a JSON object with user information.
- `/status`  : Returns 'OK' as a status check.
- Any other path returns 404 Not Found.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """Custom HTTP request handler."""

    def do_GET(self):
        """Handle GET requests."""
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode("utf-8") + b"\n")

        elif self.path == "/info":
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(info).encode("utf-8"))


        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
            self.wfile.write(json.dumps(message).encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"error": "Endpoint not found"}')


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    """Start the HTTP server."""
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on http://localhost:{port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()

