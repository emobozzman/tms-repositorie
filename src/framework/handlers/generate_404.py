import random

from framework.classes import RequestT
from framework.classes import ResponseT


def generate_404(request: RequestT) -> ResponseT:
    url = request.path
    pin = random.randint(1, 1000)

    msg = f"Hello world! Your path: {url} not found. Pin: {pin}"
    status = "404 Not found"
    headers = {
        "Content-type": "text/plain",
    }
    return ResponseT(status, headers, msg.encode())
