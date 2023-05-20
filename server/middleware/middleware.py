from flask import jsonify
from flask_http_middleware import BaseHTTPMiddleware
import os

class AccessMiddleware(BaseHTTPMiddleware):
    def __init__(self):
        super().__init__()

    def dispatch(self, request, call_next):
        print("middleware working")
        return call_next(request)

    def error_handler(self, error):
        return jsonify({"error": str(error)})