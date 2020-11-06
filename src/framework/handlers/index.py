from framework.classes import ResponseT
from framework.handlers.read_static import read_static


def handle_index(_environ):
    payload = read_static("index.html")
    status = "200 OK"
    headers = {
        "Content-type": "text/html",
    }
    return ResponseT(status, headers, payload)
