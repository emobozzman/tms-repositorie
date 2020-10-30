import mimetypes
import random

from framework.consts import DIR_STATIC


def handle_index(_dgdfgdf):
    gfdg = read_static("index.html")
    status = "200 OK"
    headers = {
        "Content-type": "text/html",
    }
    return status, headers, gfdg


def handle_logo(_environ):
    logo = read_static("logo.png")
    status = "200 OK"
    headers = {
        "Content-type": "img/png",
    }
    return status, headers, logo


def handle_styles(_environ):
    styles = read_static("styles.css")
    status = "200 OK"
    headers = {
        "Content-type": "text/css",
    }
    return status, headers, styles


def application(environ, start_response):
    url = environ["PATH_INFO"]

    handlers = {
        "/": handle_index,
        "/logo.png/": handle_logo,
        "/styles/": handle_styles,
    }
    handler = handlers.get(url, generate_404)
    status, headers, payload = handler(environ)
    start_response(status, list(headers.items()))

    yield payload


def read_static(file_name: str) -> bytes:
    path = DIR_STATIC / file_name

    with path.open("rb") as fp:
        payload = fp.read()

    return payload


def generate_404(environ) -> bytes:
    url = environ["PATH_INFO"]
    pin = random.randint(1, 1000)

    msg = f"Hello world! Your path: {url} not found. Pin: {pin}"

    return msg.encode()
