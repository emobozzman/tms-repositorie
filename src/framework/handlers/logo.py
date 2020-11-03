from framework.classes import ResponseT
from framework.handlers.read_static import read_static


def handle_logo(_environ):
    logo = read_static("logo.png")
    status = "200 OK"
    headers = {
        "Content-type": "image/png",
    }
    return ResponseT(status, headers, logo)
