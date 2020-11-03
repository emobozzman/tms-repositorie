import traceback

from framework.classes import RequestT
from framework.classes import ResponseT


def handler_error(_request: RequestT = None) -> ResponseT:
    payload = traceback.format_exc()
    traceback.print_exc()

    payload = payload.encode()
    status = "500 Internal Server Error"
    headers = {
        "Content-type": "text/plain",
    }
    return ResponseT(status, headers, payload)
