from framework.classes import ResponseT
from framework.handlers.read_static import read_static


def handle_styles(_environ):
    styles = read_static("styles.css")
    status = "200 OK"
    headers = {
        "Content-type": "text/css",
    }
    return ResponseT(status, headers, styles)
