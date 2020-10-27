import mimetypes
import random

from framework.consts import DIR_STATIC


def handle_index(dgdfgdf):
    gfdg = read_static("index.html")
    return gfdg


def handle_logo(ddddqd):
    ...


def application(environ, start_response):
    url = environ["PATH_INFO"]

    handlers = {
        "/": handle_index,
        "/logo.png/": handle_logo,
    }
    handler = handlers.get(url, generate_404)

    status = "200 OK"
    headers = {
        "Content-type": "text/html",
    }

    payload = handler(environ)
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
